import random

chars= "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"
length= int(input("enter length of password: "))
password=""

for i in range(length):
    password+=random.choice(chars)
print(password)