# -*- coding: utf-8 -*-

import functions.database as db

commands = {
    'go': 2,
    'pick': 2,
    'drop': 2,
    'use': 2,
    'push': 2,
    'pull': 2,
    'talk': 2,
    'fight': 2,
    'help': 2,
    'menu': 1,
    'inventory': 1,
    'look': 2,
    'quit': 1
}

menu = {
    1: 'Start a new game.',
    2: 'Continue playing.',
    3: 'Load a saved game.',
    4: 'Save a game.',
    5: 'Quit game'
}


def isValid(command):
    if len(command) == 0:
        return False
    elif command[0] in commands and len(command) <= commands[command[0]]:
        return True
    else:
        return False


def execute(command, directions, items, player):
    '''
    :param command: only valid commands came in from isValid(command)
    :return: "main" if switch context to "main", "game" if keep playing.
    '''

    if command[0] == "go":
        go(command, directions, player)

    elif command[0] == "help":
        if len(command) == 1:
            help()

        else:
            help(command[1])

    elif command[0] == "menu":
        return "main"

    elif command[0] == "quit":
        raise SystemExit

    elif command[0] == "look":
        if len(command) == 1:
            look(items)
        else:
            look(items, command[1])

    elif command[0] == "pick":
        if len(command) == 1:
            pick(items)
        else:
            pick(items, player, command[1])

    elif command[0] == "inventory":
        print(player.inventory)

    elif command[0] in commands:
        print('Command "{0:s}" is not implemented yet.'.format(command[0]))

    return "game"


def doMenu(selection=0):
    '''
    :param selection: int 1-5
    :return: "main" if keep context to "main", "game" if switch to playing.
    '''

    if selection == 0:
        print("--\nMain menu:")
        for key, value in menu.items():
            print("{} = {}".format(key, value))
        return "main"

    elif selection == 1:
        db.initializeDatabase()
        db.populateTables()
        db.createPlayer()
        return "game"

    elif selection == 2:
        return "game"

    elif selection == 5:
        raise SystemExit

    elif selection in menu:
        print("Menu item {0} not implemented yet.".format(selection))
        return "main"

    else:
        for key, value in menu.items():
            print("{} = {}".format(key, value))
        raise ValueError('Invalid selection {0:d}.'.format(selection))


def go(command, directions, player):
    if command[0] == "go" and len(command) == 1:
        print("You can go: ")
        for direction in directions.keys():
                print("\t* {}".format(direction))

    elif command[0] == "go" and len(command) == 2:
        if command[1] in directions:
            player.roomID = directions[command[1]]
            db.setPlayerRoomID(player.roomID)
        else:
            print(
                "Invalid direction. You can use "
                "only directions in list below:"
            )
            for direction in directions.keys():
                print("\t* {}".format(direction))


def help(command=None):
    if command == None:
        print("List of available commands:")
        for c in commands.keys():
            print("\t* {0:s}".format(c))
        print('For more information, please write "help [command]".')

    elif command in commands:
        print('help for "{0:s}" is not implemented yet.'.format(command))

    else:
        print('No help for "{0:s}". It is an invalid command.'.format(command))


def look(items,item=None):
    if item == None:
        if items != None:
            print("There is follow items in room:")
            for item in items:
                print("\t* {}".format(item))
        else:
            print("There is no items in room.")
    elif item in items:
        print(db.getItemDescription(item))
    else:
        print('Item "{}" not found.'.format(item))


def pick(items, player=None, item=None):
    if item == None:
        if items != None:
            print("You can pick items below:")
            for item in items:
                print("\t* {}".format(item))
        else:
            print("There is no items in room.")
    elif item in items:
        db.pickItem(item,player)
        print('You picked up item "{}".'.format(item))
        player.inventory.append(item)
    else:
        print('Cannot pick up item "{}".'.format(item))