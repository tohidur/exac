import random
import signal
import threading
import time


exit_event = threading.Event()


def bg_thread():
    for i in range(1, 30):
        print(f'{i} for 30 iterations...')
        time.sleep(random.random())  # Do some work

        if exit_event.is_set():
            break

    print(f'{i} iterations complete before exiting.')


def signal_handler(signum, frame):
    exit_event.set()


signal.signal(signal.SIGINT, signal_handler)
th = threading.Thread(target=bg_thread)
th.start()
th.join()

