# Method - 01
# def chocolate():
#     print("Chocolate")


# def decorator(func):
#     def wrapper():
#         print("Wrapper up side")
#         func()
#         print("Wrapper Down side")

#     return wrapper

# chocolate = decorator(chocolate)
# chocolate()


# Method - 02
# def decorator(func):
#     def wrapper():
#         print("Wrapper up side")
#         func()
#         print("Wrapper Down side")

#     return wrapper

# @decorator
# def chocolate():
#     print("Chocolate")


# @decorator
# def cake():
#     print("cake")
# chocolate()
# cake()


# Method - 03
def decorator(func):
    def wrapper(*args,**keargs):
        print("Wrapper up side")
        func(*args,**keargs)
        print("Wrapper Down side")

    return wrapper

@decorator
def chocolate():
    print("Chocolate")


@decorator
def cake(name):
    print("cake"+" : "+name)
chocolate()
cake('apple')
