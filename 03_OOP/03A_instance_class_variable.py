class A:
    counter = 0

    def __init__(self):
        A.counter += 1

obj1 = A()
obj2 = A()
obj3 = A()

print(A.counter)

