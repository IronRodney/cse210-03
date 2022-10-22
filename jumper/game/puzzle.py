import random
class Puzzle:
    """A collection of words
    The responsibility of Puzzle is to generate a random word
    and print the word with all is letters missing"""

    def __init__(self):
        """Construct a list of puzzle words"""
        self._words = ["jump", "aeroplane", "basket", "pencil","botswana", "nigeria", "apple", "elephant", "tiger"]
        self._word=random.choice(self._words)
        self._guesses = []
    
    def update_puzzle(self, guess):
        """ A method that prints the puzzle word with missing letters
        arg:
        guess: the users guess in form of a letter"""
        for letter in self._word:
            if guess==letter:
                self._guesses.append(guess)
            else:
                self._guesses=self._guesses