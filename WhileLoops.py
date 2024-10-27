### Part Two -- your code goes here. 
import random

a = input("Guess a number between 1-100:")

x = random.randint(1,100)

while a != x:
    a = int(input("Try again:"))

    if a == x: 
        print("Well Done!")
        break
