print("Roller coaster price and eligibility check program")

height = float(input("Enter your height: "))
if height >=120:
    print("You are eligible for the ride...")
    age = int(input("Enter your age..."))
    
    if age <12:
        bill = 5
        print(f"You have to pay ${bill}")

    elif age >=12 | age<=18:
        bill = 7
        print(f"You have to pay ${bill}")
    
    elif age > 18:
        bill = 12
        print(f"You have to pay ${bill}")
        
    photo =input("Do you need a photo?[y/n]").lower()

    if photo=='y':
        bill+=3
    
    print(f"Your final bill {bill}")
    


        
else:
    print("You can not ride sorry.....")

