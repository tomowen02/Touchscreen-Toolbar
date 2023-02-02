from time import sleep
import tkinter as tk
from pynput.keyboard import Key, Controller as Keyboard_Controller

running = True
def stop():
    global running
    running = False

def shiftPopupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = tk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="Okay", command = stop) # quit() just bypasses the main loop
    B1.pack()
    popup.attributes('-topmost',True)
    
    global running
    while running:
        Keyboard_Controller().press(Key.shift)
        print("test")
        sleep(0.5)
        popup.update()
    Keyboard_Controller().release(Key.shift)
    running = True
    popup.destroy()