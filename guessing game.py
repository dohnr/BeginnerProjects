import random
secret_number = (random.randint(1,10))
guess = 0
tries = 0
print("You have a 50% shot of winning!")
while tries < 5 and guess != secret_number:
    guess = int(input("Guess a number between 1 and 10:"))
    tries = tries + 1

if guess == secret_number:
    print("You won! The number was" , secret_number)
else:
    print("You lost! The number was" , secret_number)
