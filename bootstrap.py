from const import DB_NAME, DB_USER

from psycopg2 import connect
from pq import PQ

conn = connect('dbname={0} user={1}'.format(DB_NAME, DB_USER))
pq = PQ(conn)

pq.create()
