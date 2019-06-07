host='192.168.1.27'
port='5000'

import subprocess
import os
import threading
from concurrent.futures import ThreadPoolExecutor as PoolExecutor
import sys
print(sys.argv)
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
def excute_command(command):
   print(command)
   subprocess.run(command, shell=True)

commands =[]
thread_num = 1000
max_workers = 200
if(len(sys.argv) >2):
   max_workers = int(sys.argv[2])
if(len(sys.argv) >1):
   thread_num = int(sys.argv[1])
for i in range(0, thread_num):
   #print(i)
   command = 'python3 sub.py'
   commands.append(command)
   # x = threading.Thread(target=excute_command, args=(command,))
   # x.start()

with PoolExecutor(max_workers=max_workers) as executor:
    for _ in executor.map(excute_command, commands):
        pass
print("All tasks complete")

