import tkinter as tk

root = tk.Tk()
tk.Label(root, text="Name:").grid(row=0, column=0)
e_name = tk.Entry(root).grid(row=0, column=1)

tk.Label(root, text="Roll No.:").grid(row=1, column=0)
e_roll = tk.Entry(root).grid(row=1, column=1)

tk.Label(root, text="Course:").grid(row=2, column=0)
e_course = tk.Entry(root).grid(row=2, column=1)

tk.Label(root, text="Gender:").grid(row=3, column=0)
gen = tk.StringVar(value="M")
tk.Radiobutton(root, text="M", variable=gen, value="M").grid(row=3, column=1)
tk.Radiobutton(root, text="F", variable=gen, value="F").grid(row=3, column=2)

tk.Button(root, text="Submit", command=lambda: print(f"Submitted successfully!")).grid(row=4, column=1)
root.mainloop()