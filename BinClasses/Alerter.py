import os
import sys
import time
import platform
import ColorConsole

from Util import *
from PrintUtil import *


class Alerter():
  DELAY=10.0


    #===========================================================================
    # Initialize all the folders which we want to check
    #===========================================================================
    
  def __init__(self,folders,skipMenu=False):
    #Folders that have to be checked
    self.filesFolderList=[]
    
    for i in folders:
      self.validateFolder(i)
  
    #Lista di liste di (folder, lista di file e data)
    
      self.filesFolderList.append([i,Util.mostRecentFiles(i)])
    
    #Clean the screen
    platform_pc=platform.system()
    if platform_pc == 'Windows':     
      os.system('cls')
    else: os.system('clear')
    
    self.menu(skipMenu)


  def menu(self,skipMenu):  

      while True:

        if platform.system() == 'Windows':     
          os.system('cls')
        else: os.system('clear')
        
      
        print '\nBinAlerter \n================================='
        print '\nYou will be alerted if any change occurs in one of the following folders:'
        for i in enumerate(self.filesFolderList):
          print '\n',i[0]+1,' ',
          ColorConsole.printC(i[1][0],'red')

        #Skip the menu
        if skipMenu: return
        
        choice = raw_input('\n\nAre you sure? (y/n) ')
      
        if choice == 'n':

          listOfFolders=[]

          while True:
                
            temp = raw_input('Enter the new (if any): ',)

            if temp == '': break
            elif not os.path.isdir(temp): 
              print ' Error:',temp, ' is not valid.'; time.sleep(2); continue
            else: listOfFolders.append(temp)

            c = raw_input('Yet another folder? (y/n) ')

            if c=='n': break
            elif c=='y': pass
            else: print ' Error: Input not valid.'; time.sleep(2)

          if not listOfFolders: sys.exit(0)
          else:   
            #Like in the constructor
            self.filesFolderList=[]
            for i in listOfFolders:
              self.validateFolder(i)
              self.filesFolderList.append([i,Util.mostRecentFiles(i)])
            break

        elif choice=='y': break
        else: print 'Choice not valid!'; time.sleep(2)
    

 ######
  def run(self):

    try:

      mostRecentArray=[]

      for i in self.filesFolderList:
        mostRecentArray.append([i[0],PrintUtil.printListOneDir(i[0],10)])
        # [path, lista file recenti]

        
      while True:

        for i in mostRecentArray:
          l = PrintUtil.printListCompareUpdate(i[1],i[0],10)
          if l: i[1]=l

        time.sleep(Alerter.DELAY)

    except SystemExit: pass
    except:
      print sys.exc_info()[1],'The program has quit'
      sys.exit(1)


  #=============================================================================
  # Check whether the folders are valid
  #=============================================================================
  
  def validateFolder(self, *folders):
    '''Check whether the path is a folder or not'''
    try:
      for d in folders:
        if os.path.isdir(d): pass
           
    except:
      print 'Error: the folder {0} is not valid'.format(d) 
      sys.exit(1)


  #===============================================================================
  # Manage the log files
  #===============================================================================

  def logInit(self):
    self.cwd = os.getcwd()
    
    self.log = open(os.path.join(self.cwd,'update.log'), 'w')
    logHeader = 'Update log ' + str(time.ctime())
    
    self.log.writelines(logHeader)
    
  def logClose(self):
    os.chdir(self.cwd)
      
    self.log.close()
