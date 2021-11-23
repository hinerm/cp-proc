import subprocess, os

print("subproc pid=", os.getpid())
subprocess.run(["python", "multiproc.py"],)
print("subproc continuing")
