import sys, threading, time
import mproc_child as mpc

def exit_on_stdin_close():
    print("mproc poll started")
    try:
        while sys.stdin.read():
            pass
    except:
        pass
    print("mproc poll ended")


def start():
    exit_poll = threading.Thread(target=exit_on_stdin_close, name="exit-on-stdin")
    exit_poll.daemon = False
    # This daemon thread polling stdin blocks execution of subprocesses
    # But ONLY if running in another process with stdin connected to its parent by PIPE
    exit_poll.start()

    import multiprocessing as mp
    ctx = mp.get_context('spawn')
    with ctx.Pool(5) as pool:
        pool.map(mpc.start, [1, 2, 3])
    print("mproc done")

if __name__ == '__main__':
    start()
