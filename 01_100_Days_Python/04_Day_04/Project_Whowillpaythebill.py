

import tkinter as tk
from tkinter import messagebox  # for error popups
import random

# Creating main window
root = tk.Tk()


# Setting window title and size
root.title("Who will pay the bill ???")
root.geometry("300x200")


# Enter the name of the friends
tk.Label(root, text="Enter the name of your friends with comma seperated",font=('Arial',12,'bold'), fg="blue").pack(pady=10)
friends_list = tk.Entry(root,width=30)
friends_list.pack()

# Step 3: Result Label
result_label = tk.Label(root, text="", font=('Arial', 14, 'bold'),fg="red")
result_label.pack(pady=15)

# Step 4: Logic to calculate tip
def whopay():
    try:
        friends  = list(friends_list.get().split(','))
        persion = random.choice(friends)
        result_label.config(text=f"{persion} Will pay the bill...")
        
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers only!")

# Step 5: Button to trigger calculation
tk.Button(root, text="Check", command=whopay, font=("Arial", 12)).pack(pady=10)

# Start the GUI Loop
root.mainloop()

# Start the GUI Loop
# root.mainloop()



# import random


# friends = input("Enter the friends name with commas  :\n").split(',')
# list_friends = list(friends)
# print(list_friends)
# print(random.choice(list_friends))