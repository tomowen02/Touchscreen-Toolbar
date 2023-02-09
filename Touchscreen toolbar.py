import tkinter as tk
import commands
from time import localtime, sleep
from threading import Thread
from pynput.mouse import Controller as Mouse_Controller
from functools import partial


running = True
pointer_location = (0, 0)


### Functions ###
def loop():
    while running:
        window.update()
        update_time()
        sleep(0.1)

def quit_program():
    global running
    running = False
    
def minimize_program():
    window.overrideredirect(False)
    window.iconify()
    #sleep(5)
    #maximize_program()

def maximize_program():
    window.deiconify()
    window.geometry(f"50x{window.winfo_screenheight()}+0+0")
    window.overrideredirect(True)
    window.attributes('-topmost',True)

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
        
def update_time():
    time = localtime()
    time_str = f"{time.tm_hour}:{time.tm_min}"
    time_string_var.set(time_str)

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
buffer_0 = tk.Label(window, textvariable=tk.StringVar())
buffer_0.pack()

make_button("Copy", commands.copy)
make_button("Paste", commands.paste)
make_button("Del", commands.delete)

# Padding
buffer_1 = tk.Label(window, textvariable=tk.StringVar())
buffer_1.pack()

#make_button("Shift", commands.hold_shift)
make_button("Full", commands.zones_layout_full)
make_button("Split", commands.zones_layout_split)
make_button("Vert", commands.zones_layout_vert)
make_button("Triple", commands.zones_layout_triple)

# Display time
time_string_var = tk.StringVar()
time_label = tk.Label(window, textvariable=time_string_var)
time_label.pack(side=tk.BOTTOM)

make_button("Exit", quit_program, tk.BOTTOM)
make_button("Min", minimize_program, tk.BOTTOM)
make_button("Restore", maximize_program, tk.BOTTOM)

Thread(target=save_pointer_location).start()
loop()
