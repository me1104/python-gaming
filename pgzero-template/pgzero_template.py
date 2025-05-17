import pygame, pgzero, pgzrun
import sys

# Check Python version number. sys.version_info gives version as a tuple, e.g. if (3,7,2,'final',0) for version 3.7.2.
# Unlike many languages, Python can compare two tuples in the same way that you can compare numbers.
if sys.version_info < (3,5):
    print("This game requires at least version 3.5 of Python. Please download it from www.python.org")
    sys.exit()

# Check Pygame Zero version. This is a bit trickier because Pygame Zero only lets us get its version number as a string.
# So we have to split the string into a list, using '.' as the character to split on. We convert each element of the
# version number into an integer - but only if the string contains numbers and nothing else, because it's possible for
# a component of the version to contain letters as well as numbers (e.g. '2.0.dev0')
# We're using a Python feature called list comprehension - this is explained in the Bubble Bobble/Cavern chapter.
pgzero_version = [int(s) if s.isnumeric() else s for s in pgzero.__version__.split('.')]
if pgzero_version < [1,2]:
    print("This game requires at least version 1.2 of Pygame Zero. You have version {0}. Please upgrade using the command 'pip3 install --upgrade pgzero'".format(pgzero.__version__))
    sys.exit()

# Set up constants used by pgzero
WIDTH = 800
HEIGHT = 480
TITLE = "My Game!"

class Game:
    def __init__(self, controls=(None, None)):
        pass
    def draw(self):
        pass
    def update(self):
        pass
    

def update():
    '''
      periodically called by pygame
    '''
    game.update()


def draw():
    '''
      periodically called by pygame
    '''
    game.draw()    

'''
  some init code here
'''
global game

game = Game()

pgzrun.go()
