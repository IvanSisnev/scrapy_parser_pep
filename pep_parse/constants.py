"""
Константы и переменные проекта.
"""

from pathlib import Path
from typing import Final
import datetime

# путь до верхней директории проекта
BASE_DIR: Final[Path] = Path(__file__).parent.parent

# url адрес с PEP
PEP_URL: Final[str] = 'https://peps.python.org/'

# домен с PEP
PEP_DOMAIN: Final[str] = 'peps.python.org'

# имя сводного файла статусов PEP
STATUSES_FILENAME: Final[str] = 'status_summary'

# названия полей в сводном файле статусов PEP
STATUSES_FIELDNAMES: Final[tuple[str, str]] = ('Статус', 'Количество')

# формат даты и времени для сохранения файлов и записей в логах
DATETIME_FORMAT: Final[str] = '%Y-%m-%d_%H-%M-%S'

# название директории для сохранения файлов с результатами
FILE_DIR: Final[str] = 'results'

# переменная с датой и временем в данный момент
datetime_now = datetime.datetime.now().strftime(DATETIME_FORMAT)

# формат логов
LOG_FORMAT: Final[str] = '%(asctime)s - [%(levelname)s] - %(message)s'

# паттерн для парсинга заголовков страниц PEP
PATTERN: Final[str] = '^PEP\s(?P<number>\d+)\s\–\s(?P<name>.+)$'
