'''
Use this file to write an "open" version of the game (no test code or defined format). This will be translated into a testable program later. Use the reponse statements provided to make that transition easier.

"Your number is too high."
"Your number is too low."
"Your number is out of range."
"I'm sorry you are giving up!"
"I'm sorry, you are out of guesses."

'''
# Collaborators: Megan
import random
def guessing_game():
    start_rang=int(input("What would you like the range to start at: "))
    end_rang=int(input("What would you like the range to end at: "))
    choices=(end_rang+1)-(start_rang) # used for print statement about how manu numbers to choose from
    guesses_avail=int(input(f"There are {choices} numbers to guess from. How many guesses would you like: ")) #how many attempts
    answer=random.randint(start_rang,end_rang+1) #sets value that should be guessed

    guessnumber=1
    while guessnumber <=guesses_avail:
        guess=(input(f"Guess a number between {start_rang} and {end_rang} or type 'done' to quit: :  "))
        try:#deals w string or float inputs
            guess=int(guess)
        except:
            if guess=="done":
                print("You have quit. Come again soon!") #quit game protocal
                break
            else:
                guess=input(f"Please pick a number {start_rang} through {end_rang}:  ")
                

        if guess==answer:
            print(f"You Got it on attempt {guessnumber}!")
            break
        elif 0<guess<answer:
            print("Your number is too low.")
            guessnumber=guessnumber+1
        elif 11>guess>answer:
            print("Your number is too high.")
            guessnumber=guessnumber+1
        elif guess==5:
            print("I'm sorry, you are out of guesses.")
        else:
            print("Answer is out of range.")
    playagain=input("Would you like to play again: ")
    playagain=playagain.upper()#used to make it not case sensitive 
    if playagain== "YES" or playagain=="YA":
        guessing_game()


guessing_game()
