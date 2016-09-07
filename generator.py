
import time
from uuid import uuid4
from random import randint

from psycopg2 import connect
from pq import PQ
from const import DB_NAME, DB_USER, GENERATE_SIZE, QUEUE_NAMES

from multiprocessing import Process




def add_jobs(name, size):
    conn = connect('dbname={0} user={1}'.format(DB_NAME, DB_USER))
    q_con = PQ(conn)
    queue = q_con[name]
    for i in range(size+1):
        queue.put({'v': i, 'ids': [uuid4().hex for x in range(randint(1, 10))]})
    return size


if __name__ == "__main__":
    start_time = time.time()
    procs = []
    for qn in QUEUE_NAMES:
        p = Process(target=add_jobs, args=(qn, GENERATE_SIZE))
        p.start()
        procs.append(p)

    for p in procs:
        p.join()
    end_time = time.time()
    print('Total Time: {0}'.format(end_time-start_time))
