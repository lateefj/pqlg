import os

CONSUMER_POOL_SIZE = 3
DB_NAME = 'pqlg_test'
DB_USER = os.environ['USER']
NUMBER_QUEUES = 25
QUEUE_NAMES = ['load_{0}'.format(x) for x in range(NUMBER_QUEUES)]
GENERATE_SIZE = 10000
#GENERATE_SIZE = 1000000
