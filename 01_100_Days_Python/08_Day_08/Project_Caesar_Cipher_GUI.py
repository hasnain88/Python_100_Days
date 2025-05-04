import tkinter as tk
from tkinter import messagebox
import random


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# Creating main window
root = tk.Tk()

# Setting window title and size
root.title("Caesar Cipher...")
root.geometry("300x200")


# Enter the direction "decode or encode"
tk.Label(root, text="Enter what do you want encode or decode ? ",font=('Arial',12,'bold'), fg="blue").pack(pady=10)
ca_direction = tk.Entry(root,width=30)
ca_direction.pack()

# Enter the shift number
tk.Label(root, text="Enter your shift number",font=('Arial',12,'bold'), fg="blue").pack(pady=10)
ca_shift_number = tk.Entry(root,width=30)
ca_shift_number.pack()


# Enter the text
tk.Label(root, text="Enter yout message...",font=('Arial',12,'bold'), fg="blue").pack(pady=10)
ca_text = tk.Entry(root,width=30)
ca_text.pack()

# Step 3: Result Label
result_label = tk.Label(root, text="", font=('Arial', 14, 'bold'),fg="red")
result_label.pack(pady=15)

# Step 4: Logic to calculate tip
def caesar():
    try:
        direction = ca_direction.get()
        shift = int(ca_shift_number.get())
        text = ca_text.get()

        output_text=""
        if direction=='decode':
            shift *= -1

        for letter in text:
            
            if letter not in alphabet:
                output_text+=letter

            else:
                shifted_possition = alphabet.index(letter) + shift
                shifted_possition %= len(alphabet)
                output_text += alphabet[shifted_possition] 
        
        result_label.config(text=f"Here is the {direction}d result = {output_text}")
        
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers only!")

# Step 5: Button to trigger calculation
tk.Button(root, text="Check", command=caesar, font=("Arial", 12)).pack(pady=10)


# Start the GUI Loop
root.mainloop()
