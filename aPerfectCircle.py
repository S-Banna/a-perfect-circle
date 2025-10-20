import math
import time
import pyautogui # somehow bricks the whole thing if not imported?
from pynput import mouse


# use nameCoords.py to get your circle midpoint coords. 
xG = 960 
yG = 538

# magic number, number of points around the circle. 360 works well enough.
p = 360

# initially not in_rotation. a flag to stop multiple circles at once.
in_rotation = False

# a mouse controller
mouseCTRL = mouse.Controller()


def rotateAround(x, y):
    global in_rotation, p, mouseCTRL
    in_rotation = True
    
    # calculate radius. start angle magic courtesy of your favourite AI model
    r = math.hypot(x - xG, y - yG)
    start_angle = math.atan2(y - yG, x - xG)

    # short sleep to allow site to do its thing
    time.sleep(0.3)

    for i in range(p + 1):
        angle = start_angle + 2 * math.pi * i / p
        xA = xG + r * math.cos(angle)
        yA = yG + r * math.sin(angle)
        mouseCTRL.position = (xA, yA)
        time.sleep(0.001)

    time.sleep(0.05)
    in_rotation = False

def on_click(x, y, button, pressed):
    # kill switch
    if pressed and button == mouse.Button.right:
        print("exit")
        listener.stop()
        return False
    
    # execution
    global in_rotation
    if pressed and button == mouse.Button.left and not in_rotation:
        rotateAround(x, y)

with mouse.Listener(on_click=on_click) as listener:
    print("ready. hold down left click to draw, right click to exit.")
    listener.join()