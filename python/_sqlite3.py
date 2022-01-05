import sqlite3

from _configs import database


def _dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


conn = sqlite3.connect(database)
conn.row_factory = _dict_factory
