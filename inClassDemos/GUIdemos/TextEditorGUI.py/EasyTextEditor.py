import tkinter as tk
import tkinter.scrolledtext as st

# Define event methods at the top
def load():
    filename= filename_entry.get()
    f = open(filename, "r")
    text = f.read()
    contents_scrolled_text.delete("1.0", "end")
    contents_scrolled_text.insert("insert", text + "\n")
    f.close()

def save():
    filename = filename_entry.get()
    f = open(filename, "w") 
    text = contents_scrolled_text.get('1.0', 'end')
    f.write(text)
    f.close()



# Create the main window
top = tk.Tk()
top.title("Easy Text Editor")
contents_scrolled_text = st.ScrolledText()
contents_scrolled_text.pack(side="bottom", expand=True, fill="both")
filename_entry = tk.Entry()
filename_entry.pack(side="left", expand=True, fill="x")
tk.Button(text="Open", command=load, bg="lightblue").pack(side="left")
tk.Button(text="Save", command=save, bg="lightgreen").pack(side="left")

# Add Controls


# Run Mainloop
tk.mainloop()