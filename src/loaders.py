from sqlalchemy import column, create_engine
from config import *
import pandas as pd
from constans import(CINE_INSIGHTS_TABLE_NAME, CATEGORY_COUNT_TABLE_NAME, SOURCE_SIZE_TABLE_NAME, PROV_CAT_COUNT_TABLE_NAME)
from datetime import *
import numpy as np


engine = create_engine("postgresql://postgres:postgres@localhost/data_analytics")

class baseLoader:
    def cargar_tabla(self, df):
        df.to_sql(self.table_name, con = engine, index= False, if_exists='replace')


class cineinsightsloader(baseLoader):  
    table_name = CINE_INSIGHTS_TABLE_NAME
    def cargar_tabla(self, file_path):
        #Hoy = datetime.now()
        #Fecha = str(Hoy.year) + "-" + str(Hoy.month) + "-" + str(Hoy.day) # Fecha para dato de día de carga
        df = pd.read_csv(file_path)
        
        insights_df = df.groupby('Provincia', as_index=False).count()[
           ['Provincia', 'Pantallas', 'Butacas', 'espacio_INCAA']
        ]
        return super().cargar_tabla(insights_df)
        
class sizeByCategoryLoader(baseLoader):
    table_name = CATEGORY_COUNT_TABLE_NAME
    def cargar_tabla(self, file_path):
        df = pd.read_csv(file_path)
        dff = df.groupby(['categoria'], as_index=False).size()
        return super().cargar_tabla(dff)

class sizeBySourceLoader(baseLoader):
    table_name = SOURCE_SIZE_TABLE_NAME
    def cargar_tabla(self, file_path):
        lst = list()
        
        for name, file_path in file_path.items():
            df = pd.read_csv(file_path)
            lst.append({'Fuente': name, 'Total': df.size})

        df_source = pd.DataFrame(lst)
        return super().cargar_tabla(df_source)

class sizeByCatProvLoader(baseLoader):
    table_name = PROV_CAT_COUNT_TABLE_NAME
    def cargar_tabla(self, file_path):
        df = pd.read_csv(file_path)
        df_prov_cat = df.groupby(
            ['categoria', 'provincia'], as_index=False,).size()
        return super().cargar_tabla(df_prov_cat)

