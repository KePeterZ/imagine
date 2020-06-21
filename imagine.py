from ev3dev2.motor import MoveSteering, MoveTank, LargeMotor, Motor
from ev3dev2.sensor.lego import ColorSensor, GyroSensor
import time

# TODO:
#   Write faster GyroReset function into GyroClass
#   Write better position function into LargeMotorClass

class myRobot:
  # Initialize the Class 
  def __init__(self, motorL=None, motorR=None, motorM=None, gyroPort=None, colorL=None, colorR=None, colorM=None):
    if motorL: self.motorL = LargeMotor(motorL)
    if motorR: self.motorR = LargeMotor(motorR)
    if motorM: self.motorM = Motor(motorM)
    if gyroPort: 
      self.gyro = GyroSensor(gyroPort)
      self.gyro.mode = 'GYRO-CAL'
      time.sleep(0.2)
      self.gyro.mode = 'GYRO-ANG'
    if colorL: self.colorL = ColorSensor(colorL)
    if colorR: self.colorR = ColorSensor(colorR)
    if colorM: self.colorM = ColorSensor(colorM)
    if motorL and motorR: 
      self.drive = MoveSteering(motorL, motorR)
      self.move = MoveTank(motorL, motorR)

  def forward(self, speed, distance, useRots=True, correction=2, useGyro=True, way=None): 
    initialGyro = way if way else self.gyro.angle
    if useRots:
      initialMotor = abs((self.motorL.position/360 + self.motorR.position/360)/2) # Get the average of the 2 motor values
      while abs((self.motorL.position/360 + self.motorR.position/360)/2) < initialMotor+distance: 
        self.drive.on(initialGyro - self.gyro.angle*correction, speed)
        print("%f : %i" % (abs((self.motorL.position/360 + self.motorR.position/360)/2), initialMotor+distance))
        print("gyro: %i" % self.gyro.angle)
    elif not useRots:
      initialTime = time.time()
      while time.time()-initialTime < distance: 
        self.drive.on(initialGyro - self.gyro.angle*correction, speed)
        print("%f : %i" % (time.time()-initialTime, distance))
        print("gyro: %i" % self.gyro.angle)

  def stop(self, brake=False): 
    self.drive.stop(brake=brake)

  def turn(self, way, speed, linear=False, leeway=1, debug=False, minSpeed=5):
    if type(way)==type(1.1):
      way = int(self.gyro.angle+way)
    leewayList = range(way-leeway, way+leeway+1)
    if linear:
      while self.gyro.angle not in leewayList:
        if debug: print(self.gyro.angle)
        lin = abs(way/self.gyro.angle)
        print(lin)
        self.move.on(speed*lin+minSpeed, speed*-1*lin+minSpeed)
    elif not linear:
      while self.gyro.angle not in leewayList:
        if debug: print(self.gyro.angle)
        self.move.on(speed, speed*-1)

  def nodrift(self):
    self.gyro.mode = 'GYRO-CAL'
    time.sleep(0.2)
    self.gyro.mode = 'GYRO-ANG'

k = myRobot("outB", "outC", gyroPort="in4")
for i in range(4):
  k.forward(-50, 2, correction=1)
  k.turn(90.0, -5, debug=True)
k.stop()