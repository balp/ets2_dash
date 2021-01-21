import datetime
import json
import logging
from pathlib import Path
from typing import List, Optional, Dict

import ets2.model
import ets2.tracks
from ets2.database import DataBase
from ets2.jobs import Job, Delivered, delivered_from_dict, Cancelled, cancelled_from_dict

_log = logging.getLogger("work_log")


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


class DatabaseProvider:
    """

    """

    def __init__(self):
        self._databases: Dict[str, DataBase] = {}

    def get_database(self, game_id: str) -> DataBase:
        """Returns a database instance based on the current game
        :param game_id: Id of the current game
        """
        if game_id not in self._databases:
            db_path = Path.home() / '.local' / 'share' / 'ets2_work_log'
            db_name = Path(f'{game_id}.sqlite')
            new_database = DataBase(db_path, db_name)
            _log.debug(f"open new database, {db_path}/{db_name}")
            self._databases[game_id] = new_database
        return self._databases[game_id]


class WorkLog:
    """A log work jobs in ETS2/ATS"""

    def __init__(self, data: ets2.model.Model, database_provider: DatabaseProvider) -> None:
        self._model = data
        self._model.register_observer(self)
        if database_provider is None:
            self._db_provider = DatabaseProvider()
        else:
            self._db_provider = database_provider
        self._game_id = 'no_game'
        self.jobs: List[Job] = self._db_provider.get_database(self._game_id).get_jobs()

    def __repr__(self):
        return str(self.jobs)

    def notify(self, model: ets2.model.Model, _: str):
        # Good to follow issues, but takes loots of resources in live running
        # _log.debug(f"notify:({model.job}) {len(self.jobs)}:")
        if model is None:
            _log.debug(f"no model yet")
            return
        if model.telematic is None:
            _log.debug(f"no telematic yet")
            return
        if model.game.id != self._game_id:  # Reload jobs if game have changed
            self.jobs = self._db_provider.get_database(model.game.id).get_jobs()
            self._game_id = model.game.id

        if len(self.jobs) > 0:
            current_job = self.jobs[-1]
            if model.job != current_job.config:
                _log.debug(f"start a new job")
                current_job.ended = _game_time_in_model(model)
                self._db_provider.get_database(self._game_id).save_job(current_job)
                self._add_new_job(model)
            else:
                if model.telematic:
                    if current_job.track.add_telematic(model.telematic):
                        self._db_provider.get_database(self._game_id).save_job(current_job)
        else:
            _log.debug(f"new first job")
            self._add_new_job(model)

    def _add_new_job(self, model):
        _log.debug(f"_add_new_job({model})")
        new_job = job_from_model(model)
        if new_job is not None:
            self.jobs.append(new_job)
            self._db_provider.get_database(self._game_id).save_job(new_job)
        else:
            _log.warning(f"Could not make job from {model}")

    def job_delivered(self, job_delivered: Delivered) -> None:
        _log.debug(f"job_delivered({job_delivered})")
        if self.jobs[-1].config:
            self.jobs[-1].delivered = job_delivered
            self._db_provider.get_database(self._game_id).save_job(self.jobs[-1])

    def job_cancelled(self, cancelled: Cancelled) -> None:
        _log.debug(f"job_delivered({cancelled})")
        if self.jobs[-1].config:
            self.jobs[-1].cancelled = cancelled
            self._db_provider.get_database(self._game_id).save_job(self.jobs[-1])


def add_json_to_work_log(work_log: WorkLog, json_data: json, topic: str) -> None:
    # _log.debug(f"add_json_to_work_log({work_log}, {json_data}, {topic}) -> None:")
    if topic == "ets2/info/gameplay/job.cancelled":
        work_log.job_cancelled(cancelled_from_dict(json_data))
    elif topic == "ets2/info/gameplay/job.delivered":
        work_log.job_delivered(delivered_from_dict(json_data))
