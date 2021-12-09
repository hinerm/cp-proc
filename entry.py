import subprocess, time, sys, threading
from multiprocessing.managers import BaseManager
import multiprocessing as mp

class QueueManager(BaseManager): pass
QueueManager.register('get_queue', callable=lambda:queue)


def server_running(timeout=0.25):
    import socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        return s.connect_ex(('localhost', 50000)) == 0


def start():
    s_worker = subprocess.Popen([sys.executable, "-u", "server.py"],
            # When creating the subprocess with an open pipe to stdin and
            # subsequently polling that pipe, it blocks further communication
            # between subprocesses
            stdin=subprocess.PIPE,
            close_fds=False,)
    t = threading.Thread(args=(s_worker))
    t.start()

    while not server_running():
        pass

    m_worker = subprocess.Popen([sys.executable, "-u", "mproc.py"],
            # When creating the subprocess with an open pipe to stdin and
            # subsequently polling that pipe, it blocks further communication
            # between subprocesses
            stdin=subprocess.PIPE,
            close_fds=False,)
    t = threading.Thread(args=(m_worker))
    t.start()
    time.sleep(3)

if __name__ == '__main__':
    start()
