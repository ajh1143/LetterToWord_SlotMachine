import itertools
from msvcrt import getch
from nltk.corpus import words
import random

def letterCollector():
    cases = ["A", "E", "I", "O", "U"]
    active = bool
    while active:
        char1 = input("Enter a Vowel")
        if char1.upper() in cases:
            break
        else:
            print("Try Again, Enter A, E, I, O, or U")
    while active:
        char2 = input("Enter a Vowel or Consonant")
        if char2.isdigit():
            print("Error, please enter a letter")
        else:
            break
    while active:
          char3 = input("Enter another Vowel or Consonant")
          if char3.isdigit():
              print("Error, please enter a letter")
          else:
              break
    letters = [char1.lower(), char2.lower(), char3.lower()]
    return letters

def valid_words_generator():
    validPermutations = []
    checking = bool
    while checking:
        letters = letterCollector()
        permutations = [''.join(i) for i in itertools.product(letters)]
        for each in permutations:
            if each in words.words():
                validPermutations.append(each)
        if not validPermutations:
            print("No words could be generated, please enter new letters")
        else:
            break
    return letters, validPermutations

def slot_machine(letters, wordlist):
    pullLever = bool
    while pullLever:
        a = random.choice(letters)
        b = random.choice(letters)
        c = random.choice(letters)
        result = a.upper()+b+c
        print(result)
        if result in wordlist:
            print("Success")
            keypress = ord(getch())
            if keypress == 32:
               pass
            else:
                break
        else:
            print("Fail")
            print("Try Again?\nPress Space to Pull the Lever\nPress Any Other Key to Quit")
            keypress = ord(getch())
            if keypress == 32:
                pass
            else:
                break
    return None

if __name__ == "__main__":

    userLetters, userWords = valid_words_generator()
    slot_machine(userLetters, userWords)
