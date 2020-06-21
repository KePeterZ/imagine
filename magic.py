from ev3dev2.sensor import Sensor
from ev3dev2.sensor.lego import GyroSensor
import time

def m(cmd):
  a = time.time()
  print(cmd)
  exec(cmd)
  print(time.time()-a)

def calibrate(gyro):
  gyro.mode = 'GYRO-CAL'
  time.sleep(0.2)
  gyro.mode = 'GYRO-ANG'

g = GyroSensor("in4")
for i in range(100):
  print("Before: %i" % g.value())

m("calibrate(g)")

for i in range(100):
  print("After: %i" % g.value())