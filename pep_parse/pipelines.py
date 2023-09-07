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
        self.statuses_quantities = defaultdict(int)

    def open_spider(self, spider):
        """
        Pass.
        :param spider: паук
        :return: None
        """
        pass

    def process_item(self, item, spider):
        """
        Забирает статусы и подсчитывает их количество.
        :param item: объект Item
        :param spider: паук
        :return: объект Item
        """
        status: str = item['status']
        self.statuses_quantities[status] += 1
        return item

    def close_spider(self, spider):
        """
        Подсчитывает общее количество статусов и передает данные на запись в
        файл.
        :param spider: паук
        :return: None
        """
        self.statuses_quantities['Total']: int = sum(
            self.statuses_quantities.values()
        )
        logging.info('Данные переданы на запись в файл.')
        self.save_to_file()

    def save_to_file(self):
        """
        Записывает данные в файл.
        :return: None
        """
        file_name: str = (f'{BASE_DIR}/{FILE_DIR}/{STATUSES_FILENAME}'
                          f'_{datetime_now}.csv')
        try:
            with open(file_name, 'w', encoding='utf-8') as file:
                column1, column2 = STATUSES_FIELDNAMES
                writer = csv.DictWriter(file, fieldnames=[column1, column2])
                writer.writeheader()
                writer.writerows([
                    {column1: status, column2: quantity}
                    for status, quantity in self.statuses_quantities.items()
                ])
            logging.info(f'Данные записаны в файл {file_name}.')

        except IOError:
            error_msg: str = 'Не удалось записать данные в файл.'
            logging.error(msg=error_msg, stack_info=True)
