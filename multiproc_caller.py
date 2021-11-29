import multiproc as mup

if __name__ == '__main__':
    mup.start()
    print(f'Queue result: {mup.q.get()}')
