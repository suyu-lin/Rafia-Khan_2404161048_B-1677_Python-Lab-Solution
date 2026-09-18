import tkinter as tk
from tkinter import messagebox
 
root = tk.Tk()
root.title("Simple Form")
root.geometry("350x200")
 
tk.Label(root, text="Enter your Name:").pack(pady=15)
entry = tk.Entry(root, width=30)
entry.pack()
 
def show():
    name = entry.get()
    messagebox.showinfo("User Input", f"Hello, {name}!")
 
tk.Button(root, text="Submit", command=show).pack(pady=15)
 
root.mainloop()

