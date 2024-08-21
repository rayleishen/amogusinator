#this_is_where_we_will_make_our_class_for_all_the_tasks
import mouse
from time import sleep

screen_x = 2560
screen_y = 1440

def upload_data():
    x = screen_x * 0.5
    y = screen_y * 0.61
    
    mouse.move(x,y)
    mouse.click(button="left")
    
    return

def unlock_manifolds():
    return
    
def swipe_card():
    x1 = screen_x * 0.4
    y1 = screen_y * 0.757
    
    mouse.move(x1,y1)
    mouse.click(button="left")
    
    sleep(0.5)
    
    x2 = screen_x * 0.27
    x3 = screen_x * 0.73
    y2 = screen_y * 0.42
    
    mouse.drag(x2,y2, x3, y2, absolute=True, duration=0.6)
    mouse.click(button="left")
    
    return

def submit_scan():
    return

def start_reactor():
    return

def stabilize_steering():
    x = screen_x * 0.5
    y = screen_y * 0.5
    
    mouse.move(x,y)
    mouse.click(button="left")
    
    return

def prime_shields():
    return

def inspect_sample():
    return

def fuel_engines():
    x = screen_x * 0.7625
    y = screen_y * 0.82
    
    mouse.move(x,y)
    
    mouse.press(button="left")
    sleep(4)
    mouse.release(button="left")
    
    return


def fix_wiring():
    return

def empty_garbage(): #empty_chute
    return

def divert_power():
    return

def clear_asteroids():
    return

def clean_vent():
    return

def clean_o2_filter():
    return

def chart_course():
    return

def calibrate_distributor():
    return

def align_engine_output():
    x = screen_x * 0.65
    y = screen_y * 0.5
    
    mouse.move(x,y)
    mouse.click(button="left")
    
    return

while True:
    if mouse.is_pressed(button='right'):
        swipe_card()