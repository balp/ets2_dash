from dataclasses import dataclass
from typing import Optional, Dict

import ets2.model
import ets2.tracks


@dataclass
class Delivered:
    auto_load: bool
    auto_park: bool
    cargo_damage: float
    time: int
    distance: float
    xp: int
    revenue: int


def delivered_from_dict(data: Dict) -> Delivered:
    return Delivered(auto_load=data['auto.load.used'], auto_park=data['auto.park.used'],
                     cargo_damage=data['cargo.damage'], time=data['delivery.time'],
                     distance=data['distance.km'], xp=data['earned.xp'], revenue=data['revenue'])


@dataclass
class Cancelled:
    penalty: int


def cancelled_from_dict(data: Dict) -> Cancelled:
    return Cancelled(penalty=data['cancel.penalty'])


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
class Job:
    config: Optional[JobConfig]
    started: Optional[int]
    ended: Optional[int]
    delivered: Optional[Delivered]
    cancelled: Optional[Cancelled]
    track: ets2.tracks.Tracks
    id: Optional[int]

