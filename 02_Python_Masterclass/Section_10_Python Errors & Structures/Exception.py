n = int(input("Enter Numerator"))
d = int(input("Enter Denominator"))

try:
    result = n/d
    
except ZeroDivisionError:
    print('Cannot Divide a number by Zero')
else:
    print(result)
finally:
    print("This code will be executed no matter what")