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
    cargo: Optional[str]
    cargo_id: Optional[str]
    cargo_loaded: Optional[bool]
    cargo_mass: Optional[float]
    cargo_unit_count: Optional[int]
    cargo_unit_mass: Optional[float]
    delivery_time: Optional[int]
    destination_city: Optional[str]
    destination_city_id: Optional[str]
    destination_company: Optional[str]
    destination_company_id: Optional[str]
    income: Optional[int]
    is_special_job: Optional[bool]
    job_market: Optional[str]
    planned_distance_km: Optional[int]
    source_city: Optional[str]
    source_city_id: Optional[str]
    source_company: Optional[str]
    source_company_id: Optional[str]


def jobconfig_from_dict(data: Dict) -> Optional[JobConfig]:
    if len(data):
        return JobConfig(cargo=data.get('cargo'),
                         cargo_id=data.get('cargo.id'),
                         cargo_loaded=data.get('cargo.loaded'),
                         cargo_mass=data.get('cargo.mass'),
                         cargo_unit_count=data.get('cargo.unit.count'),
                         cargo_unit_mass=data.get('cargo.unit.mass'),
                         delivery_time=data.get('delivery.time'),
                         destination_city=data.get('destination.city'),
                         destination_city_id=data.get('destination.city.id'),
                         destination_company=data.get('destination.company'),
                         destination_company_id=data.get('destination.company.id'),
                         income=data.get('income'),
                         is_special_job=data.get('is.special.job'),
                         job_market=data.get('job.market'),
                         planned_distance_km=data.get('planned_distance.km'),
                         source_city=data.get('source.city'),
                         source_city_id=data.get('source.city.id'),
                         source_company=data.get('source.company'),
                         source_company_id=data.get('source.company.id'))
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

