
class Game:
  """
  The game object. Handles setup, user interaction, etc.
  Subclass and implement additional methods to make your game.
  """

  done = False
  room = None
  prompt = '> '

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
  A Room. Tracks description, adjacent rooms, and contents.
  """
  def __init__(self, description, nearby, items):
    self.description = description
    self.nearby = nearby
    self.items = items

  def describe(self):
    ret = [self.description]
    if len(self.nearby):
      ret.append(' Obvious exits are ')
      for key in sorted(self.nearby.keys()):
        ret.append(key)
        ret.append(', ')
      ret[-1] = '. '
    if len(self.items):
      ret.append(' There is a ')
      for key in sorted(self.items.keys()):
        ret.append(key)
        ret.append(', ')
      ret[-1] = '. '

    return ''.join(ret)

