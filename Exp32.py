import tkinter as tk
 
root = tk.Tk()
root.title("Radiobutton and Checkbutton Demo")
root.geometry("500x300")
 
tk.Label(root, text="Select Gender:").pack(pady=5)
gender = tk.StringVar(value="Male")
tk.Radiobutton(root, text="Male", variable=gender, value="Male").pack()
tk.Radiobutton(root, text="Female", variable=gender, value="Female").pack()
 
tk.Label(root, text="Select Hobbies:").pack(pady=5)
hobby1 = tk.BooleanVar()
hobby2 = tk.BooleanVar()
tk.Checkbutton(root, text="Reading", variable=hobby1).pack()
tk.Checkbutton(root, text="Coding", variable=hobby2).pack()
 
def show_choices():
    result = f"Gender: {gender.get()}\n"
    result += f"Reading: {hobby1.get()}, Coding: {hobby2.get()}"
    print(result)
 
tk.Button(root, text="Show Choices", command=show_choices).pack(pady=15)
 
root.mainloop()

