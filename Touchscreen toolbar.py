import tkinter as tk
import commands
from time import sleep
from threading import Thread
from pynput.mouse import Controller as Mouse_Controller
from tempfile import gettempdir

running = True

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
    while running:
        path = gettempdir() + f"\pointer_loc.txt"
        with open(path, 'w+') as f:
            pos = mouse.position
            f.write(str(pos))
        sleep(1.25)


### MAIN ###
window = tk.Tk()
window.title("")
window.geometry(f"50x{window.winfo_screenheight()}+0+0")
window.overrideredirect(True)
window.attributes('-topmost',True)

make_button("Snip", commands.snip_screen)
make_button("Multi", commands.multi_task)
make_button("Win", commands.win)
make_button("OSK", commands.osk)
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
