import smbus

bus = smbus.SMBus(2)

for x in range(0, 50000):
	data1 = bus.read_byte_data(0x29, 0)
	data2 = bus.read_byte_data(0x29, 1)
	data3 = bus.read_byte_data(0x29, 2)
	data4 = bus.read_byte_data(0x29, 3)
	print('{}:{}:{}:{}'.format(data1,data2,data3,data4))