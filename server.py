from multiprocessing.managers import BaseManager
import multiprocessing as mp
import threading, sys


ctx = mp.get_context('spawn')
queue = ctx.Queue()
class QueueManager(BaseManager): pass
QueueManager.register('get_queue', callable=lambda:queue)

def exit_on_stdin_close():
    print("server poll started")
    try:
        while sys.stdin.read():
            pass
    except:
        pass
    print("server poll ended")

def start_server():
    m = QueueManager(address=('', 50000), authkey=b'abracadabra')
    s = m.get_server()
    s.serve_forever()

def start():
    queue_server = threading.Thread(target=start_server, name="queue-server")
    queue_server.daemon = True
    queue_server.start()

    exit_poll = threading.Thread(target=exit_on_stdin_close, name="exit-on-stdin")
    exit_poll.daemon = True
    # This daemon thread polling stdin blocks execution of subprocesses
    # But ONLY if running in another process with stdin connected to its parent by PIPE
    exit_poll.start()

    m = QueueManager(address=('127.0.0.1', 50000), authkey=b'abracadabra')
    m.connect()
    queue = m.get_queue()
    print(f"result: {queue.get()}")

if __name__ == '__main__':
    start()