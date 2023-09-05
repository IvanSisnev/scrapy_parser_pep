"""
Pipelines проекта.
"""

import logging
from collections import defaultdict
import csv

from pep_parse.constants import (STATUSES_FIELDNAMES,
                                 STATUSES_FILENAME,
                                 FILE_DIR, BASE_DIR, datetime_now)


class PepParsePipeline:
    """
    Забирает из items статус, подсчитывает их количество и сохраняет в файл.
    """
    def __init__(self):
        self.statuses_quantity = defaultdict(int)

    def open_spider(self, spider):
        pass

    # забираю статусы и подсчитываю их количество
    def process_item(self, item, spider):
        status: str = item['status']
        self.statuses_quantity[status] += 1
        return item

    # подсчитываю общее количество статусов
    def close_spider(self, spider):
        self.statuses_quantity['Total']: int = sum(
            self.statuses_quantity.values()
        )
        logging.info('Данные переданы на запись в файл.')
        self.save_to_file()

    # записываю в csv файл
    def save_to_file(self):
        file_name: str = (f'{BASE_DIR}/{FILE_DIR}/{STATUSES_FILENAME}'
                          f'_{datetime_now}.csv')
        try:
            with open(file_name, 'w', encoding='utf-8') as file:
                column1, column2 = STATUSES_FIELDNAMES
                writer = csv.DictWriter(file, fieldnames=[column1, column2])
                writer.writeheader()
                for status, quantity in self.statuses_quantity.items():
                    writer.writerow({column1: status, column2: quantity})
            logging.info(f'Данные записаны в файл {file_name}.')
        except IOError:
            error_msg: str = 'Не удалось записать данные в файл.'
            logging.error(msg=error_msg, stack_info=True)
