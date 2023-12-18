import tkinter as tk
from tkinter import colorchooser

color = colorchooser.askcolor()
window = tk.Tk()
window.title("Demonstration of Place Layout")
window.geometry("900x500")
window.maxsize(900,600)
window.config(bg=color)

tk.Label(text="Name").place(x=15,y=15)
entry1 = tk.Entry().place(x=55, y=15)
button = tk.Button(fg = "orange", bg="purple")

tk.mainloop()
