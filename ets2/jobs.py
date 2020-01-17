from dataclasses import dataclass
from typing import Optional, Dict

import ets2.model


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
class Job:
    config: Optional[ets2.model.JobConfig]
    started: Optional[int]
    ended: Optional[int]
    delivered: Optional[Delivered]
    cancelled: Optional[Cancelled]
    track: ets2.model.Tracks
    id: Optional[int]
