
class Game:
  done = False

  def prompt(self):
    command = input('> ')
    self.process_command(command)

  def process_command(self, command):
    for key, action in self.commands.items():
      if command.startswith(key):
        action(self, command[len(key):])
        break

  def update(self):
    pass

  def run(self):
    while(not self.done):
      self.prompt()
      self.update()

