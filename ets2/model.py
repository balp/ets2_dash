import json
from dataclasses import dataclass
from operator import attrgetter
from typing import Optional, Dict, List


@dataclass
class Common:
    game_time: int
    scale: float
    rest_stop: int


def common_from_dict(data: Dict):
    return Common(game_time=data['common']['game.time'],
                  scale=data['common']['local.scale'],
                  rest_stop=data['common']['rest.stop'])


@dataclass
class Vector:
    x: float
    y: float
    z: float


def vector_from_dict(value: Dict) -> Vector:
    return Vector(value['x'], value['y'], value['z'])


@dataclass
class Euler:
    heading: float
    pitch: float
    roll: float


def euler_from_dict(value: Dict) -> Euler:
    return Euler(value['heading'], value['pitch'], value['roll'])


@dataclass
class Placement:
    position: Vector
    orientation: Euler


def placement_from_dict(value: Dict) -> Placement:
    return Placement(position=vector_from_dict(value['position']),
                     orientation=euler_from_dict(value['orientation']))


@dataclass
class Trailer:
    acceleration_angular: Vector
    acceleration_linear: Vector
    cargo_damage: float
    connected: bool
    velocity_angular: Vector
    velocity_linear: Vector
    wear_chassis: float
    wear_wheels: float
    world_placement: Placement


def trailer_from_dict(data: Dict) -> Trailer:
    trailer_ = data['trailer']
    return Trailer(acceleration_angular=vector_from_dict(trailer_['trailer.acceleration.angular']),
                   acceleration_linear=vector_from_dict(trailer_['trailer.acceleration.linear']),
                   cargo_damage=trailer_['trailer.cargo.damage'],
                   connected=trailer_['trailer.connected'],
                   velocity_angular=vector_from_dict(trailer_['trailer.velocity.angular']),
                   velocity_linear=vector_from_dict(trailer_['trailer.velocity.linear']),
                   wear_chassis=trailer_['trailer.wear.chassis'],
                   wear_wheels=trailer_['trailer.wear.wheels'],
                   world_placement=placement_from_dict(trailer_['trailer.world.placement']))


@dataclass
class Truck:
    adblue: float
    adblue_warning: bool
    battery_voltage: float
    battery_voltage_warning: bool
    brake_air_pressure: float
    brake_air_pressure_emergency: bool
    brake_air_pressure_warning: bool
    brake_motor: bool
    brake_parking: bool
    brake_retarder: int
    brake_temperature: float
    cabin_acceleration_angular: Vector
    cabin_offset: Placement
    cabin_velocity_angular: Vector
    cruise_control: float
    dashboard_backlight: float
    displayed_gear: int
    effective_brake: float
    effective_clutch: float
    effective_steering: float
    effective_throttle: float
    electric_enabled: bool
    engine_enabled: bool
    engine_gear: int
    engine_rpm: float
    fuel_amount: float
    fuel_consumption_average: float
    fuel_range: float
    fuel_warning: bool
    head_offset: Placement
    hshifter_slot: int
    input_brake: float
    input_clutch: float
    input_steering: float
    input_throttle: float
    lblinker: bool
    rblinker: bool
    light_aux_front: int
    light_aux_roof: int
    light_beacon: bool
    light_beam_high: bool
    light_beam_low: bool
    light_brake: bool
    light_lblinker: bool
    light_parking: bool
    light_rblinker: bool
    light_reverse: bool
    local_acceleration_angular: Vector
    local_acceleration_linear: Vector
    local_velocity_angular: Vector
    local_velocity_linear: Vector
    navigation_distance: float
    navigation_speed_limit: float
    navigation_time: float
    odometer: float
    oil_pressure: float
    oil_pressure_warning: bool
    oil_temperature: float
    speed: float
    water_temperature: float
    water_temperature_warning: bool
    wear_cabin: float
    wear_chassis: float
    wear_engine: float
    wear_transmission: float
    wear_wheels: float
    wipers: bool
    world_placement: Placement


def truck_from_dict(data: Dict):
    truck_ = data['truck']
    return Truck(adblue=truck_['truck.adblue'],
                 adblue_warning=truck_['truck.adblue.warning'],
                 battery_voltage=truck_['truck.battery.voltage'],
                 battery_voltage_warning=truck_['truck.battery.voltage.warning'],
                 brake_air_pressure=truck_['truck.brake.air.pressure'],
                 brake_air_pressure_emergency=truck_['truck.brake.air.pressure.emergency'],
                 brake_air_pressure_warning=truck_['truck.brake.air.pressure.warning'],
                 brake_motor=truck_['truck.brake.motor'],
                 brake_parking=truck_['truck.brake.parking'],
                 brake_retarder=truck_['truck.brake.retarder'],
                 brake_temperature=truck_['truck.brake.temperature'],
                 cabin_acceleration_angular=vector_from_dict(truck_['truck.cabin.acceleration.angular']),
                 cabin_offset=placement_from_dict(truck_['truck.cabin.offset']),
                 cabin_velocity_angular=vector_from_dict(truck_['truck.cabin.velocity.angular']),
                 cruise_control=truck_['truck.cruise_control'],
                 dashboard_backlight=truck_['truck.dashboard.backlight'],
                 displayed_gear=truck_['truck.displayed.gear'],
                 effective_brake=truck_['truck.effective.brake'],
                 effective_clutch=truck_['truck.effective.clutch'],
                 effective_steering=truck_['truck.effective.steering'],
                 effective_throttle=truck_['truck.effective.throttle'],
                 electric_enabled=truck_['truck.electric.enabled'],
                 engine_enabled=truck_['truck.engine.enabled'],
                 engine_gear=truck_['truck.engine.gear'],
                 engine_rpm=truck_['truck.engine.rpm'],
                 fuel_amount=truck_['truck.fuel.amount'],
                 fuel_consumption_average=truck_['truck.fuel.consumption.average'],
                 fuel_range=truck_['truck.fuel.range'],
                 fuel_warning=truck_['truck.fuel.warning'],
                 head_offset=placement_from_dict(truck_['truck.head.offset']),
                 hshifter_slot=truck_['truck.hshifter.slot'],
                 input_brake=truck_['truck.input.brake'],
                 input_clutch=truck_['truck.input.clutch'],
                 input_steering=truck_['truck.input.steering'],
                 input_throttle=truck_['truck.input.throttle'],
                 lblinker=truck_['truck.lblinker'],
                 rblinker=truck_['truck.rblinker'],
                 light_aux_front=truck_['truck.light.aux.front'],
                 light_aux_roof=truck_['truck.light.aux.roof'],
                 light_beacon=truck_['truck.light.beacon'],
                 light_beam_high=truck_['truck.light.beam.high'],
                 light_beam_low=truck_['truck.light.beam.low'],
                 light_brake=truck_['truck.light.brake'],
                 light_lblinker=truck_['truck.light.lblinker'],
                 light_parking=truck_['truck.light.parking'],
                 light_rblinker=truck_['truck.light.rblinker'],
                 light_reverse=truck_['truck.light.reverse'],
                 local_acceleration_angular=vector_from_dict(truck_['truck.local.acceleration.angular']),
                 local_acceleration_linear=vector_from_dict(truck_['truck.local.acceleration.linear']),
                 local_velocity_angular=vector_from_dict(truck_['truck.local.velocity.angular']),
                 local_velocity_linear=vector_from_dict(truck_['truck.local.velocity.linear']),
                 navigation_distance=truck_['truck.navigation.distance'],
                 navigation_speed_limit=truck_['truck.navigation.speed.limit'],
                 navigation_time=truck_['truck.navigation.time'],
                 odometer=truck_['truck.odometer'],
                 oil_pressure=truck_['truck.oil.pressure'],
                 oil_pressure_warning=truck_['truck.oil.pressure.warning'],
                 oil_temperature=truck_['truck.oil.temperature'],
                 speed=truck_['truck.speed'],
                 water_temperature=truck_['truck.water.temperature'],
                 water_temperature_warning=truck_['truck.water.temperature.warning'],
                 wear_cabin=truck_['truck.wear.cabin'],
                 wear_chassis=truck_['truck.wear.chassis'],
                 wear_engine=truck_['truck.wear.engine'],
                 wear_transmission=truck_['truck.wear.transmission'],
                 wear_wheels=truck_['truck.wear.wheels'],
                 wipers=truck_['truck.wipers'],
                 world_placement=placement_from_dict(truck_['truck.world.placement']))


@dataclass
class Telematic:
    common: Common
    trailer: Trailer
    truck: Truck


def telematic_from_dict(data: Dict):
    common = common_from_dict(data)
    trailer = trailer_from_dict(data)
    truck = truck_from_dict(data)
    return Telematic(common=common,
                     trailer=trailer,
                     truck=truck)


@dataclass
class JobConfig:
    cargo: str
    cargo_id: str
    cargo_mass: float
    delivery_time: int
    destination_city: str
    destination_city_id: str
    destination_company: str
    destination_company_id: str
    income: int
    source_city: str
    source_city_id: str
    source_company: str
    source_company_id: str


def jobconfig_from_dict(data: Dict) -> Optional[JobConfig]:
    if len(data):
        return JobConfig(cargo=data['cargo'],
                         cargo_id=data['cargo.id'],
                         cargo_mass=data['cargo.mass'],
                         delivery_time=data['delivery.time'],
                         destination_city=data['destination.city'],
                         destination_city_id=data['destination.city.id'],
                         destination_company=data['destination.company'],
                         destination_company_id=data['destination.company.id'],
                         income=data['income'],
                         source_city=data['source.city'],
                         source_city_id=data['source.city.id'],
                         source_company=data['source.company'],
                         source_company_id=data['source.company.id'])
    else:
        return None


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


@dataclass
class TruckConfig:
    id: str
    name: str
    adblue_capacity: float
    adblue_warning_factor: float
    battery_voltage_warning: float
    brake_air_pressure_emergency: float
    brake_air_pressure_warning: float
    brand: str
    brand_id: str
    cabin_position: Vector
    differential_ratio: float
    forward_ratio: float
    fuel_capacity: float
    fuel_warning_factor: float
    gears_forward: int
    gears_reverse: int
    head_position: Vector
    hook_position: Vector
    license_plate: str
    license_plate_country: str
    license_plate_country_id: str
    oil_pressure_warning: float
    retarder_steps: int
    reverse_ratio: float
    rpm_limit: float
    water_temperature_warning: float
    wheel_position: Vector
    wheel_powered: bool
    wheel_radius: float
    wheel_simulated: bool
    wheel_steerable: bool
    wheels_count: bool


def truckconfig_from_dict(data: Dict) -> Optional[TruckConfig]:
    if len(data):
        return TruckConfig(
            id=data['id'],
            name=data['name'],
            adblue_capacity=data['adblue.capacity'],
            adblue_warning_factor=data['adblue.warning.factor'],
            battery_voltage_warning=data['battery.voltage.warning'],
            brake_air_pressure_emergency=data['brake.air.pressure.emergency'],
            brake_air_pressure_warning=data['brake.air.pressure.warning'],
            brand=data['brand'],
            brand_id=data['brand_id'],
            cabin_position=vector_from_dict(data['cabin.position']),
            differential_ratio=data['differential.ratio'],
            forward_ratio=data['forward.ratio'],
            fuel_capacity=data['fuel.capacity'],
            fuel_warning_factor=data['fuel.warning.factor'],
            gears_forward=data['gears.forward'],
            gears_reverse=data['gears.reverse'],
            head_position=vector_from_dict(data['head.position']),
            hook_position=vector_from_dict(data['hook.position']),
            license_plate=data['license.plate'],
            license_plate_country=data['license.plate.country'],
            license_plate_country_id=data['license.plate.country.id'],
            oil_pressure_warning=data['oil.pressure.warning'],
            retarder_steps=data['retarder.steps'],
            reverse_ratio=data['reverse.ratio'],
            rpm_limit=data['rpm.limit'],
            water_temperature_warning=data['water.temperature.warning'],
            wheel_position=vector_from_dict(data['wheel.position']),
            wheel_powered=data['wheel.powered'],
            wheel_radius=data['wheel.radius'],
            wheel_simulated=data['wheel.simulated'],
            wheel_steerable=data['wheel.steerable'],
            wheels_count=data['wheels.count'],
        )
    else:
        return None


@dataclass
class TrailerConfig:
    id: str
    body_type: Optional[str]
    chain_type: Optional[str]
    cargo_accessory_id: str
    hook_position: Vector
    license_plate: str
    license_plate_country: str
    license_plate_country_id: str
    wheel_position: Vector
    wheel_powered: bool
    wheel_radius: float
    wheel_simulated: bool
    wheel_steerable: bool
    wheels_count: int


def trailer_config_from_dict(data: Dict) -> Optional[TrailerConfig]:
    if len(data):
        return TrailerConfig(
            id=data['id'],
            body_type=(data['body.type'] if 'body.type' in data else None),
            chain_type=(data['chain.type'] if 'chain.type' in data else None),
            cargo_accessory_id=data['cargo.accessory.id'],
            hook_position=vector_from_dict(data['hook.position']),
            license_plate=data['license.plate'],
            license_plate_country=data['license.plate.country'],
            license_plate_country_id=data['license.plate.country.id'],
            wheel_position=vector_from_dict(data['wheel.position']),
            wheel_powered=data['wheel.powered'],
            wheel_radius=data['wheel.radius'],
            wheel_simulated=data['wheel.simulated'],
            wheel_steerable=data['wheel.steerable'],
            wheels_count=data['wheels.count'],
        )
    else:
        return None


class Tracks:
    """Keep tracks of where the truck been"""
    def __init__(self):
        self.points: List[Placement] = []
        self.last_time = 0

    def __str__(self):
        return str(self.points)

    def __repr__(self):
        return str(self.points)

    def add_telematic(self, telematic: Telematic) -> bool:
        if telematic.common.game_time > self.last_time:
            self.last_time = telematic.common.game_time
            self.points.append(telematic.truck.world_placement)
            return True
        return False

    def bottom_left(self) -> (int, int):
        if self.points:
            x = min(self.points, key=attrgetter('position.x')).position.x
            y = min(self.points, key=attrgetter('position.y')).position.y
            z = min(self.points, key=attrgetter('position.z')).position.z
            return x, y, z
        return -139999, 20000  # ATS Hack

    def top_right(self) -> (int, int):
        if self.points:
            x = max(self.points, key=attrgetter('position.x')).position.x
            y = max(self.points, key=attrgetter('position.y')).position.y
            z = max(self.points, key=attrgetter('position.z')).position.z
            return x, y, z
        return -20000, -85000  # ATS Hack


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
