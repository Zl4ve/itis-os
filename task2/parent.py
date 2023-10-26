import os
import sys
import random

def fork():
	child_res = os.fork()
	if (child_res > 0):
		print('Parent[{0}]: I ran children process with PID {1}.'.format(os.getpid(), child_res))
	elif (child_res == 0):
		os.execve(sys.executable, [sys.executable, 'child.py', str(random.randint(5,10))], os.environ)

if (len(sys.argv) < 2):
	print("Enter number of child processes")
	os._exit(1)

count_str = sys.argv[1]

if (not count_str.isdigit()):
	print("Number of child processes must be integer")
	os._exit(1)

child_count = int(count_str)

for i in range(child_count):
	fork()

while (child_count > 0):
	child_pid, child_res = os.wait()

	child_res = os.waitstatus_to_exitcode(child_res)

	print('Parent[{0}]: Child with PID {1} terminated. Exit Status {2}.'.format(os.getpid(), child_pid, child_res))
	
	if (child_res != 0):
		fork()
	else:
		child_count -= 1
		
