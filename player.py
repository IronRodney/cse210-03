from game.word import pick

class Player:

    def __init__(self):

        self._guess = ""


    def guess(self, guess):
        """
        This will allow the player to guess the word
        """
        self._guess = guess

    def get_guess(self):
        """
        This will return the current guess
        """
        guess = self._guess
        return guess