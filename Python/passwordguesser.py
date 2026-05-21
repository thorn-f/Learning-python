import time

password = input("Enter the Password:")
start = time.time()
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
guess = []
for val in range(5):
    a = [i for i in chars]
    for y in range(val):
        a = [x + i for x in a for i in chars]
    guess = guess + a
    if password in guess:
        break
end = time.time()
clock = str(end - start)
print(f"Password guessed! It took {clock} seconds to guess your password '{password}'")