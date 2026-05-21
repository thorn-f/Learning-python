import math

def add():
  while True:
     a = input("Enter a number: ")
     b = input("Enter another number: ")
     another_number = input("Another number?").lower()
     a = float(a)
     b = float(b)
     c = a + b
     print("The sum is", c)

def subtract():
    a = input("Enter a number: ")
    b = input("Enter another number: ")
    a = float(a)
    b = float(b)
    c = a - b
    print("The difference is", c)

def multiply():
    a = input("Enter a number: ")
    b = input("Enter another number: ")
    a = float(a)
    b = float(b)
    c = a * b
    print("The product is", c)

def divide():
    a = input("Enter a number: ")
    b = input("Enter another number: ")
    a = float(a)
    b = float(b)
    if b == 0:
        print("Error: Division by zero is not allowed.")
    else:
        c = a / b
        print("The quotient is", c)

def calc():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = input("Enter choice(1/2/3/4): ")
    if choice == '1':
        add()
    elif choice == '2':
        subtract()
    elif choice == '3':
        multiply()
    elif choice == '4':
        divide()
    else:
        print("Invalid input")

calc()