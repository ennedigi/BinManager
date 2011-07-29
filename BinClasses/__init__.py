import os
import sys
import time
import platform
import ColorConsole

from Copier import *
from Zipper import *
from Alerter import *
from ToTranslate import *

from Util import *
from PrintUtil import *

VERSION=' 1.0.4d'


  #=============================================================================
  # MAIN
  #=============================================================================


class Main(object):
  
  def __init__(self, source='', target='', dirAlert='', zipTarget='', transDir='',option='',
	      sound='',popup='',delay='',x64=''):
    '''Set the source (where the bin resides), target folder (where Methode is installed) and whether you have the option parameter, 
    runs directly the command'''
        
    if source: self.dirSource = source 
    else: self.dirSource = r"\\eidos2nas\Release\4.0\client\Methode\4.5"

    if target: self.dirTarget = target
    else: self.dirTarget = r"C:\Program Files\EidosMedia\Methode 4.0\bin"

    if dirAlert: self.dirAlert = dirAlert
    else: self.dirAlert = [self.dirSource,self.dirTarget]

    if zipTarget: self.zipTarget = zipTarget
    else: self.zipTarget = r'C:\ '
    
    if transDir: self.transDir = transDir
    else: self.transDir = os.path.join(self.dirTarget,'ToBeTranslated')

    #Check if they are actually folders
    self.validateFolder(self.dirSource, self.dirTarget)

    if sound.lower() == 'yes': PrintUtil.sound=True
    #else: PrintUtil.sound=False

    if popup.lower() == 'yes': PrintUtil.popup=True
    #else: PrintUtil.popup=False
	
    try:
      Alerter.delay=float(delay)
    except: Alerter.delay=10.0
    
    if x64.lower() == 'yes': Copier.x64=True
	
    if option == 'copy': Copier(self.dirSource,self.dirTarget).start()
    elif option == 'zip': Zipper(self.dirSource,self.zipTarget).start()
    elif option == 'alerter': Alerter(self.dirAlert,True).run()
    elif option == 'trans': ToTranslate(self.dirSource,self.dirTarget, self.transDir).start()
    
    else: self.menu()

  
  #===========================================================================
  # Validate files and folders
  #===========================================================================

  def validateFolder(self, *folders):
    '''Check whether the path is a folder or not'''
    
    for d in folders:
      if not os.path.isdir(d):
        print 'Error: the folder {0} is not valid'.format(d)

        print "Usage: [-src=source] [-trg=target] [-dir=folder1;folder2;... folders for the BinAlerter]"+ \
          "[-transDir=ToBeTranslated folder] [-opt= option: 'copy','zip','alerter','trans'] [-sound=yes|no]"+\
          "[-popup=yes|no] [-delay= delay of the BinAlerter] [-x64=yes|no]"
        sys.exit(0)
      
    
  #===========================================================================
  # MENU or forward the option given
  #===========================================================================
      
  def menu(self):
    try:
      choice = ''
      
      while not choice in ['1', '2', '3', '4','q']:
        
        if choice: print 'Choice not valid!'; time.sleep(2)
            
        ColorConsole.cleanScreen()
              
        print '\nWelcome to ',
        ColorConsole.printC('BinManager','red')
        print VERSION

        print '------------------------------\n'
        print '1) Install the last bin'
        print '2) Zip the last bin'
        print '3) Start Bin Alerter'
        print '4) Prepare the Translation'
        print 'q) Quit\n'

    
        choice = raw_input('Select: ')
        
        
      if choice == '1': Copier(self.dirSource,self.dirTarget).start()
      
      if choice == '2': Zipper(self.dirSource,self.zipTarget).start()
      
      if choice == '3': Alerter(self.dirAlert).run()

      if choice == '4': ToTranslate(self.dirSource,self.dirTarget, self.transDir).start()

      if choice == 'q': sys.exit(0)
  
    except SystemExit: print 'The program has quit';
    except: print sys.exc_info()[1]
