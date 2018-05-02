import itertools
from msvcrt import getch
from nltk.corpus import words
import random

class LetterToWordSlotMachine(object):

    def letterCollector(self):
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

    def valid_words_generator(self):
        validPermutations = []
        checking = bool
        while checking:
            letters = LetterToWordSlotMachine().letterCollector()
            permutations = [''.join(i) for i in itertools.product(letters, repeat = 3)]
            for each in permutations:
                if each in words.words():
                    validPermutations.append(each)
            if not validPermutations:
                print("No words could be generated, please enter new letters")
            else:
                break
        print(', '.join(validPermutations))
        return letters, validPermutations

    def slot_machine(self, letters, wordlist):
        pullLever = bool
        while pullLever:
            a = random.choice(letters)
            b = random.choice(letters)
            c = random.choice(letters)
            result = a.upper()+b+c
            print(result)
            if result.lower() in wordlist:
                print("Success")
                print("Try Again?\nPress Space to Pull the Lever\nPress Any Other Key to Quit")
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
    run = LetterToWordSlotMachine()
    userLetters, userWords = run.valid_words_generator()
    run.slot_machine(userLetters, userWords)
