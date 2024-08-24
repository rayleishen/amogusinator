#this_is_where_we_will_make_our_class_for_all_the_tasks
import mouse
import time
from time import sleep
from PIL import ImageGrab

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
    #mouse.click(button="left")
    
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
    
    px = ImageGrab.grab().load()
    
    x0 = screen_x*0.293
    x1 = screen_x*0.702
    
    y0 = screen_y*0.249
    y1 = screen_y*0.426
    y2 = screen_y*0.596
    y3 = screen_y*0.769
    
    y_values = [y0, y1, y2, y3]
    
    colour_left0 = px[x0, y0] #topleft
    colour_left1 = px[x0, y1]
    colour_left2 = px[x0, y2]
    colour_left3 = px[x0, y3]
    
    colour_right0 = px[x1, y0] #topright
    colour_right1 = px[x1, y1]
    colour_right2 = px[x1, y2]
    colour_right3 = px[x1, y3]
    
    left_colors = [colour_left0, colour_left1, colour_left2, colour_left3]
    right_colors = [colour_right0, colour_right1, colour_right2, colour_right3]

    # Find matching pairs
    matching_pairs = []

    for left_index, left_color in enumerate(left_colors):
        for right_index, right_color in enumerate(right_colors):
            if left_color == right_color:
                matching_pairs.append((left_index, right_index, y_values[left_index], y_values[right_index]))

    print(matching_pairs)
    
    for i in range(4):
        mouse.drag(x0, matching_pairs[i][2], x1, matching_pairs[i][3], absolute=True, duration=0.14)
        sleep(0.02)

    return

def empty_garbage(): #empty_chute
    return

def divert_power():
    return

def clear_asteroids():

    boundingLeftX = int(screen_x*0.3203125) # 820 in 1440p
    boundingRightX = int(screen_x*0.6796875) # 1740 in 1440p
    boundingTopY = int(screen_y*0.17361111111) # 250 in 1440p
    boundingBottomY = int(screen_y*0.82638888888) # 1190 in 1440p
    asteroidsFound = 0
    foundAllAsteroids = False
    allowSearch = True
    targetColour1 = (24,56,41)
    targetColour2 = (26,60,42)
    targetColour3 = (31,72,41)

    # print("starting")
    startTime = time.time()
    while(foundAllAsteroids == False):
        if asteroidsFound >= 20:
            foundAllAsteroids = True
            break
        px = ImageGrab.grab().load()
        print(asteroidsFound)


        for x in range(boundingLeftX, boundingRightX):
            if allowSearch == True:
                for y in range(boundingTopY, boundingBottomY):
                    if allowSearch == True:
                        currentColour = px[x,y]
                        # print(currentColour)
                        if (currentColour == targetColour1 or currentColour == targetColour2 or currentColour == targetColour3):
                            mouse.move(x,y)
                            mouse.click(button="left")
                            asteroidsFound += 1
                            allowSearch = False
                    else:
                        break
            else:
                break

        allowSearch = True
        sleep(0.6)
        endTime = time.time()
        if ((endTime - startTime) > 30):
            break
                    

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
        clear_asteroids()
        break