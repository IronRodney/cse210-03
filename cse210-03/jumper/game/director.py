import random
from tkinter import SEL
from game.puzzle import Puzzle
class Director:
    """A person that directs the game play
    
    The responsibility of a director is to control the game play
    
    Attributes:
        _guess = a users guess on the puzzle word
        _is_guess = a boolean to compare if the users gues is correct (same as the puzzle word)
        """
    def __init__(self):
        """Constructs a new Director
        
        Arg:
            self (Director):" An instance of director"""
        self._guess = ""
        self._guesses=[]
        self._is_guess = True
        self._play_again="yes"
        self.puzzle = Puzzle()
        

    def start_game(self):
        self.do_update()
        for i in range (100):
            self.get_user_input()
            self.do_update()
        
        
    def get_user_input(self):
        self._guess = input("guess a letter [a-z]: ")

    def do_update(self):
        self.puzzle.print_puzzle(self._guess)
    
 