"""
Паук pep.
"""

# todo логирование
import logging
from urllib.parse import urljoin
import re

import scrapy
from tqdm import tqdm

from pep_parse.constants import PEP_DOMAIN, PEP_URL, PATTERN
from pep_parse.items import PepParseItem
from pep_parse.utils import scrape


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = [PEP_DOMAIN]
    start_urls = [PEP_URL]

    def parse(self, response, **kwargs):
        """
        Забирает информацию с PEP_URL.
        """
        self.log('Парсер запущен', level=logging.INFO)
        # забираю раздел с таблицей и саму таблицу
        num_table = scrape(response, xpath='//*[@id="numerical-index"]')
        pep_table = scrape(num_table, css='tbody')
        # забираю все ряды с PEP из таблицы
        all_peps: list = scrape(pep_table, css='tr')

        # прохожу по каждому ряду
        self.log('Парсер собрал ссылки на PEP', level=logging.INFO)
        for a_pep in tqdm(all_peps):
            # забираю ccылку на страницу PEP
            pep_a_tag = scrape(a_pep, css='a')
            pep_href: str = scrape(pep_a_tag, attrib='href')
            pep_url: str = urljoin(PEP_URL, pep_href)
            # передаю ссылку дальше
            yield response.follow(pep_url, callback=self.parse_pep)

    def parse_pep(self, response):
        """
        Забирает информацию со страницы каждого PEP.
        """
        # разбираю заголовок страницы, извлекаю номер и название
        page_title: str = scrape(response, css='#pep-content > h1::text').get()
        match = re.match(PATTERN, page_title)
        if match:
            pep_number: str = match.group('number')
            pep_title: str = match.group('name')
        else:
            # warning_message: str = ('Не удалось получить номер или название '
            #                         f'PEP по адресу: {response.url}.')
            pep_number, pep_title = 'Неизвестно', 'Неизвестно'

        # забираю статус
        pep_dd_tag = scrape(response, css='dt:contains("Status") + dd')
        pep_status: str = scrape(pep_dd_tag, css='abbr::text').get()

        data: dict[str:str] = {
            'number': pep_number,
            'name': pep_title,
            'status': pep_status
        }

        yield PepParseItem(data)
