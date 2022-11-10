import tkinter as tk

def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = tk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="Okay", command = popup.quit) # quit() just bypasses the main loop
    B1.pack()
    popup.attributes('-topmost',True)
    popup.mainloop()
    popup.destroy()