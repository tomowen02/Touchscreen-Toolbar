from pynput.keyboard import Key, Controller
import tkinter as tk
from tkinter import messagebox
from os import system
from time import sleep

### Commands ###
def exit():
    window.quit()

def snip_screen():
    keyboard = Controller()
    keyboard.press(Key.cmd)
    keyboard.press(Key.shift)
    keyboard.press("s")
    keyboard.release(Key.cmd)
    keyboard.release(Key.shift)
    keyboard.release("s")
    
def hold_shift():
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
    

### Program functions ###
def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = tk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.attributes('-topmost',True)
    popup.mainloop()
    
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


### MAIN ###
window = tk.Tk()
window.title("")
window.geometry(f"50x{window.winfo_screenheight()}+0+0")
window.overrideredirect(True)
window.attributes('-topmost',True)

make_button("Snip", snip_screen)
make_button("Multi", multi_task)
make_button("Win", win)
make_button("Notes", one_note)
make_button("White", whiteboard)
make_button("Shift", hold_shift)
make_button("Exit", exit, tk.BOTTOM)

window.mainloop()