import re

from .config import TiDBConfig, TiDBConnection

config = TiDBConfig()
conn = TiDBConnection(config)

tables_sql      = f"SELECT table_name FROM information_schema.tables WHERE table_schema = '{config.tidb_db_name}'"
show_table_sql  = "SHOW TABLE {table_name} NEXT_ROW_ID"

def list_next_autoids():
    """ Loop through all tables in the database and print the AUTO_INCREMENT value """
    tables = conn.fetchall(tables_sql)
    for table in tables:
        table_name = table["table_name"]
        ids = conn.fetchall(show_table_sql.format(table_name=table_name))
        for id in ids:
            print(f"{table_name}: {id['ID_TYPE']} = {id['NEXT_GLOBAL_ROW_ID']}")
    
