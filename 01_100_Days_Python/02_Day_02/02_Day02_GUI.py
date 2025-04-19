import tkinter as tk
from tkinter import messagebox

def calculate_tip():
    try:
        bill = float(entry_bill.get())
        tip = float(entry_tip.get())
        people = int(entry_people.get())
        
        if people <= 0:
            messagebox.showerror("Invalid Input", "Number of people must be greater than zero.")
            return

        final_amount = round((bill + (bill * tip) / 100) / people, 2)
        result_label.config(text=f"Total per person: ${final_amount}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

# Create main window
root = tk.Tk()
root.title("Tip Calculator")
root.geometry("3000x2500")

# Labels and Entries
tk.Label(root, text="Total Bill Amount ($):").pack(pady=5)
entry_bill = tk.Entry(root)
entry_bill.pack()

tk.Label(root, text="Tip Percentage (%):").pack(pady=5)
entry_tip = tk.Entry(root)
entry_tip.pack()

tk.Label(root, text="Number of People:").pack(pady=5)
entry_people = tk.Entry(root)
entry_people.pack()

# Calculate Button
tk.Button(root, text="Calculate", command=calculate_tip).pack(pady=10)

# Result
result_label = tk.Label(root, text="", font=('Arial', 12, 'bold'))
result_label.pack()

root.mainloop()