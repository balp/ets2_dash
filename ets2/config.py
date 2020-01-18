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
from typing import Dict, Optional

from ets2.types import Vector, vector_from_dict


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