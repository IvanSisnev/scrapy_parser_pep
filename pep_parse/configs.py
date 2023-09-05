"""
Конфигарутор проекта.
"""
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

from pep_parse.constants import BASE_DIR, LOG_FORMAT, DATETIME_FORMAT

def configure_logging():
    """
    Конфигуратор логирования.
    """
    # создаю директорию для логов
    log_dir: Path = Path.joinpath(BASE_DIR, 'logs')
    Path(log_dir).mkdir(exist_ok=True)
    # создаю путь для сохранения файла в директорию
    log_file: Path = Path.joinpath(log_dir, 'parser.log')

    rotating_handler = RotatingFileHandler(
        log_file, maxBytes=10 ** 6, backupCount=5
    )
    logging.basicConfig(
        datefmt=DATETIME_FORMAT,
        format=LOG_FORMAT,
        level=logging.INFO,
        handlers=(rotating_handler, logging.StreamHandler())
    )
