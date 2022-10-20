import random
from wsgiref import validate
from game.puzzle import Puzzle
from game.parachute import Parachute
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
        self.puzzle = Puzzle()
        self._parachute = Parachute()
        self._validate= True
        

    def start_game(self):
        for i in range (100):
            self.validator()
            self.show_parachute(self._validate)
            self.do_update()
            self.get_user_input()
               
     
    def do_update(self):
        self.puzzle.print_puzzle(self._guess)

    def get_user_input(self):
        self._guess = input("guess a letter [a-z]: ")
    
    def show_parachute(self, validator):
        self._parachute.print_parachute(validator)

    def validator(self):
        self._validate = self.puzzle._is_correct

    
    
 