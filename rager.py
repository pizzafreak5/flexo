from pews import *

import time
while True:
	d1 = pew1.get_distance()
	d2 = pew2.get_distance()
	d3 = pew3.get_distance()


	print('{}:{}:{}'.format(d1,d2,d3))
	time.sleep(0.5)

