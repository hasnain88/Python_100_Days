# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# def caesar(original_text, shift_amount, encode_decode):
#     output_text=""
#     if encode_decode=='decode':
#         shift_amount *= -1

#     for letter in original_text:

        
#         if letter not in alphabet:
#             output_text+=letter

#         else:
#             shifted_possition = alphabet.index(letter) + shift_amount
#             shifted_possition %= len(alphabet)
#             output_text += alphabet[shifted_possition] 

#     print(f"Here is the {encode_decode}d result = {output_text}")

# should_countinue = True
# while should_countinue:

#     direction = input("Enter what do you want encode or decode ? ").lower()
#     text = input("Enter yout message...").lower()
#     shift = int(input("Enter your shift number."))

#     caesar(original_text=text,shift_amount=shift,encode_decode=direction)
#     restart = input("Do you want to continue... ?").lower()
#     if restart == 'no':
#         should_countinue=False
#         print("Good Bye....")


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
tk.Label(root, text="How many letters would you like in your password?",font=('Arial',12,'bold'), fg="blue").pack(pady=10)
nr_letters = tk.Entry(root,width=30)
nr_letters.pack()

# Enter the how many letters
tk.Label(root, text="How many symbols would you like in ?",font=('Arial',12,'bold'), fg="blue").pack(pady=10)
nr_symbols = tk.Entry(root,width=30)
nr_symbols.pack()


# Enter the how many letters
tk.Label(root, text="How many numbers would you like in ?",font=('Arial',12,'bold'), fg="blue").pack(pady=10)
nr_numbers = tk.Entry(root,width=30)
nr_numbers.pack()

# Step 3: Result Label
result_label = tk.Label(root, text="", font=('Arial', 14, 'bold'),fg="red")
result_label.pack(pady=15)

# Step 4: Logic to calculate tip
def password_generator():
    
    try:
        letters_inpass  = int(nr_letters.get())
        symbols_inpass = int(nr_symbols.get())
        numbers_inpass = int(nr_numbers.get())

        password_list = []

        for char in range(1, letters_inpass + 1):
            password_list.append(random.choice(letters))

        for char in range(1, symbols_inpass + 1):
            password_list += random.choice(symbols)

        for char in range(1, numbers_inpass + 1):
            password_list += random.choice(numbers)

        # print(password_list)
        random.shuffle(password_list)
        # print(password_list)

        password = ""
        for char in password_list:
            password += char


        result_label.config(text=f"Your Password is: {password}")


        
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers only!")

# Step 5: Button to trigger calculation
tk.Button(root, text="Check", command=password_generator, font=("Arial", 12)).pack(pady=10)


# Start the GUI Loop
root.mainloop()
