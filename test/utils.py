import bz2
import json
import shutil
from pathlib import Path
from typing import List, Tuple

from ets2.model import Model, add_json_to_model
from ets2.database import DataBase
from ets2.work_log import WorkLog, add_json_to_work_log


def rerun_data_from_files(files: List[str], test_case: str) -> Tuple[Model, WorkLog]:
    model = Model()

    path = Path(f'/tmp/{test_case}')
    shutil.rmtree(path, ignore_errors=True)
    database = DataBase(path, 'work_log.sqlite')
    work_log: WorkLog = WorkLog(model, database=database)
    for f in files:
        with bz2.open(f) as gj:
            for line in gj:
                topic, json_str = line.decode('utf8').split(" ", 1)
                json_data = json.loads(json_str)
                add_json_to_model(model, json_data, topic)
                add_json_to_work_log(work_log, json_data, topic)
    return model, work_log
