# Simple Calculator in python
# @Author Srinidh Reddy

import time


class cal():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

    def sub(self):
        return self.a - self.b

    def mod(self):
        # Modulo operator works like a % b returns remainder when a is divided by b
        # example 7 % 3 == 1
        return self.a % self.b


Reload = 'y'
while Reload == 'y':
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    obj = cal(a, b)

    print('Enter an Operation')
    print("0. Exit")
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulo")
    choice = int(input("Enter choice: "))
    if choice == 1:
        print("Result: ", obj.add())
    elif choice == 2:
        print("Result: ", obj.sub())
    elif choice == 3:
        print("Result: ", obj.mul())
    elif choice == 4:
        print("Result: ", round(obj.div(), 2))
    elif choice == 5:
        print("Result: ", obj.mod())
    elif choice == 0:
        print("Exiting the calculator")
    else:
        print("Invalid choice!!")
    print('\n')
    Reload = str(input("Do you want to make another calculation? \nPress 'y' for Yes and 'n' for No "))
    Reload = Reload.lower()
print()



# i changed almost eveything this bitch wrote, like didnt you even reb\view the shii you wrote
