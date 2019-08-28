
from os.path import (
    join as join_path,
    dirname
)


def relative_path(*parts):
    return join_path(dirname(__file__), *parts)


NERUS = relative_path('data', 'nerus.tar.gz')