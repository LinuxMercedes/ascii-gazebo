from gazebo.game import Game, Room, Item, Player, NPC
import gazebo.commands as commands

class mygame(Game):
    def __init__(self):
        command_dict = {
            'look' : commands.look,
            'quit' : commands.quit,
            'go' : commands.change_room,
            'get' : commands.get,
            'inventory' : commands.inventory,
            'lel' : commands.unknown_command,
            'save' : commands.save,
            'load': commands.load,
        }

        rooms = {
            'butt' : Room(
                "Your butt.",
                {
                    'north' : 'face',
                    'south' : 'ass',
                },
                [
                    Item("dong", "A large dong"),
                ],
                []
            ),
            'face' : Room(
                "Your face.",
                {
                    'south' : 'butt',
                    'east' : 'ass',
                },
                [],
                []
            ),
            'ass' : Room(
                "Your anus.",
                {
                    'north' : 'butt',
                    'west' : 'face',
                },
                [],
                []
            ),
        }

        room = rooms['butt']

        player = Player()

        super().__init__(player, command_dict, rooms, room)

if __name__=="__main__":
    game = mygame()
    game.run()

