
class Parachute:
  """A jump Parachute
    The responsibility of Parachute is to print the jumpers 
    if the player's is coreect the parachute remains intact
    else, if the players guess is wrong a line is cut on the players parachute"""
  def __init__(self):
    """Constructs a new parachite"""
    self._parachute = ["      _____","     |_____|","    |       |","    |       |","    |       |","     \\     /","      \\   /","       \\ /","        o","      **|**","        |","       * *","      *   *","    ^^^^^^^^^"]

  def print_parachute(self, validator):
    """prints the user's parachute
    
    arg:
    validator: a parameter that stores true or false"""
    print()
    if validator is True:
      for i in self._parachute:
        print(i)
    else:
      print()
      self._parachute.pop(0)
      for i in self._parachute:
        print(i)
    