# Tutorial

If you had 2 Large motors, and one gyroscope, you would start your program like this:
```python
from imagine import myRobot
r = myRobot(motorL="outB", motorR="outC", gyroPort="in4") # Provided that these are the ports
```

If you wanted to move forward using the gyro measured in rotations, you could write it as simply as this: 
```python
r.forward(speed=100, distance=2, useRots=True) # Parameter names not necessary
```

If you wanted it to have a correction multiplier of 3x, just pass it as a parameter.
```python
r.forward(..., correction=3)
```

Let's say you want to stop your robot. Just call the stop function, with brake as a parameter. 
```python
r.stop(brake=True) # True if you want to stop the robot in place, False if you just want to cut the power to the motors.
```

You want to turn using the Gyro. Just use the turn function:
```python
r.turn(way=90, speed=5) # If way is float, the desired facing direction will be the current heading +/- way
```

The Gyro is drifting. Calling the nodrift function will fix that in 0.2 seconds. (if the robot is standstill) 
```python
r.nodrift() # Can pass t (time for calibration) as argument, default is 0.2s
```

You want to write your own built-in functions. Just use ```self``` and the default properties for the sensors, and you're good to go. For example:
```python
def rotate(self, rots, speed): # Turns completely, for a rotation of the LEFT motor
  initMotors = self.motorL.position/360
  while self.motorL.position/360 < initMotors+rots:
    self.motorL.on(speed) # Set Left motor to on
    self.motorR.on(-speed) # Set Right motor to negative speed
  self.stop() # Stops all motors.
```
This is just a rough example, but using the `self` declarations, you can literally program any function, and calling it will look great. Calling the above function from a brand new file is as simple as this: 
```python
from imagine import myRobot
r = myRobot("outB", "outC", gyroPort="in1")

r.rotate(1, 40) # Rotate completely 
```

See? If you wanted to write the above function using raw ev3dev2, this would be the same: 
```python
from ev3dev2.motor import LargeMotor
from ev3dev2.sensors.lego import GyroSensor

leftMotor = LargeMotor("outB")
rightMotor = LargeMotor("outC")
gyroSensor = GyroSensor("in1")

def rotate(rots, speed): # Turns completely, for a rotation of the LEFT motor
  initMotors = leftMotor.position/360
  while leftMotor.position/360 < initMotors+rots:
    leftMotor.on(speed) # Set Left motor to on
    rightMotor.on(-speed) # Set Right motor to negative speed
  leftMotor.stop() # Stops left motor
  rightMotor.stop() # Stops right motor

rotate(1, 40)
```

If you have any questions, feel free to message me on Discord at KePeterZ#4679 and I'll be sure to help you out ASAP!

# KePeterZ, 2020