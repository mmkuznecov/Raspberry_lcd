import time
import RPi.GPIO as GPIO
from glcd12864zw import clearGraphic, loadBMP12864, init

init()

def draw_right():
    clearGraphic()
    loadBMP12864('Right.bmp')
def draw_left():
    clearGraphic()
    loadBMP12864('Left.bmp')
def draw_up():
    clearGraphic()
    loadBMP12864('Up.bmp')
def draw_down():
    clearGraphic()
    loadBMP12864('Down.bmp')


KEY1 = 14 #up-down
KEY2 = 15 #right-left

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

GPIO.setup(KEY1, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(KEY2, GPIO.IN,pull_up_down=GPIO.PUD_UP)

right = True
up = True

while True:

    if GPIO.input(KEY1) == False:
        if up:
            draw_up()
        else:
            draw_down()
        
        up=not(up)
    time.sleep(0.5)

    if GPIO.input(KEY2) == False:
        if right:
            draw_right()
        else:
            draw_left()
        
        right=not(right)
    time.sleep(0.5)
            