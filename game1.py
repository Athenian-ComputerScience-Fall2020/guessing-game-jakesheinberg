'''
Use this file to write an "open" version of the game (no test code or defined format). This will be translated into a testable program later. Use the reponse statements provided to make that transition easier.

"Your number is too high."
"Your number is too low."
"Your number is out of range."
"I'm sorry you are giving up!"
"I'm sorry, you are out of guesses."

'''
# Collaborators: none

import random

answer=random.randint(0,10)

guessnumber=0
while guessnumber <5:
    try:
        guess=int(input("Guess a number 1 through 10  or type '0' to quit: :  "))
        guessnumber=guessnumber+1
    except:
        print("please pick a number 1 through 10")
    guessnumber=guessnumber+1
    if guess == 0:
        print("you have quit")
        break
       
    elif guess==answer:
        print(f"You Got it on your {guessnumber} attempt!")
        break
    elif 0<guess<answer:
        print("Your number is too low.")
    elif 11>guess>answer:
        print("Your number is too high.")
    elif guess==5:
        print("I'm sorry, you are out of guesses.")
    else:
        print("Answer is out of range.")



