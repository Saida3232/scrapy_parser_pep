import csv
import datetime as db

from pep_parse.constants import (DATETIME_FORMAT, EXPECTED_STATUS,
                                 RESULTS_DIR_NAME)


def status_pep(current_status):
    for short_status, status in EXPECTED_STATUS.items():
        if current_status in status:
            return short_status


def add_count(results):
    statuses = [('Статус', "Количество")]
    for i in EXPECTED_STATUS.keys():
        statuses.append((i, results.count(i)))
    statuses.append(('Total', len(results)))
    return statuses


def file_output(results, direcrion):
    results_dir = direcrion / RESULTS_DIR_NAME
    results_dir.mkdir(exist_ok=True)

    now = db.datetime.now()
    new_now = now.strftime(DATETIME_FORMAT)
    file_name = f'status_summary_{new_now}.csv'
    file_path = results_dir / file_name

    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, dialect='unix', delimiter=' ', quotechar='|')
        writer.writerows(results)
