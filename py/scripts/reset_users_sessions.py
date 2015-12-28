from foxgami.rdb import r, conn

r.table('users').delete().run(conn)
r.table('sessions').delete().run(conn)