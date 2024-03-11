import time
from rzctl import RZCONTROL, MOUSE_CLICK, KEYBOARD_INPUT_TYPE
dll_path = "./rzctl_lib/rzctl.dll"
    
rzctl = RZCONTROL(dll_path)

# cfg
# количество коробок с патронами
boxes = 10
boxes_all = boxes
# Количество патронов в одной обойме
ammo = 30
# Общее количество патронов
ammo_all = 150
ammo_current = ammo
ammo_all_fix = ammo_all + ammo

if not rzctl.init():
    print("Failed to initialize rzctl")
def reload():
    unscope()
    global ammo, ammo_all, ammo_current, boxes
    rzctl.keyboard_input(19, KEYBOARD_INPUT_TYPE.KEYBOARD_DOWN)
    rzctl.keyboard_input(19, KEYBOARD_INPUT_TYPE.KEYBOARD_UP)
    time.sleep(3)
    ammo_all-=ammo
    ammo_current = ammo
def kill():
    unscope()
    global ammo, ammo_all, ammo_current, boxes
    time.sleep(1)
    rzctl.keyboard_input(5, KEYBOARD_INPUT_TYPE.KEYBOARD_DOWN)
    time.sleep(1/10)
    rzctl.keyboard_input(5, KEYBOARD_INPUT_TYPE.KEYBOARD_UP)
    time.sleep(1.5)
    move(0,2500)
    rzctl.mouse_click(MOUSE_CLICK.RIGHT_DOWN)
    time.sleep(1/100)
    rzctl.mouse_click(MOUSE_CLICK.RIGHT_UP)
    time.sleep(5)
    rzctl.keyboard_input(57, KEYBOARD_INPUT_TYPE.KEYBOARD_DOWN)
    rzctl.keyboard_input(57, KEYBOARD_INPUT_TYPE.KEYBOARD_UP)
    time.sleep(1)
    rzctl.keyboard_input(28, KEYBOARD_INPUT_TYPE.KEYBOARD_DOWN)
    rzctl.keyboard_input(28, KEYBOARD_INPUT_TYPE.KEYBOARD_UP)
    boxes=boxes_all
    ammo_current=ammo
    ammo_all=ammo_all_fix-ammo
    rzctl.keyboard_input(2, KEYBOARD_INPUT_TYPE.KEYBOARD_DOWN)
    rzctl.keyboard_input(2, KEYBOARD_INPUT_TYPE.KEYBOARD_UP)
    time.sleep(1)

def tap():
    global ammo, ammo_all, ammo_current, boxes
    rzctl.mouse_click(MOUSE_CLICK.LEFT_DOWN)
    time.sleep(1/100)
    rzctl.mouse_click(MOUSE_CLICK.LEFT_UP)
    time.sleep(5/100)
    ammo_current -=1
def clickL():
    rzctl.mouse_click(MOUSE_CLICK.LEFT_DOWN)
    time.sleep(1/100)
    rzctl.mouse_click(MOUSE_CLICK.LEFT_UP)
def clickR():
    rzctl.mouse_click(MOUSE_CLICK.RIGHT_DOWN)
    time.sleep(1/10)
    rzctl.mouse_click(MOUSE_CLICK.RIGHT_UP)
    time.sleep(1/4)
def scope():
    pass
def unscope():
    rzctl.mouse_click(MOUSE_CLICK.RIGHT_UP)
    time.sleep(7/1000)


def use_box():
    unscope()
    global ammo, ammo_all, ammo_current, boxes, boxes_all
    time.sleep(1/2)
    rzctl.keyboard_input(6, KEYBOARD_INPUT_TYPE.KEYBOARD_DOWN)
    rzctl.keyboard_input(6, KEYBOARD_INPUT_TYPE.KEYBOARD_UP)
    time.sleep(1)
    rzctl.mouse_click(MOUSE_CLICK.RIGHT_DOWN)
    time.sleep(1/100)
    rzctl.mouse_click(MOUSE_CLICK.RIGHT_UP)
    time.sleep(2)
    rzctl.keyboard_input(2, KEYBOARD_INPUT_TYPE.KEYBOARD_DOWN)
    rzctl.keyboard_input(2, KEYBOARD_INPUT_TYPE.KEYBOARD_UP)
    boxes -= 1
    ammo_all=ammo_all_fix
    reload()
    time.sleep(.2)


def check_reload():
    global ammo, ammo_all, ammo_current, boxes
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nammo_all = "+str(ammo_all)+"\nammo_current = " + str(ammo_current) + "\nboxes = " + str(boxes))
    if ammo_all<=0 and ammo_current==0 and boxes==0:
        kill()
    elif ammo_all<=0 and ammo_current==0:
        use_box()
    elif ammo_current==0:
        reload()
def move(x,y):
    rzctl.mouse_move(x, y, True)
def main():
    time.sleep(5)
    while True:
        move(-800,-800)
        time.sleep(1/1000)
        move(600,50)
        time.sleep(1/1000)
        clickL()
        time.sleep(1/10)
        move(-800,-800)
        time.sleep(1/1000)
        move(500,300)
        time.sleep(1/10)
        clickL()
        time.sleep(44)
        rzctl.keyboard_input(5, KEYBOARD_INPUT_TYPE.KEYBOARD_DOWN)
        time.sleep(1/10)
        rzctl.keyboard_input(5, KEYBOARD_INPUT_TYPE.KEYBOARD_UP)
        time.sleep(1/1000)
        move(0,5000)
        time.sleep(2)
        clickR()
        time.sleep(1/2)
        rzctl.keyboard_input(6, KEYBOARD_INPUT_TYPE.KEYBOARD_DOWN)
        time.sleep(1/10)
        rzctl.keyboard_input(6, KEYBOARD_INPUT_TYPE.KEYBOARD_UP)
        rzctl.mouse_click(MOUSE_CLICK.RIGHT_DOWN)
        time.sleep(12)
        rzctl.mouse_click(MOUSE_CLICK.RIGHT_UP)
        rzctl.keyboard_input(5, KEYBOARD_INPUT_TYPE.KEYBOARD_DOWN)
        time.sleep(1/10)
        rzctl.keyboard_input(5, KEYBOARD_INPUT_TYPE.KEYBOARD_UP)
        time.sleep(1/4)
        clickR()
        time.sleep(2)
        rzctl.keyboard_input(1, KEYBOARD_INPUT_TYPE.KEYBOARD_DOWN)
        time.sleep(1/5)
        rzctl.keyboard_input(1, KEYBOARD_INPUT_TYPE.KEYBOARD_UP)
        time.sleep(1)
        move(-110,-125)
        time.sleep(1/5)
        clickL()
        time.sleep(1/5)
        move(-75,75)
        time.sleep(1/5)
        clickL()
        time.sleep(5)
        move(-800,-800)
        time.sleep(5)
        rzctl.keyboard_input(57, KEYBOARD_INPUT_TYPE.KEYBOARD_DOWN)
        time.sleep(1/10)
        rzctl.keyboard_input(57, KEYBOARD_INPUT_TYPE.KEYBOARD_UP)
        time.sleep(2)
if __name__ == '__main__':
    main()