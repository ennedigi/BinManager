import os
import sys
import time
import platform
import ColorConsole
from Util import *
from PrintUtil import *

####################################################################################

import zipfile


class Zipper(object):


  #=============================================================================
  # Set folderToZip, zip file name, target 
  #=============================================================================
  
  def __init__(self, folderToZip,targ,namefile=''):
    
    '''(folderToZip,target) '''

    #Set the zip filename
    
    y, m, d = time.localtime(time.time())[:3]
    
    #Se la versione viene dal Dev,il file e dev, altrimenti inizia con bin
    if not namefile:
      if folderToZip.find('Dev') == -1: self.namefile = 'bin_' + Util.twoDigits(str(d)) + Util.twoDigits(str(m)) + str(y) + '.zip'
      else: self.namefile = 'Dev_' + Util.twoDigits(str(d)) + Util.twoDigits(str(m)) + str(y) + '.zip'  
    else: self.namefile=namefile
    
    self.folderToZip = folderToZip
    
    if targ: self.target=targ 
    else: self.target = os.getcwd()
    
    
  #=============================================================================
  # Main function
  #=============================================================================

  def start(self):
    
    try:
    
      choice = ''
      
      while not choice == 'y':
        
        if choice: print 'Choice not valid!'; time.sleep(2)

        if platform.system() == 'Windows':     
          os.system('cls')
        else: os.system('clear')

        print '\nBinZipper \n================================='
        print '\nFolder to zip: ',
        ColorConsole.printC(self.folderToZip,'red')
        print '\nThe file: ',
        ColorConsole.printC(self.namefile,'red')
        print '\nwill be created in ',
        ColorConsole.printC(self.target,'red')
        
    
        choice = raw_input('\n\nAre you sure? (y/n) ')
  
        if choice == 'n':

          Util.setNewValue(self,'Folder to zip: ', self.folderToZip,'folderToZip')
          Util.setNewValue(self,'Zip file: ',self.namefile,'namefile',False)
          Util.setNewValue(self,'Destination: ',self.target,'target')

          choice=''


      self.zipBrain()

    except SystemExit: pass
    except: print sys.exc_info()[1],'The program has quit'


  def zipBrain(self):
    
    try:  
      
      cwd = os.getcwd()

      #INITIALIZE LOG FILE
      if not os.path.isdir('logs'): os.mkdir('logs')
      self.log = open(os.path.join('logs', self.namefile + '.log'), 'w')

      logHeader = 'Zip log ' + str(time.ctime()) + '\nSource: ' + self.folderToZip \
        + '\nTarget: ' + self.target + '\nFile name: ' + self.namefile + '\n'
      self.log.writelines(logHeader)

      os.chdir(self.target)
          
      zip_file = zipfile.ZipFile(self.namefile, 'w', zipfile.ZIP_DEFLATED)
  #DA TOGLIERE
      os.chdir(self.folderToZip)

      self.toZip('.', zip_file)
      
  #CLOSE LOG
      
      zip_file.close()

      os.chdir(cwd)

      end='\n{0} has been successfully created in {1}'.format(self.namefile, self.target)
      self.log.writelines(end)
      self.log.close()
      print end

    except SystemExit: pass
    except: print sys.exc_info()[1],'The program has quit'

  
  #=============================================================================
  # Add recursively all the files to the zip file
  #=============================================================================
  
  def toZip(self, relativePath, zip_file):
    '''Get the path that you want to zip'''
  #Create a log file  
    
    try:
      lista = os.listdir(relativePath)
    
      for f in lista:
        f_path = os.path.join(relativePath, f)  
        if os.path.isfile(f_path):
          print os.path.abspath(f_path)
          self.log.writelines(os.path.abspath(f_path) + '\n')
          zip_file.write(f_path)
        if os.path.isdir(f_path):
          self.toZip(f_path, zip_file)
    except: print 'Error in zipping the folder'

