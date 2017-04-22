import smbus
from vl6180x import VL6180X

sensor = VL6180X(debug = True)

sensor.default_settings()

for x in range (0, 10000):
	data = sensor.get_ambient_light(20)
	print(data)
