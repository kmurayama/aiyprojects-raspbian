from gpiozero import LED
import time
from time import sleep

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
from gpiozero import PWMOutputDevice

strobe = PWMLED(26)
motor = PWMOutputDevice(4)

strobe.off()

t_end = time.time() + 10
freq = 15
step = 1/freq

while time.time() < t_end:
    motor1.value = 0.5
    strobe.blink(on_time = step, off_time = step)

