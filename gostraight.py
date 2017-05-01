import motor_controller as mc
import time

speed = 255

lr_mod = 0.80

rspeed = int(speed * lr_mod)

time.sleep(20)

mc.move_right_forward(rspeed)
mc.move_left_forward(speed)

time.sleep(12)

mc.move_stop()




