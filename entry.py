import subprocess, os, threading, time, sys

def start():
    print("subproc pid=", os.getpid())
    worker = subprocess.Popen([sys.executable, "-u", "mproc_parent.py"],
            # When creating the subprocess with an open pipe to stdin and
            # subsequently polling that pipe, it blocks further communication
            # between subprocesses
            stdin=subprocess.PIPE,
            close_fds=False,)
    t = threading.Thread(args=(worker))
    t.start()
    print("subproc continuing")
    time.sleep(5)
    print("subproc complete")

if __name__ == '__main__':
    start()
