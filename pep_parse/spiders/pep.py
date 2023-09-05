# Паук pep.

# todo оптимизация
# todo перехват ошибок
# todo логирование https://docs.scrapy.org/en/latest/topics/logging.html
#  #logging-from-spiders
# todo readme
from urllib.parse import urljoin

import scrapy

from pep_parse.constants import PEP_DOMAIN, PEP_URL
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = [PEP_DOMAIN]
    start_urls = [PEP_URL]

    def parse(self, response, **kwargs):
        # забираю таблицу
        pep_table = response.xpath('//*[@id="numerical-index"]').css('tbody')
        # забираю все ряды с PEP из таблицы
        all_peps: list = pep_table.css('tr')

        # прохожу по каждому ряду
        for a_pep in all_peps:
            # забираю ccылку на страницу PEP
            pep_link: str = a_pep.css('a').attrib['href']
            pep_url: str = urljoin(PEP_URL, pep_link)
            # передаю ссылку дальше
            yield response.follow(pep_url, callback=self.parse_pep)

    def parse_pep(self, response):
        # разбираю заголовок страницы, извлекаю номер и название
        page_title: list = response.css(
            '#pep-content > h1::text'
        ).get().split('–')
        pep_number: str = page_title[0].split()[-1]
        pep_title: str = page_title[-1].strip()
        # забираю статус
        pep_status: str = response.css(
            'dt:contains("Status") + dd'
        ).css('abbr::text').get()

        data: dict[str:str] = {
            'number': pep_number,
            'name': pep_title,
            'status': pep_status
        }

        yield PepParseItem(data)
