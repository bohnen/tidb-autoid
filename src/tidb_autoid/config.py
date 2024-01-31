import os

import pymysql
from dotenv import load_dotenv
from pymysql import Connection
from pymysql.cursors import DictCursor


class TiDBConfig:
    def __init__(self):
        dotenv_path = os.path.join(os.getcwd(), ".env")
        load_dotenv(dotenv_path,verbose=True)
        self.tidb_host = os.getenv("TIDB_HOST")
        self.tidb_port = int(os.getenv("TIDB_PORT"))
        self.tidb_user = os.getenv("TIDB_USER")
        self.tidb_password = os.getenv("TIDB_PASSWORD")
        self.tidb_db_name = os.getenv("TIDB_DB_NAME")
        self.ca_path = os.getenv("CA_PATH")

class TiDBConnection:
    def __init__(self, config: TiDBConfig):
        self.config = config

    def get_connection(self,autocommit: bool = True) -> Connection:
        config = self.config
        db_conf = {
            "host": config.tidb_host,
            "port": config.tidb_port,
            "user": config.tidb_user,
            "password": config.tidb_password,
            "database": config.tidb_db_name,
            "autocommit": autocommit,
            "cursorclass": DictCursor,
        }

        if config.ca_path:
            db_conf["ssl_verify_cert"] = True
            db_conf["ssl_verify_identity"] = True
            db_conf["ssl_ca"] = config.ca_path

        return pymysql.connect(**db_conf)

    def fetchall(self, sql: str) -> list:
        with self.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(sql)
                return cursor.fetchall()
    
    def fetchone(self, sql: str) -> dict:
        with self.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(sql)
                return cursor.fetchone()