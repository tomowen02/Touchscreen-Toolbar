import tkinter as tk
import commands
from time import sleep
from threading import Thread
from pynput.mouse import Controller as Mouse_Controller
from functools import partial


running = True
pointer_location = (0, 0)


### Functions ###
def loop():
    while running:
        window.update()

def quit_program():
    global running
    running = False

def make_button(button_text, command, side=tk.TOP):
    button = tk.Button(
        window,
        text = button_text, 
        command = command
    )
    button.pack(
        ipadx = 5,
        ipady = 5,
        side = side,
        fill=tk.X
    )
    
def save_pointer_location():
    mouse = Mouse_Controller()
    global pointer_location
    while running:
        pointer_location = mouse.position
        sleep(1.5)

def command_with_pointer_loc(command):
    command(pointer_location)


### MAIN ###
window = tk.Tk()
window.title("")
window.geometry(f"50x{window.winfo_screenheight()}+0+0")
window.overrideredirect(True)
window.attributes('-topmost',True)

make_button("Snip", partial(command_with_pointer_loc, commands.snip_screen))
make_button("Multi", commands.multi_task)
make_button("Win", commands.win)
make_button("OSK", partial(command_with_pointer_loc, commands.osk))
make_button("Notes", commands.one_note)
make_button("White", commands.whiteboard)

# Temporary solution to padding out the keyboard related buttons
w = tk.Text(window)
w.insert(tk.INSERT, "")
w.pack()

make_button("Shift", commands.hold_shift)
make_button("Copy", commands.copy)
make_button("Paste", commands.paste)
make_button("Del", commands.delete)

make_button("Exit", quit_program, tk.BOTTOM)

Thread(target=save_pointer_location).start()
loop()
