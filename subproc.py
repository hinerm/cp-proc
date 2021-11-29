import subprocess, os, threading, time

print("subproc pid=", os.getpid())
worker = subprocess.Popen(["python", "multiproc_caller.py"],)
t = threading.Thread(args=(worker))
t.daemon = True
t.start()
print("subproc continuing")
time.sleep(5)
print("subproc complete")
