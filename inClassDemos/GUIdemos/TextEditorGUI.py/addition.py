import tkinter as tk
import tkinter.scrolledtext as st

# Event Methods
def add():
    num1 = float(num1_entry.get())
    num2 = float(num2_entry.get())
    result = num1 + num2
    result_scrolled_text.delete('1.0', 'end')
    result_scrolled_text.insert('insert', f"The sum of {num1} + {num2} = {result} \n")

# Create Window
top = tk.Tk()
top.geometry("350x200")

# Add controls
tk.Label(text = "Num 1").place(x=10, y=10)
num1_entry = tk.Entry()
num1_entry.place(x=110, y=10)
tk.Label(text="Num 2").place(x=10,y=40)
num2_entry = tk.Entry()
num2_entry.place(x=110, y=40)
tk.Button(text="Add Numbers", command=add, bg = "blue").place(x=100, y=70)
result_scrolled_text = st.ScrolledText()
result_scrolled_text.place(x = 10, y = 100, width = 225, height = 50)
# Run Mainloop
tk.mainloop()