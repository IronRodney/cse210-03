class Parachute:
  """A jump Parachute
    The responsibility of Parachute is to print the jumpers 
    if the player's is coreect the parachute remains intact
    else, if the players guess is wrong a line is cut on the players parachute"""
  def __init__(self):
    self._is_correct=False
    self._parachute=["      _____","     |_____|","    |       |","     \\     /","      \\   /","       \\ /","        o","      **|**","        |","       * *","      *   *","    ^^^^^^^^^","\n"]
  def show_parachute(self):
    if self._is_correct is True:
      for i in self._parachute:
        print(i)
    else:
      self._parachute.pop[0]
      for i in self._parachute:
        print(i)

Parachute().show_parachute()