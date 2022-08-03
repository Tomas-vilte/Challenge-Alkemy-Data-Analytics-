from sqlalchemy.sql import text
from sqlalchemy import create_engine
from constans import SQL_DIR, TABLE_NAMES
from config import DB_CONNSTR
from logger_base import log


engine = create_engine(DB_CONNSTR)
logging = log.getLogger()

def crear_tablas_sql():
    """CREAMOS TABLAS DE LA BASE DE DATOS"""
    with engine.connect() as con:
        for file in TABLE_NAMES:
            log.info(f'Creamos tabla {file} ')
            with open(SQL_DIR / f'{file}.sql') as f:
                query = text(f.read())
            
            con.execute(f'DROP TABLE IF EXISTS {file}')
            con.execute(query)

if __name__ == '__main__':
    crear_tablas_sql()