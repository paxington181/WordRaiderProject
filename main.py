import random

title:str = "Word Raider"
words:str = []
wrong_place:str = []
wrong_let:str = []
turn_number:int = 0
max_turn:int = 5
solution:str = " "

def main():
    print(f"Welcome to {title}!")

    with open("wordlist.txt") as wordlist:
        for word in wordlist:
            words.append(word.rstrip().lower())
    solution = random.choice(words)

    print(f"Your word has {len(solution)} letters!  Good luck!")
    print(f"You have {max_turn - turn_number} turns remaining to guess the word.")
    while turn_number <= max_turn:
        #building gameplay loop https://app.dataquest.io/c/93/m/855/guided-project%3A-word-raider/6/validate-the-guessed-word
    print(solution)

main()
