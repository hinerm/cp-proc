import subprocess, threading, time, sys

def start():
    # Create process 2
    worker = subprocess.Popen([sys.executable, "-u", "mproc.py"],
            # When creating the subprocess with an open pipe to stdin and
            # subsequently polling that pipe, it blocks further communication
            # between subprocesses
            stdin=subprocess.PIPE,
            close_fds=False,)
    t = threading.Thread(args=(worker))
    t.start()
    time.sleep(4)

if __name__ == '__main__':
    start()
