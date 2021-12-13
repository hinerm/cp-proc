import subprocess, time, sys, threading
from multiprocessing.managers import BaseManager, Server
import multiprocessing as mp
import server

class QueueManager(BaseManager): pass
QueueManager.register('get_queue')


def server_running(timeout=0.25):
    import socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        return s.connect_ex(('localhost', 50000)) == 0


def start():
    ctx = mp.get_context('spawn')
    p = ctx.Process(target=server.start)
    p.daemon = False
    p.start()

    while not server_running():
        pass

    for i in range(1,4):
        m_worker = subprocess.Popen([sys.executable, "-u", "mproc.py"],
                # When creating the subprocess with an open pipe to stdin and
                # subsequently polling that pipe, it blocks further communication
                # between subprocesses
                stdin=subprocess.PIPE,
                close_fds=False,)
        t = threading.Thread(args=(m_worker))
        t.start()
    time.sleep(8)

if __name__ == '__main__':
    start()
