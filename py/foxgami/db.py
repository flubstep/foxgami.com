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
    elif sql.strip().lower().startswith('insert'):
        return result.inserted_primary_key


def query_single(sql, args=()):
    rows = list(query(sql, args))
    if len(rows) >= 1:
        return rows[0]
    else:
        return None


'''
create table sessions (
    user_id bigint not null,
    token character(32) not null,
    primary key (token)
);

create table users (
    user_id serial,
    name character(255),
    email character(255),
    password_hash character(255),
    profile_image_url character(255),
    primary key (user_id)
);
'''