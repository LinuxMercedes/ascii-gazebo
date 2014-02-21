from gazebo.game import Game

def look(game, thing):
    print("Hah! You can't see", thing)

def quit(game, thing):
    game.done = True

class mygame(Game):
    commands = {
        'look' : look,
        'quit' : quit,
    }

if __name__=="__main__":
    game = mygame()
    game.run()
