# imagine.py, the FLL focused Python library

Like a lot of teams last year, I was really happy when they announced that we could use any type of software. Since my preference is text based coding, my first choice was Python. The problem was, all the libraries required me to define *every* single piece of hardware individually. That made the code look bad. Then I thought to myself: what if it wasn't that way?

## The Problem

I wanted to create a Python Library, or rather yet, a class that made my code easier to write, and much, *much* cleaner. If I didn't use my library, this is what the first 10 or so lines of our runfiles would look like: 

```python
from ev3dev2.motor import MoveSteering, MoveTank, LargeMotor, Motor
from ev3dev2.sensor.lego import ColorSensor, GyroSensor

motorR = LargeMotor("outB")
motorL = LargeMotor("outC")
motorM = Motor("outD")

colorL = ColorSensor("in2")
colorR = ColorSensor("in3")
colorM = ColorSensor("in4")

gyro = GyroSensor("in1")
```
And even then, when writing functions, I would have to access these in a way less than elegant.

## Then came imagine.

My first goal was clean code. The above mentioned code could be written down in imagine as this:  
```python
from imagine import myRobot
k = myRobot(motorL, motorR, motorM, gyroPort, colorL, colorR, colorM)
```
And you don't need to define every one of them! If, let's say, you don't want to use any color sensors, you just leave them out of the definition line.

## Second reason: code efficiency.

Since imagine supports micropython, and micropython supports cross-compiling, why not take use of it? Imagine comes pre-compiled, as a .mpy file, which makes it about the same speed as using the ev3dev2 libraries directly.

## The best part: BUILT-IN Gyro Drift Fix!

That's right! The robot class comes with a built-in function, that fixes gyro drift basically instantly *(0.2! seconds)*.

## But why should I use it?

Because if you should know anything about Python classes, it's that they make your life a lot easier long-term. Since the code is open-source, you're free to write your own functions in the imagine.py file. All of the declarations in def __init__ are well commented and easy to understand. This makes it a no-brainer if you want to use multiple run-files, or make individual files smaller. 

## I'm sold! Do you have any documentation or tutorials?

I'm currently working on writing a readthedocs, and will update this as soon as it's done. In the meanwhile, a star on this repo would be greatly appreciated!

## I have some optimizations for the built-in functions / want to opensource my own ones here. Can I do that?

Sure, just send a Pull request and  I'll review it ASAP.

## Credits:
- the ev3dev system: https://www.ev3dev.org/
- the ev3dev2 library: https://github.com/ev3dev/ev3dev-lang-python
- micropython: https://micropython.org/

# KePeterZ, 2020