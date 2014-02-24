import pickle
from copy import deepcopy

def save(game, filename):
    if len(filename) <= 1:
        return "Need a filename to save to!"

    with open(filename[1:], mode='wb') as save_file:
        pickle.dump(game, save_file)

    return "Saved to " + filename[1:]

def load(game, filename):
    if len(filename) <= 1:
        return "Need a filename to load from!"

    with open(filename[1:], mode='rb') as save_file:
        loaded = pickle.load(save_file)
        game.__dict__.update(loaded.__dict__)

    return "Game loaded from " + filename[1:]

def look(game, thing):
    if len(thing) > 1:
        thing = thing[1:]
        for item in game.room.items:
            if thing == item.name:
                return item.description
        else:
            return "Can't look at " + thing

    return game.room.describe()

def change_room(game, direction):
    if game.room is None:
        return "Oops, you're not on the map. You should get that checked out."

    direction = direction[1:]
    if direction in game.room.nearby:
        game.room = game.rooms[game.room.nearby[direction]]
        return game.room.describe()
    else: 
        return "Can't go that way."

def quit(game, thing):
    game.done = True

def unknown_command(game, command):
    return "Hey, " + command  + " isn't a command, jackass"


