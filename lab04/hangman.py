# Joseph Naze - CIS109 - Hangman game

wordlist = [
    "hangman",
    "llama",
    "python",
    "guitar",
    "potato",
    "walrus",
    "friend",
    "hat",
    "dog",
    "cat",
    "key",
    "light",
    "turntable",
    "chocolate"
]

import random

random_number = random.randint(0, len(wordlist) - 1)


word = wordlist[random.randint(0,len(wordlist) - 1)]
board = list('_' * len(word))
bad_guesses = []
max_wrong = 6 

while(len(bad_guesses) <=max_wrong and "_" in board):
    print("\nWelcome to Hangman!\n")
    print(f"{board}\n")

    if(len(bad_guesses) == 1):
        print("""+---+
 |
 |
 |
 |    
 =======""")
        print("Bad Guesses:" , bad_guesses)

    if(len(bad_guesses) == 2):
        print("""+---+
 |   |
 |
 |
 |   
 =======""")
        print("Bad Guesses:" , bad_guesses)

    if(len(bad_guesses) == 3):
        print("""+---+
 |   |
 |   0
 |
 |    
 =======""")
        print("Bad Guesses:" , bad_guesses)

    if(len(bad_guesses) == 4):
        print("""+---+
 |   |
 |   0
 |   |
 |   
 =======""")
        print("Bad Guesses:" , bad_guesses)

    if(len(bad_guesses) == 5):
        print("""+---+
 |   |
 |   0
 |  /|\ 
 |
 =======""")
        print("Bad Guesses:" , bad_guesses)

    if(len(bad_guesses) == 6):
        print("""+---+
 |   |
 |   0
 |  /|\ 
 |  / \ 
 =======""")
        print("Bad Guesses:" , bad_guesses)
    

    guess = input("Guess a letter: ")

    # Validate Input 
    if len(guess) != 1 or not guess.isalpha():
        print("\n⚠️ Please enter exactly one letter.\n")
        input("Press [enter] to continue.")
        continue

    if guess in bad_guesses or guess in board: 
        print("\n⚠️ You already guessed that letter!\n")
        input("Press [enter] to continue.")
        continue
    is_found = False
    for i, letter in enumerate(word, start=0):
        if letter == guess:
            board[i] = word[i]
            is_found = True

    if not is_found:
        bad_guesses.append(guess)
        print(f"\n '{guess}'")

    if len(bad_guesses) == 6:
        print("You Lose!")
        print("The word was:" , word)
        break

