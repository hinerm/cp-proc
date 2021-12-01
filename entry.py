import subprocess, time, sys, threading
import multiprocessing as mp

def start():
    s_worker = subprocess.Popen([sys.executable, "-u", "server.py"],
            # When creating the subprocess with an open pipe to stdin and
            # subsequently polling that pipe, it blocks further communication
            # between subprocesses
            stdin=subprocess.PIPE,
            close_fds=False,)
    t = threading.Thread(args=(s_worker))
    t.start()

    m_worker = subprocess.Popen([sys.executable, "-u", "mproc.py"],
            # When creating the subprocess with an open pipe to stdin and
            # subsequently polling that pipe, it blocks further communication
            # between subprocesses
            stdin=subprocess.PIPE,
            close_fds=False,)
    t = threading.Thread(args=(m_worker))
    t.start()
    time.sleep(5)

if __name__ == '__main__':
    start()
