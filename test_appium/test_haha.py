import _thread
import requests
import time, logging

# requests.
logging.basicConfig(level=logging.INFO)


def loop0():
    logging.info('start loop0 at' + time.ctime())
    time.sleep(4)
    logging.info('end loop0 at' + time.ctime())


def loop1():
    logging.info('start loop1 at' + time.ctime())
    time.sleep(2)
    logging.info('end loop1 at' + time.ctime())


def main():
    logging.info('start all at' + time.ctime())
    # loop0()
    # loop1()
    _thread.start_new_thread(loop0, ())
    _thread.start_new_thread(loop1, ())
    time.sleep(6)
    logging.info('end all at' + time.ctime())


if __name__ == '__main__':
    main()
