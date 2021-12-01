import os, sys, threading
import multiprocessing as mp


def exit_on_stdin_close():
    print("starting exit on close daemon")
    try:
        while sys.stdin.read():
            pass
    except:
        pass

    print("ending exit on close daemon")


def put_hello(q):
    q.put("hello")


if __name__ == '__main__':
    print("mproc_parent pid:", os.getpid())
    thread = threading.Thread(target=exit_on_stdin_close, name="exit-on-stdin")
    thread.daemon = True
    # This daemon thread polling stdin blocks communication with multiprocessing.queue
    # But ONLY if running in another process with stdin connected to its parent by PIPE
    thread.start()

    ctx = mp.get_context('spawn')
    q = ctx.Queue()
    p = ctx.Process(target=put_hello, args=(q,))
    p.start()

    print(f'mproc_parent pipe result: {q.get()}')
