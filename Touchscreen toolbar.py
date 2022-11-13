import tkinter as tk
from tkinter import messagebox
import commands

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

make_button("Snip", commands.snip_screen)
make_button("Multi", commands.multi_task)
make_button("Win", commands.win)
make_button("Notes", commands.one_note)
make_button("White", commands.whiteboard)
make_button("Shift", commands.hold_shift)
make_button("Copy", commands.copy)
make_button("Paste", commands.paste)
make_button("Del", commands.delete)

make_button("Exit", exit, tk.BOTTOM)

window.mainloop()