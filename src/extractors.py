from constans import BASE_FILE
from datetime import datetime
import requests
from logger_base import log
import pandas as pd


logging = log.getLogger()

class urlExtract:
    file_path_crib = (
        '{category}/{year}-{month:02d}/{category}-{day:02d}-{month:02d}-{year}.csv'
    )

    def __init__(self, name, url) -> None:
        self.name = name
        self.url = url
    
    def extract(self, date_str: str ) -> str:
        """Extrae datos de la URL, los almacena en el file_path y devuelve un dataframe transformado

        Args:
            date_str (str): Cadena de fecha con formato %Y-%m-%d_

        Returns:
            str: Ubicación de la ruta csv transformada
        """
        log.info(f'Extrayendo: {self.name}')
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        file_path = self.file_path_crib.format(
            category=self.name, year=date.year, month=date.month, day=date.day
        )
        m_path = BASE_FILE / file_path
        m_path.parent.mkdir(parents=True, exist_ok=True)
        print(file_path)

        r = requests.get(self.url)
        r.encoding = 'utf-8'

        log.info(f'Archivo guardado en {m_path}')
        with open(m_path, 'w') as f_out:
            f_out.write(r.text)

        return m_path

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """Transforma datos sin procesar y los devuelve en un pd.DataFrame

        Args:
            df (pd.DataFrame): DataFrame a transformado
        
        Returns:
            pd.DataFrame: Transformado DataFrame
        """

        renamed_columns= {
            'Cod_Loc': 'cod_localidad',
            'IdProvincia': 'id_provincia',
            'IdDepartamento': 'id_departamento',
            'Provincia': 'provincia',
            'Categoría': 'categoria',
            'direccion': 'domicilio',
            'CP': 'codigo_postal',
            'Localidad': 'localidad',
            'Nombre': 'nombre',
            'Teléfono': 'numero_telefono',
            'Mail': 'mail',
            'Web': 'web',
        }
        df = df.rename(columns = renamed_columns)

        campos = ['cod_localidad','id_provincia','id_departamento','categoria','provincia','localidad','nombre','codigo_postal','numero_telefono','mail','web']

        df_museos = df[campos]
        return df_museos


class museoExtractor(urlExtract):
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """Transforma los datos sin procesar y los devuelve en un DataFrame


        Args:
            df (pd.DataFrame): DataFrame a transformado
        
        Returns:
            pd.DataFrame: Transformado DataFrame
        """

        renamed_columns_museos = {
            'Cod_Loc': 'cod_localidad',
            'IdProvincia': 'id_provincia',
            'IdDepartamento': 'id_departamento',
            'direccion': 'domicilio',
            'CP': 'codigo_postal',
            'telefono': 'numero_telefono',
            'Mail': 'mail',
            'Web': 'web',
            }

        df = df.rename(columns = renamed_columns_museos)

        campos = ['cod_localidad','id_provincia','id_departamento','domicilio','categoria','provincia','localidad','nombre','codigo_postal','numero_telefono','mail','web']

        return df[campos]