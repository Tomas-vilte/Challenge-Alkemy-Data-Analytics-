import logging as log
import os

try:
    os.mkdir('logs')
except FileExistsError:
    pass

log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('logs/ETL_process.log'),
                    log.StreamHandler()
                ])
