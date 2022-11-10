from pynput.keyboard import Key, Controller
from os import system
from time import sleep
from popupmsg import popupmsg

def snip_screen():
    keyboard = Controller()
    keyboard.press(Key.cmd)
    keyboard.press(Key.shift)
    keyboard.press("s")
    keyboard.release(Key.cmd)
    keyboard.release(Key.shift)
    keyboard.release("s")
    
def hold_shift():
    popupmsg("The shift key is about to be held down virtually")
    keyboard = Controller()
    keyboard.press(Key.shift)
    sleep(5)
    keyboard.release(Key.shift)
    popupmsg("DONE!")

def multi_task():
    keyboard = Controller()
    keyboard.press(Key.cmd)
    keyboard.press(Key.tab)
    keyboard.release(Key.cmd)
    keyboard.release(Key.tab)
    
def win():
    keyboard = Controller()
    keyboard.press(Key.cmd)
    keyboard.release(Key.cmd)

def one_note():
    system("start onenote:")

def whiteboard():
    system("start ms-whiteboard-cmd:")