#  Copyright (c) 2020. Anders Arnholm <Anders@Arnholm.se>
#
#   Permission to use, copy, modify, and distribute this software for any
#   purpose with or without fee is hereby granted, provided that the above
#   copyright notice and this permission notice appear in all copies.
#
#   THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
#   WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
#   MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
#   ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
#   WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
#   ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
#   OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
from dataclasses import dataclass
from typing import Dict

from ets2.types import Vector, vector_from_dict, Placement, placement_from_dict


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
