"""
Установки фреймворка.
"""

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {'pep_parse.pipelines.PepParsePipeline': 300, }

FEEDS = {'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}

LOG_FILE = 'logs/pep_logs.log'
LOG_FILE_APPEND = True
LOG_LEVEL = 'INFO'
LOG_STDOUT = True
