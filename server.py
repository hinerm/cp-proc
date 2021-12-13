from multiprocessing.managers import SyncManager
import threading, socket, sys, time
from queue import Queue


queue = Queue()
lock = threading.Lock()
class QueueManager(SyncManager): pass
QueueManager.register('get_queue', callable=lambda:queue)
QueueManager.register('get_lock', callable=lambda:lock)


def exit_on_stdin_close():
    print("server poll started")
    try:
        while sys.stdin.read():
            pass
    except:
        pass
    print("server poll ended")


def server_running(timeout=0.25):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        return s.connect_ex(('localhost', 50000)) == 0


def start_server():
    print("starting server")
    m = QueueManager(address=('', 50000), authkey=b'abracadabra')
    s = m.get_server()
    s.serve_forever()
    print("server ended")


def start():

    queue_server = threading.Thread(target=start_server, name="queue-server")
    queue_server.daemon = True
    queue_server.start()

    while not server_running():
        pass

    m = QueueManager(address=('127.0.0.1', 50000), authkey=b'abracadabra')
    m.connect()

    queue = m.get_queue()
    for i in range(1,4):
        print(f"result: {queue.get()}")

    time.sleep(2)

if __name__ == '__main__':
    start()
