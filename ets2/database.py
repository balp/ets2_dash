import sqlite3

from ets2.jobs import Job


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
                x real,
                y real,
                z real,
                PRIMARY KEY (id, count),
                FOREIGN KEY (id)
                    REFERENCES tracks (id)
            );
""")
        cursor.close()

    def save_job(self, job: Job):
        cursor = self._conn.cursor()
        if job.id is not None:
            cursor.execute("update job set started = ?, ended = ? where id = ?",
                           (job.started, job.ended, job.id))
        else:
            cursor.execute("insert into job (started, ended) values (?,?)",
                           (job.started, job.ended))
            job.id = cursor.lastrowid
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
            cursor.execute("replace into track_point (id, count, x, y, z) values (?,?,?,?,?)",
                           (job.id, i, point.position.x, point.position.y, point.position.z))
        cursor.close()
