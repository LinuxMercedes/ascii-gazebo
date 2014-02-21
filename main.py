from gazebo.game import Game
from gazebo.room import Room

def look(game, thing):
    print("Hah! You can't see", thing)

def quit(game, thing):
    game.done = True

class mygame(Game):
    commands = {
        'look' : look,
        'quit' : quit,
        'go' : Game.change_room,
        'lel' : Game.unknown_command,
    }

    rooms = {
        'butt' : Room(
            {
                'north' : 'face',
                'south' : 'ass',
            },
            {}
        ),
        'face' : Room(
            {
                'south' : 'butt',
                'east' : 'ass',
            },
            {}
        ),
        'ass' : Room(
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
