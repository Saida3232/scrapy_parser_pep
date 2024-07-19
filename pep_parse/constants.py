PEP_PAGE = 'http://peps.python.org/'

EXPECTED_STATUS = {
    'A': ('Active', 'Accepted'),
    'D': ('Deferred',),
    'F': ('Final',),
    'P': ('Provisional',),
    'R': ('Rejected',),
    'S': ('Superseded',),
    'W': ('Withdrawn',),
    '': ('Draft', 'Active'),
    'April Fool!': ('April Fool!')
}

RESULTS_DIR_NAME = 'results'
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'

FILE_FORMAT = 'csv'
PEP_FILE_NAME = f'pep_%(time)s.{FILE_FORMAT}'
