import random
import os
import time

operations = ['+', '-', '*' , '/']
n = random.randint(120, 180)

for i in range(n):
	x = random.randint(1, 9)
	o = random.choice(operations)
	y = random.randint(1, 9)
	print(str(x) + ' ' + o + ' ' + str(y), flush=True)
	time.sleep(1)
