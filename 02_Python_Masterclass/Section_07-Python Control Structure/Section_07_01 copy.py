products = [
    {'Name': 'Smart Phone', 'price': 500},
    {'Name': 'Laptop', 'price': 1000},
    {'Name': 'Tablet', 'price': 350},
    {'Name': 'Smart Watch', 'price': 200},
    {'Name': 'Bluetooth Speaker', 'price': 80},
    {'Name': 'Wireless Earbuds', 'price': 120},
    {'Name': 'Gaming Console', 'price': 400},
    {'Name': 'Smart TV', 'price': 600},
    {'Name': 'Digital Camera', 'price': 550},
    {'Name': 'E-Reader', 'price': 130},
    {'Name': 'VR Headset', 'price': 300},
    {'Name': 'Fitness Tracker', 'price': 100},
    {'Name': 'Drone', 'price': 450},
    {'Name': 'Portable Charger', 'price': 40},
    {'Name': 'Smart Home Hub', 'price': 150}
]

cart =[]


while True:
    choice = input("Do you want to continue shopping: ")
    if choice =='y':
        print("Here is a list of products and their prices")
        for index, product in enumerate(products):
            print(f"{index}: {product['Name']}: ${product['price']}")
        product_id = int(input("Enter the Id of the product you want to add to the cart"))
        # Check if the product is already in cart
        if products[product_id] in cart:
            # if present, increase the quantity of the product
            products[product_id]['Quantity']+=1
        else:
            # if not present, add the product to the cart with quantity 1
            products[product_id]['Quantity']=1
            cart.append(products[product_id])        
        # Code display the current cart contents, including the new, description, price and quantity
        
        total = 0
        print("Here are the contents in your cart")
        for product in cart:
            print(f"{product['Name']} :  ${product['price']} : QTY:{product['Quantity']}")
            total += product['price'] * product['Quantity']
        print(f"Cart total is: ${total}")
    else:
        break
print(f"Thank you, your final cart contents are {cart}")