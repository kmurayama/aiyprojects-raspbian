from giozero import Button
from subprocess import check_all
from signal import pause

def shutdown():
    check_call(['sudo', 'poweroff'])

shutdown_btn = Button(17, hold_time = 2)
shutdown_btn.when_held = shutdown

pause()
