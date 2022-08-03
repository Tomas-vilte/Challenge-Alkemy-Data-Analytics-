from pathlib import Path

BASE_FILE = Path('/home/tomi/Challenge-Data-Analytics/Datos')
ROOT_DIR = Path().parent
SQL_DIR = ROOT_DIR / 'src/sql'



CINE_INSIGHTS_TABLE_NAME = 'cines'
SOURCE_SIZE_TABLE_NAME = 'total_fuente'
CATEGORY_COUNT_TABLE_NAME = 'total_categoria'
PROV_CAT_COUNT_TABLE_NAME = 'prov_cat'

TABLE_NAMES = [
    CINE_INSIGHTS_TABLE_NAME,
    SOURCE_SIZE_TABLE_NAME,
    CATEGORY_COUNT_TABLE_NAME,
    PROV_CAT_COUNT_TABLE_NAME,
]