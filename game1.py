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
def guessing_game():
    start_rang=int(input("What would you like the range to start at: "))
    end_rang=int(input("What would you like the range to end at: "))
    choices=end_rang-start_rang+1
    guesses_avail=int(input(f"There are {choices} numbers to guess from. How many guesses would you like: "))
    answer=random.randint(start_rang,end_rang+1)

    guessnumber=0
    while guessnumber <guesses_avail:
        guess=(input(f"Guess a number between {start_rang} and {end_rang} or type 'done' to quit: :  "))
        try:
            guess=int(guess)
            guessnumber=guessnumber+1
        except:
            if guess=="done":
                print("You have quit. Come again soon!")
                break
            else:
                print("Please pick a number 1 through 10")

            print("please pick a number 1 through 10")
        guessnumber=guessnumber+1
        if guess==answer:
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
    playagain=input("Would you like to play again: ")
    playagain=playagain.upper()
    if playagain== "YES" or "YA":
        guessing_game()
    else:
        break



guessing_game()
