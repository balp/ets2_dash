import bz2
import json
import shutil
from pathlib import Path
from typing import List, Tuple

import jsonpickle as jsonpickle
from approvaltests import verify_with_namer, get_default_reporter
from approvaltests.core.namer import StackFrameNamer

from ets2.model import Model, add_json_to_model
from ets2.database import DataBase
from ets2.work_log import WorkLog, add_json_to_work_log, DatabaseProvider


class TestDataBaseProvider(DatabaseProvider):
    def __init__(self, database: DataBase):
        self._db = database

    def get_database(self, game_id: str) -> DataBase:
        return self._db


def rerun_data_from_files(files: List[str], test_case: str) -> Tuple[Model, WorkLog, DataBase]:
    model = Model()
    path = Path(f'/tmp/{test_case}')
    shutil.rmtree(path, ignore_errors=True)
    database = DataBase(path, Path('work_log.sqlite'))
    work_log: WorkLog = WorkLog(model, database_provider=TestDataBaseProvider(database))
    for f in files:
        with bz2.open(f) as gj:
            for line in gj:
                topic, json_str = line.decode('utf8').split(" ", 1)
                json_data = json.loads(json_str)
                add_json_to_model(model, json_data, topic)
                add_json_to_work_log(work_log, json_data, topic)
    return model, work_log, database


def verify_work_log_as_json(work_log: WorkLog):
    jsonpickle.set_encoder_options('json', sort_keys=True, indent=4)
    jsonpickle.set_preferred_backend('json')
    verify_with_namer(data=jsonpickle.encode(work_log.jobs),
                      namer=StackFrameNamer(extension='.json'),
                      reporter=get_default_reporter())
