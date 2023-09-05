from collections import defaultdict
import csv

from pep_parse.constants import (STATUSES_FIELDNAMES,
                                 STATUSES_FILENAME,
                                 FILE_DIR, BASE_DIR, datetime_now)


class PepParsePipeline:

    def __init__(self):
        self.statuses_quantity = defaultdict(int)

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        status = item['status']
        self.statuses_quantity[status] += 1
        return item

    def close_spider(self, spider):
        self.statuses_quantity['Total']: int = sum(
            self.statuses_quantity.values()
        )
        self.save_to_file()

    def save_to_file(self):
        file_name = (f'{BASE_DIR}/{FILE_DIR}/{STATUSES_FILENAME}'
                     f'_{datetime_now}.csv')

        with open(file_name, 'w', encoding='utf-8') as file:
            status_column, quantity_column = STATUSES_FIELDNAMES
            writer = csv.DictWriter(file, fieldnames=[
                status_column, quantity_column
            ])
            writer.writeheader()
            for status, quantity in self.statuses_quantity.items():
                writer.writerow({status_column: status,
                                 quantity_column: quantity})
