import tkinter as tk
import commands
from time import sleep
import threading
from pynput.mouse import Controller as Mouse_Controller

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
    
def loop():
    while True:
        window.update()
    
def save_pointer_location():
    mouse = Mouse_Controller()
    while True:
        with open("pointer_loc.txt", 'w+') as f:
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

make_button("Exit", exit, tk.BOTTOM)

threading.Thread(target=save_pointer_location).start()
loop()