import multiprocessing as mp
import os, time

q = None

def f(q):
    print("multiproc f pid:", os.getpid())
    q.put("hello")
    time.sleep(2.4)

def start():
    print("multiproc main pid:", os.getpid())
    global q
    q = mp.Queue()
    p = mp.Process(target=f, args=(q,))
    p.start()
    print("multiproc started")
    p.join()
    print("multiproc joined")
