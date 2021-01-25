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

import logging
import sqlite3 as db
import threading
from pathlib import Path
from typing import List, Dict

from ets2.jobs import Job, Delivered, Cancelled, JobConfig
from ets2.types import Vector
from ets2.tracks import Tracks, TrackPoint

_log = logging.getLogger("database")


def _get_job_delivered(curr2, job, job_id):
    _log.debug(f"_get_job_delivered(curr2, {job}, {job_id}):")
    curr2.execute('select auto_load, auto_park, cargo_damage, time,'
                  ' distance, xp, revenue from job_delivered where id=?',
                  (job_id,))
    r = curr2.fetchone()
    if r is not None:
        _log.debug(f"Got delivered {r}")
        job.delivered = Delivered(auto_load=r[0],
                                  auto_park=r[1],
                                  cargo_damage=r[2],
                                  time=r[3],
                                  distance=r[4],
                                  xp=r[5],
                                  revenue=r[6])


def _get_job_config(curr2, job, job_id):
    curr2.execute('select cargo, cargo_id, cargo_loaded, cargo_mass,'
                  ' cargo_unit_count, cargo_unit_mass, delivery_time, destination_city, destination_city_id,'
                  ' destination_company, destination_company_id,'
                  ' income, is_special_job, job_market, planned_distance_km, source_city, source_city_id,'
                  ' source_company, source_company_id from job_config where id=?',
                  (job_id,))
    r = curr2.fetchone()
    if r is not None:
        _log.debug(f"Got config {r}")
        job.config = JobConfig(cargo=r[0],
                               cargo_id=r[1],
                               cargo_loaded=r[2],
                               cargo_mass=r[3],
                               cargo_unit_count=r[4],
                               cargo_unit_mass=r[5],
                               delivery_time=r[6],
                               destination_city=r[7],
                               destination_city_id=r[8],
                               destination_company=r[9],
                               destination_company_id=r[10],
                               income=r[11],
                               is_special_job=r[12],
                               job_market=r[13],
                               planned_distance_km=r[14],
                               source_city=r[15],
                               source_city_id=r[16],
                               source_company=r[17],
                               source_company_id=r[18])


def _get_job_cancelled(curr2, job, job_id):
    curr2.execute('select penalty from job_cancelled where id=?',
                  (job_id,))
    r = curr2.fetchone()
    if r is not None:
        _log.debug(f"Got config {r}")
        job.cancelled = Cancelled(penalty=r[0])


def _get_job_track(curr2, job, job_id):
    curr2.execute('select last_time from tracks where id=?',
                  (job_id,))
    r = curr2.fetchone()
    if r is not None:
        _log.debug(f"Got config {r}")
        job.track.last_time = r[0]

    for count, time, x, y, z in curr2.execute('select count, time, x, y, z from track_point'
                                              ' where id=?'
                                              ' order by count', (job_id,)):
        job.track.points.append(TrackPoint(position=Vector(x=x, y=y, z=z), time=time))


def _save_job(cursor, job):
    _log.debug(f"_save_job(self, cursor, {job})")
    if job.id is not None:
        _log.debug(f"update job set started = {job.started}, ended = {job.ended} where id = {job.id}")
        cursor.execute("update job set started = ?, ended = ? where id = ?",
                       (job.started, job.ended, job.id))
        job_id = job.id
    else:
        _log.debug(f"insert into job (started, ended) values ({job.started},{job.ended})")
        cursor.execute("insert into job (started, ended) values (?,?)",
                       (job.started, job.ended))
        job.id = cursor.lastrowid
        job_id = job.id
    _log.debug(f"_save_job(...) -> {job_id}")
    return job_id


def _save_tracks(cursor, job):
    number_of_track_points = len(job.track.points)
    _log.debug(f"replace into tracks (id, last_time) values ({job.id}, {job.track.last_time})) # {number_of_track_points}")
    cursor.execute("replace into tracks (id, last_time) values (?,?)", (job.id, job.track.last_time))
    # for i, point in enumerate(job.track.points):
    if number_of_track_points > 0:
        last_index = number_of_track_points - 1
        point = job.track.points[-1]
        _log.debug(f"replace into track_point (id, count, time, x, y, z) values ({job.id}, {last_index}, {point.time},"
                   f" {point.position.x}, {point.position.y}, {point.position.z})")
        cursor.execute("replace into track_point (id, count, time, x, y, z) values (?,?,?,?,?,?)",
                       (job.id, last_index, point.time, point.position.x, point.position.y, point.position.z))


def _save_job_cancelled(cursor, job):
    _log.debug(f"_save_job_cancelled(self, cursor, {job})")
    if job.cancelled is not None:
        _log.debug(f"replace into job_cancelled (id, penalty) values ({job.id}, {job.cancelled.penalty})")
        cursor.execute("replace into job_cancelled (id, penalty) values (?,?)",
                       (job.id, job.cancelled.penalty))


def _save_job_delivered(cursor, job):
    _log.debug(f"_save_job_delivered(self, cursor, {job}):")
    if job.delivered is not None:
        _log.debug(f"replace into job_delivered (id, auto_load, auto_park, cargo_damage, time,"
                   f" distance, xp, revenue) values ({job.id}, {job.delivered.auto_load},"
                   f" {job.delivered.auto_park}, {job.delivered.cargo_damage}, {job.delivered.time},"
                   f" {job.delivered.distance}, {job.delivered.xp}, {job.delivered.revenue})")
        cursor.execute("replace into job_delivered ("
                       "    id, auto_load, auto_park, cargo_damage,"
                       "    time, distance, xp, revenue)"
                       "   values (?,?,?,?,?,?,?,?)",
                       (job.id,
                        job.delivered.auto_load,
                        job.delivered.auto_park,
                        job.delivered.cargo_damage,
                        job.delivered.time,
                        job.delivered.distance,
                        job.delivered.xp,
                        job.delivered.revenue))


def _save_job_config(cursor, job):
    _log.debug(f"_save_job_config(self, cursor, {job})")
    if job.config is not None:
        cursor.execute("replace into job_config (id, cargo, cargo_id, cargo_loaded, cargo_mass, cargo_unit_count,"
                       "                         cargo_unit_mass, delivery_time, "
                       "                         destination_city, destination_city_id, destination_company,"
                       "                         destination_company_id, income, is_special_job, source_city,"
                       "                         job_market, source_city_id, planned_distance_km, "
                       "                         source_company, source_company_id)"
                       "   values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                       (job.id,
                        job.config.cargo,
                        job.config.cargo_id,
                        job.config.cargo_loaded,
                        job.config.cargo_mass,
                        job.config.cargo_unit_count,
                        job.config.cargo_unit_mass,
                        job.config.delivery_time,
                        job.config.destination_city,
                        job.config.destination_city_id,
                        job.config.destination_company,
                        job.config.destination_company_id,
                        job.config.income,
                        job.config.is_special_job,
                        job.config.job_market,
                        job.config.planned_distance_km,
                        job.config.source_city,
                        job.config.source_city_id,
                        job.config.source_company,
                        job.config.source_company_id))


def _setup_tables(cursor):
    user_version = None
    schema_version = None
    application_id = None
    cursor.execute('PRAGMA user_version')
    for version in cursor:
        user_version = version[0]
    cursor.execute('PRAGMA schema_version')
    for _schema_version in cursor:
        schema_version = _schema_version[0]
    cursor.execute('PRAGMA application_id')
    for _application_id in cursor:
        application_id = _application_id[0]
    _log.info(f"_setup_tables: user_version={user_version}, schema_version={schema_version}, application_id={application_id}")
    if application_id == 0:
        cursor.execute('PRAGMA application_id = 1337')
    elif application_id != 1337:
        _log.error(f"Unknown application id in data base: {application_id}, not adding tables")
        return
    if user_version == 0 and schema_version != 0:
        _log.debug(f"initial database had no version, e.g. 0 lets call that version 1 as 0 also is empty file")
        cursor.execute('PRAGMA user_version = 1')
        user_version = 1
    # Nice to have in development if you forget to ser new db version on upgrade
    # if user_version == 1 and schema_version == 12:
    #     cursor.execute('PRAGMA user_version = 2')
    #     user_version = 2
    if user_version == 1:
        pass
        # Upgrade v1 to v2
        cursor.executescript("""
        ALTER TABLE job_config ADD COLUMN cargo_loaded           boolean;
        ALTER TABLE job_config ADD COLUMN cargo_unit_count       integer;
        ALTER TABLE job_config ADD COLUMN cargo_unit_mass        real;
        ALTER TABLE job_config ADD COLUMN is_special_job         boolean;
        ALTER TABLE job_config ADD COLUMN job_market             text;
        ALTER TABLE job_config ADD COLUMN planned_distance_km    integer;
        PRAGMA user_version = 2;
""")
    elif user_version == 0:
        cursor.executescript("""
    
        CREATE TABLE IF NOT EXISTS job
        (
            id      integer primary key,
            started integer,
            ended   integer
        );
        
        CREATE TABLE IF NOT EXISTS job_config
        (
            id                     integer primary key,
            cargo                  text,
            cargo_id               text,
            cargo_loaded           boolean,
            cargo_mass             real,
            cargo_unit_count       integer,
            cargo_unit_mass        real,
            delivery_time          integer,
            destination_city       text,
            destination_city_id    text,
            destination_company    text,
            destination_company_id text,
            income                 integer,
            is_special_job         boolean,
            job_market             text,
            planned_distance_km    integer,
            source_city            text,
            source_city_id         text,
            source_company         text,
            source_company_id      text,
            FOREIGN KEY (id)
                REFERENCES job (id)
        );
        
        CREATE TABLE IF NOT EXISTS job_delivered
        (
            id           integer primary key,
            auto_load    integer,
            auto_park    integer,
            cargo_damage real,
            time         integer,
            distance     real,
            xp           integer,
            revenue      integer,
            FOREIGN KEY (id)
                REFERENCES job (id)
        );
        
        CREATE TABLE IF NOT EXISTS job_cancelled
        (
            id      integer primary key,
            penalty integer,
            FOREIGN KEY (id)
                REFERENCES job (id)
        );
        
        CREATE TABLE IF NOT EXISTS tracks
        (
            id    integer primary key,
            last_time integer,
            FOREIGN KEY (id)
                REFERENCES job (id)
        );
        
        CREATE TABLE IF NOT EXISTS track_point
        (
            id        integer,
            count     integer,
            time      integer,
            x real,
            y real,
            z real,
            PRIMARY KEY (id, count),
            FOREIGN KEY (id)
                REFERENCES tracks (id)
        );
        
        PRAGMA user_version = 2;
""")



class DataBase:
    def __init__(self, db_path: Path, db_name: Path):
        self._connections: Dict[int, db.Connection] = {}
        db_path.mkdir(parents=True, exist_ok=True)
        self.database = db_path / db_name
        _log.info(f"DataBase.__init__(... {self.database.absolute()} ...)")

        cursor = self._get_cursor()
        _setup_tables(cursor)
        cursor.close()

    def _get_connection(self):
        tid = threading.get_ident()
        # Some DB as SQLite need one connection per thread
        if tid not in self._connections:
            self._connections[tid] = db.connect(self.database.absolute(), isolation_level=None)
        return self._connections[tid]

    def _get_cursor(self):
        return self._get_connection().cursor()

    def save_job(self, job: Job) -> int:
        _log.debug(f"save_job(self, {job}: Job) -> :")
        # _log.debug(f"Save job id: {job.id} started: {job.started}")
        if job is None:
            _log.warning(f"save_job() on none")
            return -1
        # _log.debug("get cursor")
        try:
            cursor = self._get_cursor()
            # _log.debug("got cursor")
            job_id = _save_job(cursor, job)
            # _log.debug(f"got job_id: {job_id}")
            _save_job_config(cursor, job)
            _save_job_delivered(cursor, job)
            _save_job_cancelled(cursor, job)
            _save_tracks(cursor, job)
            cursor.close()
        except db.DatabaseError as db_err:
            _log.error(f"Database error in save_job({job.id}: {db_err})")
            raise db_err
        _log.debug(f"save_job(self, job: Job) -> {job_id}:")
        return job_id

    def get_jobs(self) -> List[Job]:
        _log.debug(f"get_jobs(self)")
        jobs: List[Job] = []
        curr = self._get_cursor()
        for job_id, started, ended in curr.execute('select id, started, ended from job order by id'):
            _log.debug(f"job_id '{job_id}' {type(job_id)}, started '{started}', ended '{ended}'")
            job = Job(config=None, started=started, ended=ended, delivered=None, cancelled=None,
                      track=Tracks(), id=job_id)
            curr2 = self._get_cursor()
            _get_job_config(curr2, job, job_id)
            _get_job_delivered(curr2, job, job_id)
            _get_job_cancelled(curr2, job, job_id)
            _get_job_track(curr2, job, job_id)

            jobs.append(job)
            curr2.close()
        curr.close()
        _log.info(f"get_jobs(self): returning {len(jobs)} jobs.")
        return jobs
