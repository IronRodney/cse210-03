import random
from game.puzzle import Puzzle
from game.parachute import Parachute
from game.rules import Rules
class Director:
    """A person that directs the game play
    
    The responsibility of a director is to control the game play
    
    Attributes:
        _guess = a users guess on the puzzle word
        _is_guess = a boolean to compare if the users gues is correct (same as the puzzle word)
        _parachute = an instance of the parachute class
        _rules = an instance of the rules class
        """
    def __init__(self):
        """Constructs a new Director
        
        Arg:
            self (Director):" An instance of director"""
        self._guess = ""
        self._puzzle = Puzzle()
        self._parachute = Parachute()
        self._rules = Rules()
        self._validate= True       

    def start_game(self):
        """Start the game by calling the methods in the direcor class 
        needed to run the game, and ending the game ones the user 
        exhausts their chances to guess the letter right
    
        Arg: none"""
        
        self.show_rules()
        while len(self._parachute._parachute) >1:
            self.show_parachute()
            self.show_puzzle()
            self.get_user_input()
            self.do_update()
        print("Game Over!") 
        
        if len(self._parachute._parachute) <1:
            print("Game Over!")     

    def show_parachute(self):
        """ Prints the jumper's parachute        
        Arg:
            self (_validate): a boolean variable that cuts a part of the 
            parachute if the user's guess is wrong or leave the 
            parachute intact if the user's guess is right"""
        self._parachute.print_parachute(self._validate) 
    
    def show_puzzle(self):
        """prints the user's guess(letter) if it is in the puzzle word, else prints a blank line.
        
        Arg:
            ._word: An attribute of puzzle word
            ._guesses: A list of all the user's guess"""
        for string in self._puzzle._word:
            if string in self._puzzle._guesses:
                print(string, end = " ")
            else:
                print("_", end=" ")
        print()

    def get_user_input(self):
        """Prompts the user for an input
        
        Arg:
            _guess: a letter"""
        self._guess = input("guess a letter [a-z]: ")  

    def do_update(self):
        """Updates the self._validate to true or false if the user's guess is true or false.
        
        Arg:
            self (guess): a letter (the user's guess)
            self (gueses): a list of letters(that stores all the user's correct guesses)"""
        self._puzzle.update_puzzle(self._guess)
        if self._guess in self._puzzle._guesses:
            self._validate = True
        else:
            self._validate = False
    
    def show_rules(self):
        """Displays the rules of the game
        
        Arg:
            self (answer): a sting (yes/no) to indicate if the user will like to see the rules of the game or not"""
        answer = input("Will you like to read the rules of the game (yes/no)? ")
        self._rules.print_rules(answer)
