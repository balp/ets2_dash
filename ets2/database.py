import sqlite3
from typing import List

from ets2.jobs import Job, Delivered, Cancelled, JobConfig
from ets2.types import Vector
from ets2.tracks import Tracks, TrackPoint


def _get_job_delivered(curr2, job, job_id):
    curr2.execute('select auto_load, auto_park, cargo_damage, time,'
                  ' distance, xp, revenue from job_delivered where id=?',
                  (job_id,))
    r = curr2.fetchone()
    if r is not None:
        print(f"Got delivered {r}")
        job.delivered = Delivered(auto_load=r[0],
                                  auto_park=r[1],
                                  cargo_damage=r[2],
                                  time=r[3],
                                  distance=r[4],
                                  xp=r[5],
                                  revenue=r[6])


def _get_job_config(curr2, job, job_id):
    curr2.execute('select cargo, cargo_id, cargo_mass,'
                  ' delivery_time, destination_city, destination_city_id,'
                  ' destination_company, destination_company_id,'
                  ' income, source_city, source_city_id,'
                  ' source_company, source_company_id from job_config where id=?',
                  (job_id,))
    r = curr2.fetchone()
    if r is not None:
        print(f"Got config {r}")
        job.config = JobConfig(cargo=r[0],
                               cargo_id=r[1],
                               cargo_mass=r[2],
                               delivery_time=r[3],
                               destination_city=r[4],
                               destination_city_id=r[5],
                               destination_company=r[6],
                               destination_company_id=r[7],
                               income=r[8],
                               source_city=r[9],
                               source_city_id=r[10],
                               source_company=r[11],
                               source_company_id=r[12])


def _get_job_cancelled(curr2, job, job_id):
    curr2.execute('select penalty from job_cancelled where id=?',
                  (job_id,))
    r = curr2.fetchone()
    if r is not None:
        print(f"Got config {r}")
        job.cancelled = Cancelled(penalty=r[0])


def _get_job_track(curr2, job, job_id):
    curr2.execute('select last_time from tracks where id=?',
                  (job_id,))
    r = curr2.fetchone()
    if r is not None:
        print(f"Got config {r}")
        job.track.last_time = r[0]

    for count, time, x, y, z in curr2.execute('select count, time, x, y, z from track_point'
                                              ' where id=?'
                                              ' order by count', (job_id,)):
        job.track.points.append(TrackPoint(position=Vector(x=x, y=y, z=z), time=time))


class DataBase:
    def __init__(self, db_path, db_name):
        db_path.mkdir(parents=True, exist_ok=True)
        database = db_path / db_name
        print(f"DataBase.__init__(... {database.absolute()} ...)")
        self._conn = sqlite3.connect(database.absolute(), isolation_level=None)
        cursor = self._conn.cursor()
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
                cargo_mass             real,
                delivery_time          integer,
                destination_city       text,
                destination_city_id    text,
                destination_company    text,
                destination_company_id text,
                income                 integer,
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
""")
        cursor.close()

    def save_job(self, job: Job) -> int:
        print(f"Save job {job.id}: {job.started}")
        if job is None:
            return -1
        cursor = self._conn.cursor()
        if job.id is not None:
            print(f"update job set started = {job.started}, ended = {job.ended} where id = {job.id}")
            cursor.execute("update job set started = ?, ended = ? where id = ?",
                           (job.started, job.ended, job.id))
            job_id = job.id
        else:
            print(f"insert into job (started, ended) values ({job.started},{job.ended})")
            cursor.execute("insert into job (started, ended) values (?,?)",
                           (job.started, job.ended))
            job.id = cursor.lastrowid
            job_id = job.id
        if job.config is not None:
            cursor.execute("replace into job_config (id, cargo, cargo_id, cargo_mass, delivery_time, "
                           "                         destination_city, destination_city_id, destination_company,"
                           "                         destination_company_id, income, source_city, source_city_id,"
                           "                         source_company, source_company_id)"
                           "   values (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                           (job.id,
                            job.config.cargo,
                            job.config.cargo_id,
                            job.config.cargo_mass,
                            job.config.delivery_time,
                            job.config.destination_city,
                            job.config.destination_city_id,
                            job.config.destination_company,
                            job.config.destination_company_id,
                            job.config.income,
                            job.config.source_city,
                            job.config.source_city_id,
                            job.config.source_company,
                            job.config.source_company_id))
        if job.delivered is not None:
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
        if job.cancelled is not None:
            cursor.execute("replace into job_cancelled (id, penalty) values (?,?)",
                           (job.id, job.cancelled.penalty))
        cursor.execute("replace into tracks (id, last_time) values (?,?)", (job.id, job.track.last_time))
        for i, point in enumerate(job.track.points):
            cursor.execute("replace into track_point (id, count, time, x, y, z) values (?,?,?,?,?,?)",
                           (job.id, i, point.time, point.position.x, point.position.y, point.position.z))
        cursor.close()
        return job_id

    def get_jobs(self) -> List[Job]:
        jobs: List[Job] = []
        curr = self._conn.cursor()
        for job_id, started, ended in curr.execute('select id, started, ended from job order by id'):
            print(f"job_id '{job_id}' {type(job_id)}, started '{started}', ended '{ended}'")
            job = Job(config=None, started=started, ended=ended, delivered=None, cancelled=None,
                      track=Tracks(), id=job_id)
            curr2 = self._conn.cursor()
            _get_job_config(curr2, job, job_id)
            _get_job_delivered(curr2, job, job_id)
            _get_job_cancelled(curr2, job, job_id)
            _get_job_track(curr2, job, job_id)

            jobs.append(job)
            curr2.close()
        curr.close()
        return jobs
