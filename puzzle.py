import random
class Puzzle:
    """A collection of words
    The responsibility of Puzzle is to generate a random word
    and print the word with all is letters missing"""

    def __init__(self):
        """Construct a list of puzzle words"""
        self._words = ["jump", "aeroplane", "basket", "pencil","botswana", "nigeria"]
        self._word=random.choice(self._words)
        self._is_correct = True
        self._guesses = []
        self._lives = 4
        self._word_length = len(self._word)
        self._display = []
        self._still_playing = True
    
    def print_puzzle(self, guess=""):
        """ A method that prints the puzzle word with missing letters"""
        for _ in range(self._word_length):
            self._display == "_"


        while self._still_playing:

            for position in range(self._word_length):
                letter = self._word[position]

                if guess == letter:
                    self.display[position] = letter

                if guess not in self._word:
                    lives -= 1

                    if lives == 0:
                        self._still_playing = False
                        print("You lose.")

                if "_" not in self._display:
                    self._still_playing = False
                    print("Well done, you win!")

