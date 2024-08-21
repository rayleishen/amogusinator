import mouse
from time import sleep

while True:
    if mouse.is_pressed(button='right'):
        print(mouse.get_position())
        sleep(1)
        
screen_x = 2560
screen_y = 1440