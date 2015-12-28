from foxgami.rdb import r, conn

r.table('users').delete().run(conn)
r.tables('sessions').delete().run(conn)