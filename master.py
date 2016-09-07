import time
from psycopg2 import connect
from pq import PQ
from const import DB_NAME, DB_USER, QUEUE_NAMES, GENERATE_SIZE


from multiprocessing import Process


def handle(data):
    """Does nothing really """
    #print("Value is {0}".format(data['v']))
    if data['v'] > GENERATE_SIZE:
        print("Something wrong v {0} should not be greater than {1}".format(
            data['v'], GENERATE_SIZE))


def process_queue(name, size):
    conn = connect('dbname={0} user={1}'.format(DB_NAME, DB_USER))
    pq = PQ(conn)
    queue = pq[name]
    for job in queue:
        if job is None:
            print("Sleeping...")
            time.sleep(1)
            continue
        if 'v' in job.data.keys() and job.data['v'] >= size:
            print('For Q_NAME {0} got value {1}'.format(name, job.data['v']))
            break


if __name__ == "__main__":
    start_time = time.time()
    procs = []
    end_time = None
    for qn in QUEUE_NAMES:
        p = Process(target=process_queue, args=(qn, GENERATE_SIZE))
        p.start()
        procs.append(p)

    for p in procs:
        p.join()
    end_time = time.time()
    print('Total Time: {0}'.format(end_time-start_time))
