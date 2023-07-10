import random

#Gets the player's name to initiate game
print('Hello, what is your name?')
name = input()

#Create the Secret Number and get started
secret_number = random.randint(1,20)
print(f"Well, {name}, I'm thinking of a number between 1 and 20. Guess what it is:")

#Allows for 7 Guesses
for guesses in range (1,7):
    #User to input guess
    user_guess = int(input())
    #Guess is too low
    if user_guess < secret_number:
        print(f"{user_guess} is too low. Try again!")
    #Guess is too high
    elif user_guess > secret_number:
        print(f"{user_guess} is too high. Try again!")
    #Correct Guess or runs out of guesses
    else:
        break

#Instant Win
if user_guess == secret_number and guesses == 1:
    print(f"Great job, {name}! You guessed {secret_number} right away!")

#Eventual Win
elif user_guess == secret_number:
    print(f"Great job, {name}! You guessed {secret_number} in {guesses} guesses!")

#Losing
else:
    print(f"You're taking too long to figure this out. The number I was thinking of was {secret_number}. Sucks to be you, {name}!")
    
    
