import multiprocessing as mp
import time
from multiprocessing.managers import BaseManager

def start(queue):
    queue.put("hello")


