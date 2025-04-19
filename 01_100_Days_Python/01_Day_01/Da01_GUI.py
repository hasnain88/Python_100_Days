import tkinter as tk
from tkinter import messagebox  # for error popups



# Creating main window
root = tk.Tk()

# City name entry
tk.Label(root, text="Enter the city name :",font=('Arial',12,'bold'), fg="blue").pack(pady=10)
city_name = tk.Entry(root,width=30)
city_name.pack()

# Pet name entry
tk.Label(root, text="Enter the Pet name :",font=('Arial',12,'bold'), fg="blue").pack(pady=10)
pet_name = tk.Entry(root,width=30)
pet_name.pack()

# Step 3: Result Label
result_label = tk.Label(root, text="", font=('Arial', 14, 'bold'),fg="red")
result_label.pack(pady=15)

# Step 4: Logic to calculate tip
def calculate_tip():
    try:
        cityname = city_name.get()
        petname= pet_name.get()
        

        if len(cityname) <= 0 or len(petname)<=0 :
            messagebox.showerror("Error", "Please enter valid entery")
            return

        # Calculation
        band_name = petname+" "+cityname
        result_label.config(text=f"Your Band Name is  :->{band_name}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers only!")

# Step 5: Button to trigger calculation
tk.Button(root, text="Calculate", command=calculate_tip, font=("Arial", 12)).pack(pady=10)

# Start the GUI Loop
root.mainloop()













# your_name = input("Enter your name")
# city_name = input("Enter your city name")
# band_name = city_name +" "+ your_name
# print(f"Your Band Name is {band_name}")
