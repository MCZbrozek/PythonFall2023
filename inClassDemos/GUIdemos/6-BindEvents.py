import tkinter as tk

def callback(event):
    print(event.x, event.y) # Will print to console the x,y of the mouse click

top = tk.Tk()
top.bind("<Button-3>", callback) # <Button-1> refers to the mouse button

tk.mainloop()