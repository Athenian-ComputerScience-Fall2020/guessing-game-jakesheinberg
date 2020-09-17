# Guessing Game
## Problem Description
Write a guessing game that asks the user to guess a random number. You should plan for multiple scenarios:
* Correct guess: Write a message that tells the user their guess was correct. Include the value of the guess in the response.
* Guess too low: Write a message telling the user their guess was too low. Include the value of the guess in the response.
* Guess too high: Write a message telling the user their guess was too high. Include the value of the guess in the response.

Other notes:
* The user should have 5 tries to guess the correct number. If they do not guess it by the end, print a message telling them that the game is over and they lost. (Be kind...)
* You will need a random number for the user to guess. Be sure to import the random package and use the random integer method with the desired range:
  * Import: at the top of your program, type `import random`
  * Call: `random.randint(0,10)` This generates a random number between 0 and 10. Hint: if you assign it to a variable, you can use it more easily!
  
## Suggested Approach
1) Map out your strategy before you start typing.
2) Import the `random` package
3) Define your functions, if you are using any. (Functions are optional.)
4) Generate your number to be guessed (the random number) and get user input (guess)
5) Compare the values and pair possible outcomes with the appropriate message.
6) Consider the loop structure to have it run more than once. Be careful about which parts you want to run and which should stay the same. Do you want a new guess every time? Do you want a new random number every time? Place your loop accordingly.


