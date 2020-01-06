import datetime
import json
from dataclasses import dataclass
from typing import Optional, Dict, List

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
    started: Optional[datetime.datetime]
    ended: Optional[datetime.datetime]
    delivered: Optional[Delivered]
    cancelled: Optional[Cancelled]
    track: ets2.model.Tracks


class WorkLog:
    """A log work jobs in ETS2/ATS"""

    def __init__(self, data: ets2.model.Model):
        self._model = data
        self._model.register_observer(self)
        self._jobs: List[Job] = []

    def __repr__(self):
        return str(self._jobs)

    def notify(self, model: ets2.model.Model, change: str):
        if self._jobs:
            if model.job != self._jobs[-1].config:
                self._jobs[-1].ended = self.time_in_game(model)
                job = self.job_from_model(model)
                self._jobs.append(job)
            else:
                if model.telematic:
                    self._jobs[-1].track.add_telematic(model.telematic)
        else:
            job = self.job_from_model(model)
            self._jobs.append(job)

    def job_from_model(self, model):
        started = self.time_in_game(model)
        job = Job(config=model.job,
                  started=started,
                  ended=None,
                  delivered=None,
                  cancelled=None,
                  track=ets2.model.Tracks())
        return job

    def time_in_game(self, model):
        if model.telematic:
            started = datetime.datetime.fromordinal(1) \
                      + datetime.timedelta(minutes=model.telematic.common.game_time)
        else:
            started = None
        return started

    def job_delivered(self, delivered: Delivered) -> None:
        if self._jobs[-1].config:
            self._jobs[-1].delivered = delivered

    def job_cancelled(self, cancelled: Cancelled) -> None:
        if self._jobs[-1].config:
            self._jobs[-1].cancelled = cancelled


def add_json_to_work_log(work_log: WorkLog, json_data: json, topic: str) -> None:
    if topic == "ets2/info/gameplay/job.cancelled":
        work_log.job_cancelled(cancelled_from_dict(json_data))
    elif topic == "ets2/info/gameplay/job.delivered":
        work_log.job_delivered(delivered_from_dict(json_data))
