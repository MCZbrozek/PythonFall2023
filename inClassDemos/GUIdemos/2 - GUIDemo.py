import tkinter as tk

# Step 3 - write your event functions
def clicked():
    print('I was clicked')


# Step 1 - Create a window
top = tk.Tk() # Instantiating a window

# Step 2 - add Controls
button = tk.Button(fg='blue', bg='green', text = "Click me!", command = clicked).pack() 
# Instantiating a button


tk.mainloop() #main event loop listening for events