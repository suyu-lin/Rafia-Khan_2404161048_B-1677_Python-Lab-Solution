import tkinter as tk
root = tk.Tk()
root.title("Basic Tkinter GUI")
root.geometry("450x300")
root.iconbitmap("idea.png")
tk.Label(root, text="Welcome to Tkinter GUI", font=("Times New Roman", 14)).pack(pady=50)
root.mainloop()
