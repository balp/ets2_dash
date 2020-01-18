import datetime
import json
from pathlib import Path
from typing import List, Optional

import ets2.model
import ets2.tracks
from ets2.database import DataBase
from ets2.jobs import Job, Delivered, delivered_from_dict, Cancelled, cancelled_from_dict


def time_in_game(model: ets2.model.Model):
    if model.telematic:
        started = game_time_to_datetime(model.telematic.common.game_time)
    else:
        started = None
    return started


def game_time_to_datetime(time):
    return datetime.datetime.fromordinal(1) \
           + datetime.timedelta(minutes=time)


def job_from_model(model):
    game_time = None
    if model.telematic:
        game_time = model.telematic.common.game_time
    return Job(id=None,
               config=model.job,
               started=game_time,
               ended=None,
               delivered=None,
               cancelled=None,
               track=ets2.tracks.Tracks())


def _game_time_in_model(model: ets2.model.Model) -> Optional[int]:
    game_time = None
    if model.telematic:
        game_time = model.telematic.common.game_time
    return game_time


class WorkLog:
    """A log work jobs in ETS2/ATS"""

    def __init__(self, data: ets2.model.Model, database: Optional[DataBase]) -> None:
        self._model = data
        self._model.register_observer(self)
        if database is None:
            self._db = DataBase(Path.home() / '.local/share/ets2_work_log/',
                                'work_log.sqlite')
        else:
            self._db = database
        self.jobs: List[Job] = self._db.get_jobs()

    def __repr__(self):
        return str(self.jobs)

    def notify(self, model: ets2.model.Model, _: str):
        print(f"notify:({model.job}) {len(self.jobs)}:")
        if model is None:
            return
        if model.telematic is None:
            return
        if len(self.jobs) > 0:
            current_job = self.jobs[-1]
            if model.job != current_job.config:
                print(f"start new job")
                current_job.ended = _game_time_in_model(model)
                self._db.save_job(current_job)
                self._add_new_job(model)
            else:
                if model.telematic:
                    if current_job.track.add_telematic(model.telematic):
                        self._db.save_job(current_job)
        else:
            print(f"new first job")
            self._add_new_job(model)

    def _add_new_job(self, model):
        new_job = job_from_model(model)
        self.jobs.append(new_job)
        self._db.save_job(new_job)

    def job_delivered(self, delivered: Delivered) -> None:
        if self.jobs[-1].config:
            self.jobs[-1].delivered = delivered

    def job_cancelled(self, cancelled: Cancelled) -> None:
        if self.jobs[-1].config:
            self.jobs[-1].cancelled = cancelled


def add_json_to_work_log(work_log: WorkLog, json_data: json, topic: str) -> None:
    if topic == "ets2/info/gameplay/job.cancelled":
        work_log.job_cancelled(cancelled_from_dict(json_data))
    elif topic == "ets2/info/gameplay/job.delivered":
        work_log.job_delivered(delivered_from_dict(json_data))
