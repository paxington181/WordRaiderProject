import random

title:str = "Word Raider"
words:str = []

def main():

    with open("wordlist.txt") as wordlist:
        for word in wordlist:
            words.append(word.rstrip().lower())

    print(random.choice(words))

main()
