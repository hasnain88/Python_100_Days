def product(**kwargs):
    for key, value in kwargs.items():
        print(key+":"+value)



product(name='Phone',price = "500")
product(name='IPhone',price ="1500",details = "This is Iphone")