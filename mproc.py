import multiprocessing as mp
import os, time, sys, threading

def exit_on_stdin_close():
    print("starting exit on close daemon")
    try:
        while sys.stdin.read():
            pass
    except:
        pass

    print("ending exit on close daemon")

def f(q):
    with open("C:\\users\\hiner\\code\\cellprofiler\\cp-procs\\test.txt", 'w') as outfile:
        outfile.write("hi")
    print("mproc_child f pid:", os.getpid())
    # Here is where we block
    q.put("hello")
    time.sleep(2.4)

def start():
    print("mproc_child main pid:", os.getpid())
    thread = threading.Thread(target=exit_on_stdin_close, name="exit-on-stdin")
    thread.daemon = True
    # This daemon thread polling stdin blocks communication with multiprocessing.queue
    # But ONLY if running in another process with stdin connected to its parent by PIPE
    thread.start()

    ctx = mp.get_context('spawn')

    q = ctx.Queue()
    p = ctx.Process(target=f, args=(q,))

    p.start()
    print(f"mproc_child started: {p}")
    p.join()
    print("mproc_child joined")
    print(f'mproc_child pipe result: {q.get()}')

if __name__ == '__main__':
    start()