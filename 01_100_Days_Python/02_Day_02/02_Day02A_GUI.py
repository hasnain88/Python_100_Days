import tkinter as tk
from tkinter import messagebox  # for error popups


# Creating main window
root = tk.Tk()


# Setting window title and size
root.title("My Firt GUI app")
root.geometry("300x200")


# Bill amount entery
tk.Label(root, text="Entter the total bill amount: $",font=('Arial',12,'bold'), fg="blue").pack(pady=10)
entry_bill = tk.Entry(root,width=30)
entry_bill.pack()

# Tip percentage calculator
tk.Label(root, text="Enter percentage :",font=('Arial',12,'bold'), fg="blue").pack(pady=10)
tip_percentage = tk.Entry(root,width=30)
tip_percentage.pack()

# Sharing Person
tk.Label(root, text="Enter Person",font=('Arial',12,'bold'), fg="blue").pack(pady=10)
person = tk.Entry(root,width=30)
person.pack()

# Step 3: Result Label
result_label = tk.Label(root, text="", font=('Arial', 14, 'bold'),fg="red")
result_label.pack(pady=15)

# Step 4: Logic to calculate tip
def calculate_tip():
    try:
        bill = float(entry_bill.get())
        tip = float(tip_percentage.get())
        people = int(person.get())

        if people <= 0:
            messagebox.showerror("Error", "Number of people must be more than 0.")
            return

        # Calculation
        total_per_person = round((bill + (bill * tip / 100)) / people, 2)
        result_label.config(text=f"Each person pays: ${total_per_person}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers only!")

# Step 5: Button to trigger calculation
tk.Button(root, text="Calculate", command=calculate_tip, font=("Arial", 12)).pack(pady=10)

# Start the GUI Loop
root.mainloop()