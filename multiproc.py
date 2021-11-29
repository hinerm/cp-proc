import multiprocessing as mp
import os, time

def f():
    print("multiproc f pid:", os.getpid())
    time.sleep(2.4)

def start():
    print("multiproc main pid:", os.getpid())
    p = mp.Process(target=f)
    p.start()
    print("multiproc started")
    p.join()
    print("multiproc joined")
