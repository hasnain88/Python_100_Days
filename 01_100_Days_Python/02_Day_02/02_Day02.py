print("Welcome to Tip calculator")
bill_amount = float(input("Enter total bill amount: $"))
tip_ratio = float(input("Enter a tip ratio: "))
people = int(input("Total number of person: "))

final_amount = round((bill_amount + (bill_amount*tip_ratio)/100)/people,2)

print(f"Total per person need to pay ${final_amount}")

