import sys, threading, time

from multiprocessing.managers import BaseManager

class QueueManager(BaseManager): pass
QueueManager.register('get_queue')
QueueManager.register('get_lock')

def exit_on_stdin_close():
    print("mproc poll started")
    try:
        while sys.stdin.read():
            pass
    except:
        pass
    print("mproc poll ended")


def start():
    exit_poll = threading.Thread(target=exit_on_stdin_close, name="exit-on-stdin")
    exit_poll.daemon = False
    # This daemon thread polling stdin blocks execution of subprocesses
    # But ONLY if running in another process with stdin connected to its parent by PIPE
    exit_poll.start()

    m = QueueManager(address=('127.0.0.1', 50000), authkey=b'abracadabra')
    m.connect()
    # l = m.get_lock()
    # l.acquire()
    print("got lock")
    queue = m.get_queue()
    queue.put("hello")
    time.sleep(2)
    print("mproc done")
    # l.release()


if __name__ == '__main__':
    start()