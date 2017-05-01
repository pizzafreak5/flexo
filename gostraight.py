import motor_controller as mc
import time

time.sleep(20)

mc.move_right_forward(255)
mc.move_left_forward(255)

time.sleep(8)

mc.move_stop()

time.sleep(4)

mc.move_right_forward(255)
mc.move_left_backward(255)

time.sleep(4)

mc.move_right_backward(255)
mc.move_left_backward(255)

time.sleep(4)

mc.move_stop()




