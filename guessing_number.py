import random
import math

lower = int(input("Enter a number: "))
upper = int(input("Enter another number: "))
x = random.randint(lower, upper)
max_of_guess = round(math.log2(upper - lower + 1))

count = 0
while True:
    guess_num = int(input("Guess a number:"))
    count += 1
    if count > max_of_guess:
        print("Better Luck, Next Time!")
        break
    elif guess_num > x:
        print("Try again, Too high!")
        continue
    elif guess_num < x:
        print("Try again, Too small!")
        continue
    else:
        print("Congratulation! it's correct.")
        print(f"The number of guesses: {count}")
        break

    
    