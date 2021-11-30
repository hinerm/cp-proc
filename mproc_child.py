import multiprocessing as mp
import os, time

q = None

def f(q):
    print("mproc_child f pid:", os.getpid())
    # Here is where we block
    q.put("hello")
    time.sleep(2.4)

def start():
    print("mproc_child main pid:", os.getpid())
    ctx = mp.get_context('spawn')
    global q
    q = ctx.Queue()
    p = ctx.Process(target=f, args=(q,))
    p.start()
    print("mproc_child started")
    p.join()
    print("mproc_child joined")
