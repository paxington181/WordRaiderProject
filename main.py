import random

title:str = "Word Raider"
words:str = []
wrong_place:str = []
wrong_let:str = []

max_turn:int = 5
solution:str = " "

def main():
    print(f"Welcome to {title}!")

    with open("wordlist.txt") as wordlist:
        for word in wordlist:
            words.append(word.rstrip().lower())
    solution = random.choice(words)
    print(solution)
    print(f"Your word has {len(solution)} letters!  Good luck!")
    turn_number:int = 0
    while turn_number < (max_turn + 1):
        if turn_number == 5:
            print("Game over!")
            break
        elif turn_number == 4:
            print("Last turn!")
        else:
            print(f"You have {max_turn - turn_number} turns remaining to guess the word.")
        guess = input(f"Please enter your {len(solution)} letter guess: ")
        guess.lower()
        if len(guess) != len(solution):
            print("Incorrect word length, try again")
        elif guess.isalpha() is False:
            print("Please enter only letters.")
        elif guess == solution:
            print("Correct! You win!")
            break
        else:
            turn_number += 1
    

main()
