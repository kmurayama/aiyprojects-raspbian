from gpiozero import LED
import time
from time import sleep

strobe = LED(26)

strobe.off()

t_end = time.time() + 10
freq = 15
step = 1/freq

while time.time() < t_end:
    sleep(step)
    strobe.on()
    sleep(step)
    strobe.off()

