import json
from dataclasses import dataclass
from typing import Optional, Dict, List

from ets2.config import TruckConfig, truckconfig_from_dict, TrailerConfig, trailer_config_from_dict
from ets2.jobs import JobConfig, jobconfig_from_dict
from ets2.telematic import Telematic, telematic_from_dict
from ets2.tracks import Tracks


@dataclass
class Info:
    paused: bool


def info_from_dict(data: Dict) -> Info:
    return Info(paused=data['paused'])


@dataclass
class Version:
    major: int
    minor: int


def version_from_dict(data: Dict) -> Version:
    return Version(data['major'], data['minor'])


@dataclass
class Game:
    id: str
    name: str
    raw_version: int
    version: Version


def game_from_dict(data: Dict) -> Game:
    return Game(id=data['id'],
                name=data['name'],
                raw_version=data['raw_version'],
                version=version_from_dict(data['version']))


class Model:
    def __init__(self):
        self._observers = []
        self.telematic: Optional[Telematic] = None
        self.job: Optional[JobConfig] = None
        self.info: Optional[Info] = None
        self.game: Optional[Game] = None
        self.truck_config: Optional[TruckConfig] = None
        self.trailer_config: List[Optional[TrailerConfig]] = [None for _ in range(10)]
        self.tracks: Tracks = Tracks()

    def register_observer(self, observer):
        self._observers.append(observer)

    def _data_changed(self, change):
        for observer in self._observers:
            observer.notify(self, change)

    def set_telematic_data(self, data):
        self.telematic = telematic_from_dict(data)
        self.tracks.add_telematic(self.telematic)
        self._data_changed("telematic")

    def set_job_config(self, data):
        self.job = jobconfig_from_dict(data)
        self._data_changed("job")

    def set_info(self, data):
        self.info = info_from_dict(data)
        self._data_changed("info")

    def set_game(self, data):
        self.game = game_from_dict(data)
        self._data_changed("game")

    def set_truck_config(self, data):
        self.truck_config = truckconfig_from_dict(data)
        self._data_changed("truck_config")

    def set_trailer_config(self, data, index):
        self.trailer_config[index] = trailer_config_from_dict(data)
        self._data_changed("trailer_config")

    def get_game_pause(self) -> Optional[bool]:
        if self.info:
            return self.info.paused
        return None

    def get_game_name(self) -> Optional[str]:
        if self.game:
            return self.game.name
        return None

    def get_game_id(self) -> Optional[str]:
        if self.game:
            return self.game.id
        return None

    def get_time_left(self) -> Optional[int]:
        if self.telematic and self.job:
            game_time = self.telematic.common.game_time
            delivery_time: int = self.job.delivery_time
            if game_time and delivery_time and delivery_time != 0xFFFFFFFF:
                return delivery_time - game_time
        return None

    def get_time_to_rest(self) -> int:
        if self.telematic:
            return self.telematic.common.rest_stop
        return 0

    def get_time_destination(self) -> int:
        if self.telematic:
            eta = self.telematic.truck.navigation_time
            return int(eta) // 60
        return 0

    def get_time_destination_with_rest(self) -> int:
        if self.telematic:

            drive_time = self.get_time_destination()
            next_rest = self.get_time_to_rest()
            total_time = drive_time

            if drive_time > next_rest:
                total_time += 9*60
                total_time += ((drive_time - next_rest) // (11 * 60)) * 9 * 60
            return int(total_time)
        return 0

    def get_speed_kmh(self) -> float:
        if self.telematic:
            return self.telematic.truck.speed * 3.6
        return 0.0

    def get_cruise_control_kmh(self) -> float:
        if self.telematic:
            return self.telematic.truck.cruise_control * 3.6
        return 0.0

    def get_speed_limit_kmh(self) -> float:
        if self.telematic:
            return self.telematic.truck.navigation_speed_limit * 3.6
        return 0.0

    def get_speed_mph(self) -> float:
        if self.telematic:
            return self.telematic.truck.speed * 2.2369363
        return 0.0

    def get_cruise_control_mph(self) -> float:
        if self.telematic:
            return self.telematic.truck.cruise_control * 2.2369363
        return 0.0

    def get_speed_limit_mph(self) -> float:
        if self.telematic:
            return self.telematic.truck.navigation_speed_limit * 2.2369363
        return 0.0

    def get_fuel_left(self) -> float:
        if self.telematic:
            return self.telematic.truck.fuel_amount
        return 0.0

    def get_fuel_range(self) -> float:
        if self.telematic:
            return self.telematic.truck.fuel_range
        return 0.0

    def get_fuel_consumtion(self) -> float:
        if self.telematic:
            return self.telematic.truck.fuel_consumption_average
        return 0.0

    def get_wear_cabin(self) -> float:
        if self.telematic:
            return self.telematic.truck.wear_cabin
        return 0.0

    def get_wear_chassis(self) -> float:
        if self.telematic:
            return self.telematic.truck.wear_chassis
        return 0.0

    def get_wear_engine(self) -> float:
        if self.telematic:
            return self.telematic.truck.wear_engine
        return 0.0

    def get_wear_transmission(self) -> float:
        if self.telematic:
            return self.telematic.truck.wear_transmission
        return 0.0

    def get_wear_wheels(self) -> float:
        if self.telematic:
            return self.telematic.truck.wear_wheels
        return 0.0

    def get_wear_trailer(self) -> float:
        if self.telematic:
            return self.telematic.trailer.wear_chassis
        return 0.0

    def get_light_high_beam(self) -> bool:
        if self.telematic:
            return self.telematic.truck.light_beam_high
        return False

    def get_light_low_beam(self) -> bool:
        if self.telematic:
            return self.telematic.truck.light_beam_low
        return False

    def get_light_beacon(self) -> bool:
        if self.telematic:
            return self.telematic.truck.light_beacon
        return False

    def get_light_l_blinker(self) -> bool:
        if self.telematic:
            return self.telematic.truck.light_lblinker
        return False

    def get_light_r_blinker(self) -> bool:
        if self.telematic:
            return self.telematic.truck.light_rblinker
        return False

    def get_l_blinker(self) -> bool:
        if self.telematic:
            return self.telematic.truck.lblinker
        return False

    def get_r_blinker(self) -> bool:
        if self.telematic:
            return self.telematic.truck.rblinker
        return False

    def get_light_parking(self) -> bool:
        if self.telematic:
            return self.telematic.truck.light_parking
        return False

    def get_light_reverse(self) -> bool:
        if self.telematic:
            return self.telematic.truck.light_reverse
        return False

    def get_light_aux_front(self) -> bool:
        if self.telematic:
            return self.telematic.truck.light_aux_front != 0
        return False

    def get_light_aux_roof(self) -> bool:
        if self.telematic:
            return self.telematic.truck.light_aux_roof != 0
        return False

    def get_light_breaking(self) -> bool:
        if self.telematic:
            return self.telematic.truck.light_brake
        return False

    def get_ad_blue_warning(self) -> bool:
        if self.telematic:
            return self.telematic.truck.adblue_warning
        return False

    def get_break_emergency(self) -> bool:
        if self.telematic:
            return self.telematic.truck.brake_air_pressure_emergency
        return False

    def get_break_warning(self) -> bool:
        if self.telematic:
            return self.telematic.truck.brake_air_pressure_warning
        return False

    def get_break_motor(self) -> bool:
        if self.telematic:
            return self.telematic.truck.brake_motor
        return False

    def get_break_parking(self) -> bool:
        if self.telematic:
            return self.telematic.truck.brake_parking
        return False

    def get_electric(self) -> bool:
        if self.telematic:
            return self.telematic.truck.electric_enabled
        return False

    def get_battery_warning(self) -> bool:
        if self.telematic:
            return self.telematic.truck.battery_voltage_warning
        return False

    def get_engine(self) -> bool:
        if self.telematic:
            return self.telematic.truck.engine_enabled
        return False

    def get_fuel_warning(self) -> bool:
        if self.telematic:
            return self.telematic.truck.fuel_warning
        return False

    def get_oil_warning(self) -> bool:
        if self.telematic:
            return self.telematic.truck.oil_pressure_warning
        return False

    def get_water_warning(self) -> bool:
        if self.telematic:
            return self.telematic.truck.water_temperature_warning
        return False

    def get_wipers(self) -> bool:
        if self.telematic:
            return self.telematic.truck.wipers
        return False

    def get_air_pressure(self) -> float:
        if self.telematic:
            return self.telematic.truck.brake_air_pressure
        return False

    def get_break_retarder(self) -> int:
        if self.telematic:
            return self.telematic.truck.brake_retarder
        return False

    def get_break_temperature(self) -> float:
        if self.telematic:
            return self.telematic.truck.brake_temperature
        return False


def add_json_to_model(model: Model, json_data: json, topic: str):
    if topic == "ets2/data":
        model.set_telematic_data(json_data)
    elif topic == "ets2/game":
        model.set_game(json_data)
    elif topic == "ets2/info":
        model.set_info(json_data)
    elif topic == "ets2/info/config/job":
        model.set_job_config(json_data)
    elif topic == "ets2/info/config/truck":
        model.set_truck_config(json_data)
    elif topic == "ets2/info/config/trailer.0":
        model.set_trailer_config(json_data, 0)
    elif topic == "ets2/info/config/trailer.1":
        model.set_trailer_config(json_data, 1)
    elif topic == "ets2/info/config/trailer.2":
        model.set_trailer_config(json_data, 2)
    elif topic == "ets2/info/config/trailer.3":
        model.set_trailer_config(json_data, 3)
    elif topic == "ets2/info/config/trailer.4":
        model.set_trailer_config(json_data, 4)
    elif topic == "ets2/info/config/trailer.5":
        model.set_trailer_config(json_data, 5)
    elif topic == "ets2/info/config/trailer.6":
        model.set_trailer_config(json_data, 6)
    elif topic == "ets2/info/config/trailer.7":
        model.set_trailer_config(json_data, 7)
    elif topic == "ets2/info/config/trailer.8":
        model.set_trailer_config(json_data, 8)
    elif topic == "ets2/info/config/trailer.9":
        model.set_trailer_config(json_data, 9)
