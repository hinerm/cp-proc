import sys, threading, subprocess
from multiprocessing.managers import BaseManager
from queue import Queue


queue = Queue()
class QueueManager(BaseManager): pass
QueueManager.register('get_queue', callable=lambda:queue)


def start_server():
    m = QueueManager(address=('', 50000), authkey=b'abracadabra')
    s = m.get_server()
    s.serve_forever()


def exit_on_stdin_close():
    try:
        while sys.stdin.read():
            pass
    except:
        pass


def start():
    exit_poll = threading.Thread(target=exit_on_stdin_close, name="exit-on-stdin")
    exit_poll.daemon = True
    # This daemon thread polling stdin blocks execution of subprocesses
    # But ONLY if running in another process with stdin connected to its parent by PIPE
    exit_poll.start()

    queue_server = threading.Thread(target=start_server, name="queue-server")
    queue_server.daemon = True
    # This daemon thread polling stdin blocks execution of subprocesses
    # But ONLY if running in another process with stdin connected to its parent by PIPE
    queue_server.start()

    subprocess.Popen([sys.executable, "-u", "mproc_child.py"],
            # When creating the subprocess with an open pipe to stdin and
            # subsequently polling that pipe, it blocks further communication
            # between subprocesses
            close_fds=False,)

    m = QueueManager(address=('127.0.0.1', 50000), authkey=b'abracadabra')
    m.connect()
    queue = m.get_queue()
    # Create process 3
    print(f"result: {queue.get()}")


if __name__ == '__main__':
    start()