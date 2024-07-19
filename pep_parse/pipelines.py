from pathlib import Path

from pep_parse.utils import add_count, status_pep, file_output

BASE_DIR = Path(__file__).parent.parent


class PepParsePipeline:
    def open_spider(self, spider):
        self.results = []

    def process_item(self, item, spider):
        short_status = status_pep(item['status'])
        self.results.append(short_status)
        return item

    def close_spider(self, spider):
        pep_results = add_count(self.results)
        file_output(pep_results, BASE_DIR)
