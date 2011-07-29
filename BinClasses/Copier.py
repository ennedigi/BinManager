
import os
import sys
import time
import platform
import ColorConsole

from Util import *
from PrintUtil import *
###########################################################################

import shutil

class Copier(object):

  x64=False
  
  #=============================================================================
  # Set source and target
  #=============================================================================
  
  def __init__(self, source, target):
    '''Set the source and the target folder'''
    
    self.dirSource = source
    self.dirTarget = target
    

  #=============================================================================
  # Menu 
  #=============================================================================


  def start(self):

    try:
      
      choice = ''
      
      while not choice in ['y','n']:

        if choice: print ' Error: Input not valid.'; time.sleep(2);
        
        #Clean screen
        ColorConsole.cleanScreen()
        
        print '\nBinCopier \n================================='
        print '\nSource: ',
        ColorConsole.printC(self.dirSource,'red')
        print '\nTarget: ',
        ColorConsole.printC(self.dirTarget,'red')
    
        choice = raw_input('\n\nAre you sure? (y/n) ')
  
  #Redefine and the relative messages to print on screen
        if choice == 'n':
          Util.setNewValue(self,'Source: ',self.dirSource,'dirSource')
          Util.setNewValue(self,'Target: ',self.dirTarget,'dirTarget')

          choice = ''

  #Print the list of the most recent
      PrintUtil.printListCompare2(self.dirSource,self.dirTarget)

      choice=''
      
      while not choice in ['1','2']:
        
        if choice: print 'Choice not valid!'; time.sleep(2)
     
        choice = raw_input('\n\n(1) Update the folder \n(2) Replace all the files\n Select [1,2]: ')
  
  #Init the LOG
      self.logInit()
        
      if choice=='1': self.copyFun(self.dirSource,self.dirTarget,'','update')
      if choice=='2': self.copyFun(self.dirSource,self.dirTarget,'','replace')
      
      if not self.n_err and self.n_file: 
        if Copier.x64: self.updateDLLs('register_4.0_x64.bat')
        else: self.updateDLLs()

      self.logClose()

    except SystemExit: pass
    except: print sys.exc_info()[1],'The program has quit'

  #===============================================================================
  # Manage the log files
  #===============================================================================



  def logInit(self):
    self.cwd = os.getcwd()

    if not os.path.isdir('logs'): os.mkdir('logs')

    y,m,d= time.localtime()[:3]
    hh,mm= time.localtime()[3:5]
    
    nome_log='Copy_' + Util.tupleToStr((hh,mm)) + '_' + Util.tupleToStr((d,m,y)) + '.log'
   
    self.log = open(os.path.join('logs',nome_log), 'w')
    logHeader = 'Copy log ' + str(time.ctime()) + '\nSource: ' + self.dirSource \
      + '\nTarget: ' + self.dirTarget + '\n'
    self.log.writelines(logHeader)
    
    #INIT THE variable for the log statistic
    self.n_err=self.n_cop=self.n_upd=self.n_file=0
    
  def logClose(self):
    
    if self.n_err==0 and self.n_cop!=0:
      end='\n{0}/{1} files have been successfully copied to {2}'.format(self.n_cop,self.n_file, self.dirTarget)
    elif self.n_err==0 and self.n_upd!=0:
      end='\n{0}/{1} files have been successfully updated in {2}'.format(self.n_upd,self.n_file, self.dirTarget)
    else: end='Copy completed with '+str(self.n_err)+' errors on '+str(self.n_file)+' files'

    self.log.writelines(end)
    self.log.close() 
    
    print end
    print 'Log created in', os.path.join(self.cwd,'logs')
    os.chdir(self.cwd)

  #=============================================================================
  # Replace all the directory
  #=============================================================================


  def copyFun(self,s,t,relativePath,typeOfCopy):
    '''copy all the files from the source to the targetdir'''


    src = os.path.join(s, relativePath)
    trg = os.path.join(t, relativePath)
    
    #Create teh folder if doesn't exist 
    if not os.path.isdir(trg): os.mkdir(trg)

    #Seleziona tutti i file della src li copia nella trg sovrascrivendoli
    lista_src = os.listdir(src)

    try:
      for f in lista_src:
        f_path = os.path.join(src,f)
    
        if os.path.isfile(f_path):
          if typeOfCopy =='update':
            if self.hasToBeUpdated(src, trg, f):
              shutil.copy2(f_path, trg)
              ##AGGIORNA
              text_copy='UPDATED '+f_path+' --> \n   '+trg+'\n'
              self.log.writelines(text_copy)
              self.n_file+=1
              print text_copy
              self.n_cop+=1
          
            else: continue

              
          elif typeOfCopy =='replace':
            shutil.copy2(f_path, trg)

            text_copy='COPIED '+f_path+' --> \n   '+trg+'\n'
            self.log.writelines(text_copy)
            self.n_file+=1
            print text_copy
            self.n_cop+=1
          
          
          
        elif os.path.isdir(f_path):
          self.copyFun(src,trg,os.path.basename(f_path),typeOfCopy)
    except: 
      text='An error occurred during the copy: '
      print text+str(sys.exc_info()[1])
      self.log.writelines(text+str(sys.exc_info()[1])+str(sys.exc_info()))
      self.n_err+=1
  
     
  #=============================================================================
  # Says which files have to be updated
  #=============================================================================
  
  def hasToBeUpdated(self, pathS, pathT, f):
    # Compare the DATE of the file in the SOURCE and the TARGET. 
    #If the same, returns False. If different, returns True  
    try:
      if not os.path.isfile(os.path.join(pathT, f)): return False
      
      time_fileSource = os.stat(os.path.join(pathS, f)).st_mtime
      time_fileTarget = os.stat(os.path.join(pathT, f)).st_mtime
    except:
      print 'Error:',f,'not found.'
      self.n_err+=1
      time_fileTarget = 0.0
      
    if time_fileSource == time_fileTarget: return False
    else: return True

  #=============================================================================
  # Update the DLL once copied 
  #=============================================================================

  def updateDLLs(self,nameFile='register_4.0.bat'): #Aggiorna le librerie da register_4.0.bat
    try:
      print '\nDLL are being registered...\n'
      os.chdir(self.dirTarget)
      os.system(nameFile)
    except: print 'Error: register_4.0.bat not found. The DLL have not been registered '
