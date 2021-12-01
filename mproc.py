import multiprocessing as mp
from os import close
import time, sys, threading, subprocess

def exit_on_stdin_close():
    try:
        while sys.stdin.read():
            pass
    except:
        pass


def put_hello(q):
    # We never reach this line if exit_poll.start() is uncommented
    q.put("hello")
    time.sleep(2.4)


def start():
    exit_poll = threading.Thread(target=exit_on_stdin_close, name="exit-on-stdin")
    exit_poll.daemon = True
    # This daemon thread polling stdin blocks execution of subprocesses
    # But ONLY if running in another process with stdin connected to its parent by PIPE
    exit_poll.start()

    ctx = mp.get_context('spawn')

    q = ctx.Queue()
    p = ctx.Process(target=put_hello, args=(q,))

    # Create process 3
    p.start()
    print(f"result: {q.get()}")
    p.join()


if __name__ == '__main__':
    start()