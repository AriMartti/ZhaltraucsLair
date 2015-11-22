# -*- coding: utf-8 -*-

commands = {
    'go' : 2,
    'turn' : 1,
    'help' : 2,
    'exit' : 1
}

directions = (
    'left',
    'right',
    'front',
    'up',
    'down'
)

menu = {
    1 : 'Start a new game.',
    2 : 'Load a saved game.',
    3 : 'Save a game.',
    4 : 'Quit game'
}

def isValid(command):
    if command[0] in commands and len(command) <= commands[command[0]]:
        return True
    else:
        return False


def execute(command):
    if command[0] in ("go", "turn"):
        go(command)
    elif command[0] == "help":
        if len(command) == 1:
            help()
        else:
            help(command[1])


def go(command):
    if command[0] == "go" and len(command) == 1:
        print("go", directions)
    elif command[0] == "go" and len(command) == 2:
        if command[1] in directions:
            print(command)
        else:
            print(
                "Invalid direction. You can use only directions in list below:"
            )
            print(directions)
    elif len(command) == 1 and command[0] == "turn":
        print(command)

def help(command="none"):
    if command == "none":
        print("List of available commands:")
        print(commands.keys())
    elif command in commands:
        print('help for "{0:s}" is not implemented yet.'.format(command))
    else:
        print('No help for "{0:s}". It is invalid command.'.format(command))

def doMenu(selection=0):
    if selection == 0:
        print(menu)
    elif selection == 1:
        print (menu[selection])
    elif selection == 4:
        raise SystemExit
    elif selection in menu:
        print ("Menu item {0} not implemented yet.".format(selection))
    else:
        print(menu)
        raise ValueError('Invalid selection {0:d}.'.format(selection))