import os
import sys
import signal


def sigusr1_handler(signum, frame):
	print(f'Produced: {produced}')
	sys.stdout.flush()


signal.signal(signal.SIGUSR1, sigusr1_handler)

pipe1_0 = os.pipe()
pipe0_2 = os.pipe()
pipe2_0 = os.pipe()

pid1 = os.fork()
if pid1 == 0:
	os.close(pipe1_0[0])
	os.dup2(pipe1_0[1], 1)
	os.execve('/bin/python3', ['/bin/python3', 'producer.py'], os.environ)

pid2 = os.fork()

if pid2 == 0:
	os.close(pipe0_2[1])
	os.close(pipe2_0[0])
	os.dup2(pipe0_2[0], 0)
	os.dup2(pipe2_0[1], 1)
	os.execve('/usr/bin/bc', ['/usr/bin/bc'], os.environ)

os.close(pipe1_0[1])
os.close(pipe0_2[0])
os.close(pipe2_0[1])

produced = 0

while True:
	expression = os.read(pipe1_0[0], 1024).decode('utf-8')

	if not expression:
		break

	os.write(pipe0_2[1], expression.encode('utf-8'))
	result = os.read(pipe2_0[0], 1024).decode('utf-8')
	print(f'{expression.strip()} = {result.strip()}')

	produced += 1
