import multiprocessing as mp
import time
from multiprocessing.managers import BaseManager

def start(i):
    print("helloooooo", i)


if __name__ == '__main__':
    start()
