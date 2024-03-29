from pynput.keyboard import Key, Controller as Keyboard_Controller
from pynput.mouse import Controller as Mouse_Controller
from os import system
from time import sleep
from shiftPopupmsg import shiftPopupmsg
from tempfile import gettempdir

mouse = Mouse_Controller()
keyboard = Keyboard_Controller()

### Functions to help with other commands ###

def get_cursor_pos(filename="pointer_loc.txt"):
    path = gettempdir() + f"\pointer_loc.txt"
    with open(path, 'r') as f:
        pos_as_str = f.read()
        pos_as_tuple = eval(pos_as_str)
        return pos_as_tuple

def fancy_zones_shortcut_hold(layout_number):
    layout_number = str(int(layout_number))
    keyboard.press(Key.ctrl_l)
    keyboard.press(Key.cmd)
    keyboard.press(Key.alt_l)
    keyboard.press(layout_number)
    keyboard.release(Key.ctrl_l)
    keyboard.release(Key.cmd)
    keyboard.release(Key.alt_l)
    keyboard.release(layout_number)
    hold_shift()

def release_special_keys():
    keyboard.release(Key.ctrl_l)
    keyboard.release(Key.cmd)
    keyboard.release(Key.alt_l)
    keyboard.release(Key.shift)
    keyboard.release(Key.tab)


### Command functions ###

def snip_screen(pos_before_click):
    keyboard.press(Key.cmd)
    keyboard.press(Key.shift)
    keyboard.press("s")
    keyboard.release(Key.cmd)
    keyboard.release(Key.shift)
    keyboard.release("s")
    mouse.position = pos_before_click
    
def hold_shift():
    shiftPopupmsg("The shift key is currently being held down. Press OK to release")

def multi_task():
    keyboard.press(Key.cmd)
    keyboard.press(Key.tab)
    keyboard.release(Key.cmd)
    keyboard.release(Key.tab)
    
def win():
    keyboard.press(Key.cmd)
    keyboard.release(Key.cmd)

def one_note():
    system("start onenote:")

def whiteboard():
    system("start ms-whiteboard-cmd:")

def copy():
    keyboard.press(Key.alt_l)
    keyboard.press(Key.tab)
    sleep(0.15)
    keyboard.release(Key.tab)
    keyboard.release(Key.alt_l)
    sleep(0.2)
    keyboard.press(Key.ctrl_l)
    keyboard.press("c")
    keyboard.release(Key.ctrl_l)
    keyboard.release("c")
    
def paste():
    keyboard.press(Key.alt_l)
    keyboard.press(Key.tab)
    sleep(0.15)
    keyboard.release(Key.tab)
    keyboard.release(Key.alt_l)
    sleep(0.2)
    keyboard.press(Key.ctrl_l)
    keyboard.press("v")
    keyboard.release(Key.ctrl_l)
    keyboard.release("v")
    
def delete():
    keyboard.press(Key.alt_l)
    keyboard.press(Key.tab)
    sleep(0.15)
    keyboard.release(Key.tab)
    keyboard.release(Key.alt_l)
    sleep(0.2)
    keyboard.press(Key.delete)
    keyboard.release(Key.delete)
    
def osk(pos_before_click):
    keyboard.press(Key.cmd)
    keyboard.press(Key.ctrl_l)
    keyboard.press("o")
    keyboard.release(Key.cmd)
    keyboard.release(Key.ctrl_l)
    keyboard.release("o")
    mouse.position = pos_before_click
    
def zones_layout_vert():
    fancy_zones_shortcut_hold(0)
    
def zones_layout_full():
    fancy_zones_shortcut_hold(2)
    
def zones_layout_split():
    fancy_zones_shortcut_hold(1)
    
def zones_layout_triple():
    fancy_zones_shortcut_hold(3)