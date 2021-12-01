import subprocess, time, sys, threading

def start():
    worker = subprocess.Popen([sys.executable, "-u", "server.py"],
            # When creating the subprocess with an open pipe to stdin and
            # subsequently polling that pipe, it blocks further communication
            # between subprocesses
            stdin=subprocess.PIPE,
            close_fds=False,)

    # Create process 2
    worker = subprocess.Popen([sys.executable, "-u", "mproc.py"],
            # When creating the subprocess with an open pipe to stdin and
            # subsequently polling that pipe, it blocks further communication
            # between subprocesses
            stdin=subprocess.PIPE,
            close_fds=False,)
    time.sleep(5)

if __name__ == '__main__':
    start()
