import datetime
import pprint
from dataclasses import dataclass
from typing import Optional

import ets2.model


@dataclass
class Job:
    config: Optional[ets2.model.JobConfig]
    started: Optional[datetime.datetime]
    ended: Optional[datetime.datetime]
    track: ets2.model.Tracks


class WorkLog:
    """A log work jobs in ETS2/ATS"""

    def __init__(self, data: ets2.model.Model):
        self._model = data
        self._model.register_observer(self)
        self._jobs = []

    def __repr__(self):
        return str(self._jobs)

    def notify(self, model: ets2.model.Model):
        if self._jobs:
            if model.job is not self._jobs[-1].config:
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
                  track=ets2.model.Tracks())
        return job

    def time_in_game(self, model):
        if model.telematic:
            started = datetime.datetime.fromordinal(1) \
                      + datetime.timedelta(minutes=model.telematic.common.game_time)
        else:
            started = None
        return started

