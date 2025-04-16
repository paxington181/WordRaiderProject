import random

title:str = "Word Raider"
words:str = []
solution:str = " "
wrong_let:str = []

def main():
    print(f"Welcome to {title}!")

    with open("wordlist.txt") as wordlist:
        for word in wordlist:
            words.append(word.rstrip().lower())
    solution = random.choice(words)
    max_turn:int = len(solution)
    letters = list(solution)
    print(f"Your word has {len(solution)} letters!  Good luck!")
    print("  ")
    turn_number:int = 0
    while turn_number < (max_turn + 1):
        if turn_number == max_turn:
            print(f"Game over!  The word was {solution}")
            break
        elif turn_number == (max_turn - 1):
            print("Last turn!")
        else:
            print(f"You have {max_turn - turn_number} turns remaining to guess the word.")
        guess = input(f"Please enter your {len(solution)} letter guess: ")
        guess.lower()
        guess_letters = list(guess)
        if len(guess) != len(solution):
            print("Incorrect word length, try again")
        elif guess.isalpha() is False:
            print("Please enter only letters.")
        elif guess == solution:
            print("Correct! You win!")
            break
        else:
            wrong_place:str = []
            correct_let:str = []
            temp_letters = letters.copy() 
            for i, g in enumerate(guess_letters):
                if g == temp_letters[i]: 
                    correct_let.append(g)
                    temp_letters[i] = None  
                elif g in temp_letters: 
                    wrong_place.append(g)
                    temp_letters[temp_letters.index(g)] = None 
                else: 
                    wrong_let.append(g)
            print(f"Correct letters in correct place: {correct_let}")
            print(f"Correct letters in the wrong place: {wrong_place}")
            print(f"Letters not in the word: {set(wrong_let)}")
            print(" ")
            turn_number += 1    

main()
