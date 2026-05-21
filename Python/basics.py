import random
import time
 
#Checks user's name and age
name = input("Name:")
age = int(input("Age:"))

if age < 18:
    print(f"Sorry {name}, you are not eligible to create an account.")
    exit()
else:
    print(f"Welcome {name}!")

#Checks user's email and password and account
account_available = input("Do you have an account? (yes/no):").lower()
if account_available == "no":
    while True:
      email = input("Enter your email to create an account:")
      if "@" not in email or "." not in email:
        print("Please enter a valid email address.")
        continue
      else:  
        break
    password = input("Generate random password? (yes/no):").lower()
    if password == "yes":
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
        password = "".join(random.sample(chars, 12))
        print(f"Your generated password is: {password}")
    else:
        password = input("Enter your desired password:")

    print("Account created successfully!")
else:
    email = input("Enter your email:")
    password = input("Enter your password:")
    print("Login successful!")

#Simulates loading
print("Loading", end="")
for i in range(5):
    time.sleep(0.5)
    print(".", end="")