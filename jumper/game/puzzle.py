import random
class Puzzle:
    """A collection of words
    The responsibility of Puzzle is to generate a random word
    and print the word with all is letters missing"""

    def __init__(self):
        """Construct a list of puzzle words"""
        self._words = ["jump", "aeroplane", "basket", "pencil","botswana", "nigeria"]
        self._word=random.choice(self._words)
    
    def print_puzzle(self, guess="", guesses=[]):
        """ A method that prints the puzzle word with missing letters"""
        for letter in self._word:
            if guess==letter:
                guesses.append(guess)
            else:
                guesses=guesses
        for string in self._word:
            if string in guesses:
                print(string, end=" ")
            else:
                print("_", end=" ")
        print()