from gazebo.commands import unknown_command

class Game:
    """
    The game object. Handles setup, user interaction, etc.
    Subclass and implement additional methods to make your game.
    """

    done = False
    room = None
    prompt = '> '
    
    def __init__(self, player, commands, rooms, room):
        self.player = player
        self.commands = commands
        self.rooms = rooms
        self.room = room

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

        output = unknown_command(self, command)
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
    def __init__(self, description, nearby, items, npcs):
        self.description = description
        self.nearby = nearby
        self.items = self._make_dict(items)
        self.npcs = self._make_dict(npcs)

    def _make_dict(self, things):
        d = {}
        for thing in things:
            d[thing.name] = thing
        return d

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
        for item in self.items.keys():
            ret.append(item)
            ret.append(', ')
        ret[-1] = '. '

        return ''.join(ret)

class Item:
    """ 
    An item. 
    """
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Player:
    """ 
    A player
    """

    def __init__(self, inventory = {}):
        self.inventory = inventory

class NPC:
    """
    An NPC or enemy
    """
    def __init__(self, name, description):
        self.name = name
        self.description = description

