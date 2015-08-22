import functools
from sqlalchemy import create_engine


@functools.lru_cache()
def engine():
    return create_engine('postgresql://foxgami:foxgami@localhost/foxgami') 


def query(sql, args=()):
    e = engine()
    result = e.execute(sql, tuple(args))
    if result.returns_rows:
        return list(result)


def query_single(sql, args=()):
    rows = list(query(sql, args))
    if len(rows) >= 1:
        return rows[0]
    else:
        return None
