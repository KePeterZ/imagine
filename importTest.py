from ev3dev2.motor import MoveSteering, MoveTank, LargeMotor, Motor
from ev3dev2.sensor.lego import ColorSensor, GyroSensor

motorR = LargeMotor("outB")
motorL = LargeMotor("outC")
motorM = Motor("outD")

colorL = ColorSensor("in2")
colorR = ColorSensor("in3")
colorM = ColorSensor("in4")

gyro = GyroSensor("in1")