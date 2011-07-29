import os
import sys
import time
import platform
import ColorConsole
from Util import *
from PrintUtil import *
import shutil
from xml.dom import minidom

NOMEFILE='transFiles.xml'

class ToTranslate(object):
  
  def populateListFile(self):

    try:
      f=open(NOMEFILE)
      xmldoc=minidom.parse(f)
      f.close()

      #Seleziona tutti i file nel tag file
      filesTags=xmldoc.getElementsByTagName('file')

      listFiles=[]
      
      for i in filesTags:
        listFiles.append(i.firstChild.data)
     
    except IOError:
      print 'File '+NOMEFILE+' not found'
      sys.exit(1)
      
    return listFiles


  
  #=============================================================================
  # Set source and target
  #=============================================================================
  
  def __init__(self, source, target, transDir='ToBeTranslated'):
    '''Set the source and the target folder'''
    
    self.dirSource = source
    self.dirTarget = target
    self.dirTrans= transDir
    
    self.ToBeTrans=self.populateListFile()



  #=============================================================================
  # Menu 
  #=============================================================================

  def start(self):

    try:
      
      choice = ''
      
      while not choice in ['y','n']:

        if choice: print ' Error: Input not valid.'; time.sleep(2);
        
        #Clean screen
        if platform.system() == 'Windows':     
          os.system('cls')
        else: os.system('clear')

        print '\nTranslation Tool\n================================='
        print '\nThe tool will copy to the target dir all the bin except for the'+ \
          'files that have to be translated. \nThese files will be placed into the ToBeTranslated folder, instead.\n'

        print '\nSource: ',
        ColorConsole.printC(self.dirSource,'red')
        print '\nTarget: ',
        ColorConsole.printC(self.dirTarget,'red')
        print '\nToBeTranslated folder: ',
        ColorConsole.printC(self.dirTrans,'red')
    
        choice = raw_input('\n\nAre you sure? (y/n) ')
  
        if choice == 'n':

          Util.setNewValue(self,'Source: ',self.dirSource,'dirSource')
          Util.setNewValue(self,'Target: ',self.dirTarget,'dirTarget')
          
          #self.dirTrans=os.path.join(self.dirTarget,
          #                                 os.path.basename(self.dirTrans))
          Util.setNewValue(self,'ToBeTranslated folder: ',self.dirTrans,'dirTrans')

          choice=''

      if not os.path.isdir(self.dirTrans): os.mkdir(self.dirTrans)
      
      self.copyFun(self.dirSource,self.dirTarget,'')
      
      ColorConsole.printC('The files you have to translate are '+str(len(self.ToBeTrans))+'\n',
                          'green')

    except SystemExit: pass
    except: print sys.exc_info()[1],'The program has quit'


  #=============================================================================
  # Replace all the directory
  #=============================================================================

  def copyFun(self,s,t,relativePath):
    '''copy all the files from the source to the targetdir'''

    try:
      src = os.path.join(s, relativePath)
      trg = os.path.join(t, relativePath)

      #Create teh folder if doesn't exist 
      if not os.path.isdir(trg): os.mkdir(trg)
    
      #Seleziona tutti i file della src li copia nella trg sovrascrivendoli
      lista_src = os.listdir(src)

      for f in lista_src:
        f_path = os.path.join(src,f)
    
        if os.path.isfile(f_path):

          if f in self.ToBeTrans:
            
            dest=self.dirTrans
            
          else:
            dest=trg
            
          shutil.copy2(f_path, dest)

          text_copy=f_path+' --> \n   '+dest+'\n'
            
 
          print text_copy
          
        elif os.path.isdir(f_path):
          self.copyFun(src,trg,os.path.basename(f_path))
    except: 
      text='An error occurred during the copy', sys.exc_info()[1]
      print text

#Debug
#ToTranslate(r'\\eidos2nas\Release\4.0\client\Methode\4.5','').start()
