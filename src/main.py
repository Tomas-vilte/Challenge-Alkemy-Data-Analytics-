from extractors import museoExtractor, urlExtract
import pandas as pd
from constans import BASE_FILE
from config import (museos,cines,bibliotecas)
from loaders import(rawdata ,cineinsightsloader, rawdata, sizeByCategoryLoader, sizeBySourceLoader, sizeByCatProvLoader)
from logger_base import log
import click

logging = log.getLogger()
extractors_dict = {
    'museo': museoExtractor(museos['name'], museos['url']),
    'cines': urlExtract(cines['name'], cines['url']),
    'bibliotecas': urlExtract(bibliotecas['name'], bibliotecas['url']),
}


def extract_raws(date_str: str) -> str:
    """Ejecutamos extract

    Args:
        date_str (str): Ejecutamos fecha con formato yyyy-mm-dd

    Returns:
        list[str]: Lista de rutas de archivos de datos guardados

    """
    file_paths = dict()
    for name, extractor in extractors_dict.items():
        file_path = extractor.extract(date_str)
        file_paths[name] = file_path

    return file_paths


def unir_df(file_paths: str, out_file_path: str) -> str:
    """Une datos y los almacena en out_file_path_

    Args:
        file_paths (str): Lista de ubicación de datos
        out_file_path (str): Ubicación de destino

    Returns:
        str: Ubicación de destino
    """
    dfs_transformed = list()
    for name, extractor in extractors_dict.items():
        df = pd.read_csv(file_paths[name])
        dft = extractor.transform(df)
        dfs_transformed.append(dft)
        pd.concat(dfs_transformed, axis=0).to_csv(out_file_path)
    return out_file_path

@click.command()
@click.option('--date', help='Fecha de ejecución en formato YYYY-MM-DD')
def ejecutar_pipeline(date: str) -> None:
    """Ejecutar pipeline

    Args:
        date (str): Formato de fecha YYYY-MM-DD
    """

    # Extract
    log.info('Extrayendo')
    file_paths = extract_raws(date)

    # Transform
    merge_path = BASE_FILE / 'merge_df_{date}.csv'
    unir_df(file_paths, merge_path)

    # Load
    log.info('Cargando')
    rawdata().cargar_tabla(merge_path)
    cineinsightsloader().cargar_tabla(file_paths['cines'])
    sizeByCategoryLoader().cargar_tabla(merge_path)
    sizeBySourceLoader().cargar_tabla(file_paths)
    sizeByCatProvLoader().cargar_tabla(merge_path)
    log.info('Termino de cargar los datos')

if __name__ == '__main__':
    ejecutar_pipeline()