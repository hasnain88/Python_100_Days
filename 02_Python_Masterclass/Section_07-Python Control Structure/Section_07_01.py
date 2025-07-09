products = [{'Name': 'Smart Phone', 'price': 500, 'Description': 'A handheld device used for communication and browsing the internet'},
    {'Name': 'Laptop', 'price': 1000, 'Description': 'A portable computer used for work, study, and entertainment'},
    {'Name': 'Tablet', 'price': 350, 'Description': 'A slim, portable device ideal for reading, watching videos, and casual browsing'},
    {'Name': 'Smart Watch', 'price': 200, 'Description': 'A wearable device that tracks fitness and connects to your phone'},
    {'Name': 'Bluetooth Speaker', 'price': 80, 'Description': 'A portable speaker that connects wirelessly for playing music'},
    {'Name': 'Wireless Earbuds', 'price': 120, 'Description': 'Compact earbuds with Bluetooth connectivity for hands-free audio'},
    {'Name': 'Gaming Console', 'price': 400, 'Description': 'A device designed for playing video games on a TV or monitor'},
    {'Name': 'Smart TV', 'price': 600, 'Description': 'A television with internet capabilities and streaming apps'},
    {'Name': 'Digital Camera', 'price': 550, 'Description': 'A device used to capture high-quality photos and videos'},
    {'Name': 'E-Reader', 'price': 130, 'Description': 'A portable device designed specifically for reading digital books'},
    {'Name': 'VR Headset', 'price': 300, 'Description': 'A virtual reality headset for immersive gaming and experiences'},
    {'Name': 'Fitness Tracker', 'price': 100, 'Description': 'A wearable device that monitors physical activity and health metrics'},
    {'Name': 'Drone', 'price': 450, 'Description': 'A flying device used for aerial photography and videography'},
    {'Name': 'Portable Charger', 'price': 40, 'Description': 'A battery pack used to charge devices on the go'},
    {'Name': 'Smart Home Hub', 'price': 150, 'Description': 'A central device for controlling smart home appliances and devices'}]

cart =[]


while True:
    choice = input("Do you want to continue shopping: ")
    if choice =='y':
        print("Here is a list of products and their prices")
        for index, product in enumerate(products):
            print(f"{index}: {product['Name']}: {product['Description']}: ${product['price']}")
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
        print(f"Final Products list {products}")
        total = 0
        print("Here are the contents in your cart")
        for product in cart:
            print(f"{product['Name']} : {product['Description']} : ${product['price']} : QTY:{product['Quantity']}")
            total += product['price'] * product['Quantity']
        print(f"Cart total is: ${total}")
    else:
        break
print(f"Thank you, your final cart contents are {cart}")