from gpiozero import LED,Button
from time import sleep
from signal import pause

button=Button(20)
red = LED(2)
amber = LED(3)
green = LED(4)


def toggle():
    print('i am here')
    amber.on
    sleep(3)
    green.off
    amber.off
    red.on
    sleep(10)
    green.on

def toGreen():
    green.on
    red.off
    amber.off


button.when_pressed = toggle
button.when_released = toGreen

pause()    
    