activation_bind="c"
import winsound
import keyboard
import time, getpixelcolor
import statistics
from rzctl import RZCONTROL, MOUSE_CLICK, KEYBOARD_INPUT_TYPE
from numba import jit
dll_path = "./rzctl_lib/rzctl.dll"
white=(255,255,255)
fire=(255,40,40)
rzctl = RZCONTROL(dll_path)
@jit(nopython=True)
def calculate_diff(initial_color, r, g, b):
    diff = [abs(component - initial_color[i]) for i, component in enumerate((r, g, b))]
    return diff
def tap():
    rzctl.mouse_click(MOUSE_CLICK.LEFT_DOWN)
    time.sleep(1/100)
    rzctl.mouse_click(MOUSE_CLICK.LEFT_UP)
    time.sleep(15/100)
scoped=False
threshold=20
initial_color = None
while True:
    if keyboard.is_pressed(activation_bind):
        if not scoped:
            rzctl.mouse_click(MOUSE_CLICK.RIGHT_DOWN)
            time.sleep(.3)
            scoped=True
        r, g, b = getpixelcolor.pixel(962, 542)
        if initial_color == None:
            initial_color = (r, g, b)
        else:
            diff = calculate_diff(initial_color, r, g, b)
            if statistics.mean(diff) > threshold:
                tap()
                time.sleep(1/4)
                initial_color = None
    else:
        if scoped:
            rzctl.mouse_click(MOUSE_CLICK.RIGHT_UP)
            scoped=False
        initial_color = None
        time.sleep(.0001)