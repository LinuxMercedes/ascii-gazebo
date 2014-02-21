
class Game:
  """
  The game object. Handles setup, user interaction, etc.
  Subclass and implement additional methods to make your game.
  """

  done = False
  room = None
  prompt = '> '

  def change_room(self, direction):
    if self.room is None:
      return "Oops, you're not on the map. You should get that checked out."

    direction = direction[1:]
    if direction in self.room.adjacent:
      self.room = self.rooms[self.room.adjacent[direction]]
      return None
    else: 
      return "Can't go that way."

  def unknown_command(self, command):
    return "Hey, " + command  + " isn't a command, jackass"

  def get_input(self):
    """ Prompt user for actions """
    command = input(self.prompt)
    self.process_command(command)

  def process_command(self, command):
    """ Process commands from the user and hand off to the derived actions """
    for key, action in self.commands.items():
      if command.startswith(key):
        output = action(self, command[len(key):])
        if output:
          print(output)
        return

    output = self.unknown_command(command)
    if output:
      print(output)

  def update(self):
    pass

  def run(self):
    while(not self.done):
      self.get_input()
      self.update()

class Room:
  """ 
  A Room. Tracks adjacent rooms and contents.
  """
  def __init__(self, nearby, items):
    self.adjacent = nearby

