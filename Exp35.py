import tkinter as tk
from tkinter import messagebox
import csv
import matplotlib.pyplot as plt
 
root = tk.Tk()
root.title("Student Record Management System")
root.geometry("450x400")
 
records = []
 
tk.Label(root, text="Subject:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
subject_entry = tk.Entry(root)
subject_entry.grid(row=0, column=1)
 
tk.Label(root, text="Marks (out of 100):").grid(row=1, column=0, padx=10, pady=5, sticky="w")
marks_entry = tk.Entry(root)
marks_entry.grid(row=1, column=1)
 
result_box = tk.Listbox(root, width=50)
result_box.grid(row=3, column=0, columnspan=2, pady=10)
 
def calculate_result(marks):
    if marks >= 33:
        return "Pass"
    return "Fail"
 
def add_record():
    subject = subject_entry.get()
    try:
        marks = float(marks_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Enter valid marks")
        return
    status = calculate_result(marks)
    records.append({"Subject": subject, "Marks": marks, "Result": status})
    result_box.insert(tk.END, f"{subject} - {marks} - {status}")
    subject_entry.delete(0, tk.END)
    marks_entry.delete(0, tk.END)
 
def save_to_csv():
    with open("student_records.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["Subject", "Marks", "Result"])
        writer.writeheader()
        writer.writerows(records)
    messagebox.showinfo("Saved", "Records saved to student_records.csv")
 
def show_graph():
    subjects = [r["Subject"] for r in records]
    marks = [r["Marks"] for r in records]
    plt.bar(subjects, marks, color="skyblue")
    plt.title("Student Marks Report")
    plt.xlabel("Subject")
    plt.ylabel("Marks")
    plt.show()
 
tk.Button(root, text="Add Record", command=add_record).grid(row=2, column=0, pady=10)
tk.Button(root, text="Save to CSV", command=save_to_csv).grid(row=4, column=0, pady=5)
tk.Button(root, text="Show Graph", command=show_graph).grid(row=4, column=1, pady=5)
 
root.mainloop()

