from decouple import AutoConfig
from constans import ROOT_DIR

config = AutoConfig(search_path= ROOT_DIR)


DB_CONNSTR = config('DB_CONNSTR')
MUSEO_URL = config('MUSEO_URL')
CINES_URL = config('CINES_URL')
BIBLIOTECAS = config('BIBLIOTECAS_URL')

#print(f'Datos de la base: {DB_CONNSTR}')
#print(f'Url museos: {MUSEO_URL}')

museos = {
    'name': 'museo',
    'url': MUSEO_URL,
}
cines = {
    'name': 'cines',
    'url': CINES_URL,
}

bibliotecas = {
    'name': 'bibliotecas_populares',
    'url': BIBLIOTECAS,
}