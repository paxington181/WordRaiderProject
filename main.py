import random

title:str = "Word Raider"
words:str = []
wrong_place:str = []
wrong_let:str = []
correct_let:str = []
max_turn:int = 5
solution:str = " "

def main():
    print(f"Welcome to {title}!")

    with open("wordlist.txt") as wordlist:
        for word in wordlist:
            words.append(word.rstrip().lower())
    solution = random.choice(words)
    letters = list(solution)
    print(solution)
    print(f"Your word has {len(solution)} letters!  Good luck!")
    print(" ")
    turn_number:int = 0
    while turn_number < (max_turn + 1):
        if turn_number == 5:
            print(f"Game over!  The word was {solution}")
            break
        elif turn_number == 4:
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
            for g in guess_letters:
                for l in letters:
                    if l == g and letters.index(l) == guess_letters.index(g):
                        correct_let.append(g)
                    elif l == g and letters.index(l) != guess_letters.index(g):
                        wrong_place.append(g)
                    elif l != g:
                        wrong_let.append(g)
            print(f"Correct letters in correct place: {correct_let}")
            print(f"Correct letters in the wrong place: {set(wrong_place)}")
            print(f"Letters not in the word: {set(wrong_let)}")
            print(" ")
            turn_number += 1
    

main()
