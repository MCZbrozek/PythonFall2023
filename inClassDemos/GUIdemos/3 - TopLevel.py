import tkinter as tk

tk.Label(text="I'm the first window!!").pack()

second = tk.Toplevel() #Instantiate a second window
tk.Label(second,text="I'm in the second window!!!").pack()

tk.mainloop()