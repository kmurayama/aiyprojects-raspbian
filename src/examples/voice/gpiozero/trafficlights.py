from gpiozero import LED
from time import sleep

red = LED(26)
amber = LED(13)
green = LED(5)

green.on()
amber.off()
red.off()

while True:
    sleep(5)
    green.off()
    amber.on()
    sleep(2)
    amber.off()
    red.on()
    sleep(5)
    green.on()
    red.off()
    
