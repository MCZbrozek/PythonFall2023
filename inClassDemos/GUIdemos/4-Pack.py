import tkinter as tk

for i in range(3):
    tk.Button(text=i).pack(side='top')
for i in range(3):
    tk.Button(text=i).pack(side='left')

for i in range(3):
    tk.Button(text=i).pack(side='right')
for i in range(3):
    tk.Button(text=i).pack(side='bottom')

tk.mainloop()