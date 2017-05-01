import motor_controller as mc
import time

speed = 255

lr_mod =float(250)/float(255)

lspeed = 252

time.sleep(20)

mc.move_right_forward(speed)
mc.move_left_forward(lspeed)

time.sleep(12)

mc.move_stop()




