import tkinter as tk
 
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x150")
 
tk.Label(root, text="Number 1:").grid(row=0, column=0, padx=5, pady=5)
num1 = tk.Entry(root)
num1.grid(row=0, column=1)
 
tk.Label(root, text="Number 2:").grid(row=1, column=0, padx=5, pady=5)
num2 = tk.Entry(root)
num2.grid(row=1, column=1)
 
result = tk.Label(root, text="Result: ")
result.grid(row=3, column=0, columnspan=2)
 
def calculate(op):
    try:
        n1 = float(num1.get())
        n2 = float(num2.get())
        if op == "+":
            res = n1 + n2
        elif op == "-":
            res = n1 - n2
        elif op == "*":
            res = n1 * n2
        elif op == "/":
            res = n1 / n2 if n2 != 0 else "Error"
        result.config(text=f"Result: {res}")
    except ValueError:
        result.config(text="Result: Invalid Input")
 
frame = tk.Frame(root)
frame.grid(row=2, column=0, columnspan=2)
tk.Button(frame, text="+", command=lambda: calculate("+")).pack(side="right")
tk.Button(frame, text="-", command=lambda: calculate("-")).pack(side="right")
tk.Button(frame, text="*", command=lambda: calculate("*")).pack(side="right")
tk.Button(frame, text="/", command=lambda: calculate("/")).pack(side="right")
 
root.mainloop()
