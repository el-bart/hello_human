#!/usr/bin/env python
import time
import Servo

ld = Servo.LineDriver("/dev/ttyUSB0")
p  = Servo.Position(ld, 'l', 'f')

p.set(0,0)
time.sleep(1)

p.set(0, -0.5)
time.sleep(1)

p.set(-0.5, -0.5)
time.sleep(1)

p.set(-0.0, +0.5)
time.sleep(1)

p.set(+0.5, +0.5)
time.sleep(1)

p.set(0,0)
