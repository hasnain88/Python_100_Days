import tkinter as tk
from tkinter import messagebox


# Creating main window
root = tk.Tk()

# Enter Height
tk.Label(root, text="Enter your height :",font=('Arial',12,'bold'), fg="blue").pack(pady=10)
height_entry = tk.Entry(root,width=30)
height_entry.pack()


# Enter Age
tk.Label(root, text="Enter your Age :",font=('Arial',12,'bold'), fg="blue").pack(pady=10)
age_entry = tk.Entry(root,width=30)
age_entry.pack()


# Step 3: Result Label
result_label = tk.Label(root, text="", font=('Arial', 14, 'bold'),fg="red")
result_label.pack(pady=15)

# Step 4: Logic to calculate tip
def rollercoster():
    try:
        hight = int(height_entry.get())
        age = int(age_entry.get())
        

        if hight <0 or age <0:
            messagebox.showerror("Error", "Please enter valid entery")
            return

        # Calculation
        if hight >=120:
            if age <= 12:
                result_label.config(text=f"You have to pay $5.")
            elif age <= 18:
                result_label.config(text=f"You have to pay $7.")
            else:
                result_label.config(text=f"You have to pay $12.")
        else:
            result_label.config(text=f"You can not ride..")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers only!")


# Step 5: Button to trigger calculation
tk.Button(root, text="Ckeck", command=rollercoster, font=("Arial", 12)).pack(pady=10)

# Start the GUI Loop
root.mainloop()
