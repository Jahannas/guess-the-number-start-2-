from random import randint

EASY_TURN = 10
HARD_TURN = 5

  
def check_answer (guess,number,turns):
  
      if guess > number:
            print ("Too High")
            return turns-1
      elif guess < number:
            print ("Too Low")
            return turns-1
      else:
        print(f"You got it! Guess is {guess}")
       
def set_difficulty():
  
    difficulty = input ("Choose a difficulty. Type 'easy' or 'hard':")
    if difficulty == "easy":
      return EASY_TURN
    
    if difficulty == "hard":
      return HARD_TURN

def game():  
  print("Welcome to the number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  number = randint(1,100)
  print(f"Psst. Guessed number is {number}")
  
  turns = set_difficulty()
   
  guess = 0      
  while guess != number:
    print(f"You have {turns} attempts remaining.")
    
    guess = int(input("Guess a number: "))
  
    turns = check_answer(guess,number,turns)
    if turns == 0: 
      print(f"You have left no guess.")
      return
    elif guess != number:
      print("Guess again.")
game()  
    
#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).



