from gazebo.game import Game, Room
import gazebo.commands as commands

class mygame(Game):
    commands = {
        'look' : commands.look,
        'quit' : commands.quit,
        'go' : commands.change_room,
        'lel' : commands.unknown_command,
    }

    rooms = {
        'butt' : Room(
            "Your butt.",
            {
                'north' : 'face',
                'south' : 'ass',
            },
            {}
        ),
        'face' : Room(
            "Your face.",
            {
                'south' : 'butt',
                'east' : 'ass',
            },
            {}
        ),
        'ass' : Room(
            "Your anus.",
            {
                'north' : 'butt',
                'west' : 'face',
            },
            {}
        ),
    }

    room = rooms['butt']

if __name__=="__main__":
    game = mygame()
    game.run()
