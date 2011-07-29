STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE= -11
STD_ERROR_HANDLE = -12

# wincon.h
FOREGROUND_BLACK     = 0x0000
FOREGROUND_BLUE      = 0x0001
FOREGROUND_GREEN     = 0x0002
FOREGROUND_CYAN      = 0x0003
FOREGROUND_RED       = 0x0004
FOREGROUND_MAGENTA   = 0x0005
FOREGROUND_YELLOW    = 0x0006
FOREGROUND_GREY      = 0x0007
FOREGROUND_INTENSITY = 0x0008 # foreground color is intensified.
BACKGROUND_BLACK     = 0x0000
BACKGROUND_BLUE      = 0x0010
BACKGROUND_GREEN     = 0x0020
BACKGROUND_CYAN      = 0x0030
BACKGROUND_RED       = 0x0040
BACKGROUND_MAGENTA   = 0x0050
BACKGROUND_YELLOW    = 0x0060
BACKGROUND_GREY      = 0x0070
BACKGROUND_INTENSITY = 0x0080 


FOREGROUND_BLUE = 0x01 # text color contains blue.
FOREGROUND_GREEN= 0x02 # text color contains green.
FOREGROUND_RED  = 0x04 # text color contains red.
FOREGROUND_INTENSITY = 0x08 # text color is intensified.
BACKGROUND_BLUE = 0x10 # background color contains blue.
BACKGROUND_GREEN= 0x20 # background color contains green.
BACKGROUND_RED  = 0x40 # background color contains red.
BACKGROUND_INTENSITY = 0x80 # background color is intensified.

#Colors array just for the example
colors={}
colors['red']=FOREGROUND_RED | FOREGROUND_INTENSITY
colors['green']=FOREGROUND_GREEN | FOREGROUND_INTENSITY
colors['black']=FOREGROUND_BLACK
colors['blue']=FOREGROUND_BLUE
colors['cyan']=FOREGROUND_CYAN
colors['magenta']=FOREGROUND_MAGENTA
colors['yellow']=FOREGROUND_YELLOW
colors['grey']=FOREGROUND_GREY

colors['std']=BACKGROUND_BLACK | FOREGROUND_GREY

import ctypes
import sys,os
from termcolor import colored
import platform

if platform.system()=='Windows':
  std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

def __set_color(color):
  """(color) -> BOOL Example: set_color(FOREGROUND_GREEN | FOREGROUND_INTENSITY)"""
  bool = ctypes.windll.kernel32.SetConsoleTextAttribute(std_out_handle, color)
  return bool


def printC(text,c):
  '''(text,color) -> colored text \n example: printC(test,'red') '''
  if platform.system()=='Windows':
    __set_color(colors[c])
    sys.stdout.write(text)
    __set_color(colors['std'])
  else: print colored(text,c),
  
  
def sound(seconds=500):
  if platform.system() == 'Windows':     
    import winsound
    winsound.MessageBeep()

def cleanScreen():
  if platform.system() == 'Windows':     
    os.system('cls')
  else: os.system('clear')


#ColorsConsole().printC('prova','red')
#col('prova','green')
#raw_input() #Keep console from closing
