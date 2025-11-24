import tkinter as tk
from tkinter import messagebox

def calculate_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def calculate():
    try:
        num_subjects = int(num_subjects_entry.get())
        if num_subjects <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Enter a valid positive integer for number of subjects.")
        return
    
    marks = []
    for i in range(num_subjects):
        try:
            mark = float(marks_entries[i].get())
            if mark < 0 or mark > 100:
                raise ValueError
            marks.append(mark)
        except ValueError:
            messagebox.showerror("Invalid Input", f"Enter valid marks between 0 and 100 for subject {i+1}.")
            return

    average = sum(marks) / num_subjects
    grade = calculate_grade(average)
    result_label.config(text=f"Average Marks: {average:.2f}\nGrade: {grade}")

def create_mark_entries():
    # Clear previous entries if any
    for widget in marks_frame.winfo_children():
        widget.destroy()
    try:
        num_subjects = int(num_subjects_entry.get())
        if num_subjects <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Enter a valid positive integer for number of subjects.")
        return

    global marks_entries
    marks_entries = []
    for i in range(num_subjects):
        label = tk.Label(marks_frame, text=f"Marks for subject {i+1}:", font=("Arial", 14))
        label.grid(row=i, column=0, padx=5, pady=5, sticky='e')
        entry = tk.Entry(marks_frame, font=("Arial", 14), width=10)
        entry.grid(row=i, column=1, padx=5, pady=5)
        marks_entries.append(entry)

root = tk.Tk()
root.title("Student Grade Calculator")
root.geometry("500x600")  # Bigger window size

title_label = tk.Label(root, text="Student Grade Calculator", font=("Arial", 20, "bold"))
title_label.pack(pady=15)

num_subjects_frame = tk.Frame(root)
num_subjects_frame.pack(pady=10)

num_subjects_label = tk.Label(num_subjects_frame, text="Enter number of subjects:", font=("Arial", 16))
num_subjects_label.pack(side=tk.LEFT, padx=5)

num_subjects_entry = tk.Entry(num_subjects_frame, font=("Arial", 16), width=5)
num_subjects_entry.pack(side=tk.LEFT, padx=5)

create_button = tk.Button(num_subjects_frame, text="Create Fields", font=("Arial", 14), command=create_mark_entries)
create_button.pack(side=tk.LEFT, padx=5)

marks_frame = tk.Frame(root)
marks_frame.pack(pady=20)

calculate_button = tk.Button(root, text="Calculate Grade", font=("Arial", 16), command=calculate)
calculate_button.pack(pady=20)

result_label = tk.Label(root, text="", font=("Arial", 18))
result_label.pack(pady=20)

root.mainloop()