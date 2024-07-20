from pep_parse.constants import FILE_FORMAT, PEP_FILE_NAME, RESULTS_DIR_NAME

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

FEEDS = {
    f'{RESULTS_DIR_NAME}/{PEP_FILE_NAME}': {
        'format': FILE_FORMAT,
        'fields': ['number', 'name', 'status']
    },
}


ALLOWED_DOMAINS = ['peps.python.org']
START_URLS = ['https://peps.python.org/']
PEP_SPIDER_NAME = 'pep'
