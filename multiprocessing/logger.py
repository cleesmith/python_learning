import multiprocessing
import logging
import sys

def worker(logger):
    logger.info('\tworker: doing some work')
    sys.stdout.flush()

if __name__ == '__main__':
    multiprocessing.log_to_stderr()
    logger = multiprocessing.get_logger()
    logger.setLevel(logging.DEBUG)
    p = multiprocessing.Process(target=worker, args=(logger,))
    p.start()
    p.join()
