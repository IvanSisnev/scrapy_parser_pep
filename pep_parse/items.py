# Items проекта.

import scrapy


class PepParseItem(scrapy.Item):
    """
    Items паука pep: номер PEP, его название и статус.
    """
    number = scrapy.Field()
    name = scrapy.Field()
    status = scrapy.Field()
