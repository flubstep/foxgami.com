import functools
from sqlalchemy import create_engine


@functools.lru_cache()
def engine():
    return create_engine('postgresql://foxgami:foxgami@localhost/foxgami') 


def query(sql, args=()):
    e = engine()
    result = e.execute(sql, tuple(args))
    return result 
