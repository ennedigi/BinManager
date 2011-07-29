import os
import sys
import time
import platform
import ColorConsole

import TkinterDialog

from Util import *


class PrintUtil(object):
  sound=False
  popup=False

#===============================================================================
# Print the list with the file updated
#===============================================================================

  @staticmethod
  def printListCompare(dir, list_dir1, list_dir2, n=5):
    
    try:
      #Create dictionaries: filename -> modified date
      d_1={}
          
      for i in list_dir1:
        d_1[i[0]]=i[1]
      
      print '\n\nThe most recent files in ',
      ColorConsole.printC(dir,'red')
      print ' are:',
      
      for i in enumerate(list_dir2[:n]):
        try: 
          if i[1][1]!=d_1[i[1][0]]:
            #number - filename - modified data
            print '\n\t{0} {1:35s} '.format(i[0]+1,os.path.basename(i[1][0])),
            ColorConsole.printC(time.ctime(i[1][1]),'green')
          else:
            print '\n\t{0} {1:35s} {2}'.format(i[0] + 1,os.path.basename(i[1][0]), time.ctime(i[1][1])),
        except: print '\n\t{0} {1:35s} {2}'.format(i[0] + 1,os.path.basename(i[1][0]), time.ctime(i[1][1])),
      
    except: print 'Error',sys.exc_info()[1]
    


  #=============================================================================
  # Print the most recent files
  #=============================================================================

  @staticmethod
  def printListCompare2(dir1, dir2, n=5):
    
    try:
      list_source=Util.mostRecentFiles(dir1)
      
      list_target=Util.mostRecentFiles(dir2)
      


      #Create dictionaries: filename -> modified date
      d_target={}
      
      if list_target:
        for i in list_target:
          d_target[i[0]]=i[1]
        
      print '\n\nThe most recent files in ',
      ColorConsole.printC(dir1,'red')
      print ' are:',
      
      for i in enumerate(list_source[:n]):

        try:
        
          if i[1][1]!=d_target[i[1][0]]:
          #number - filename - modified data
            print '\n\t{0} {1:35s} '.format(i[0]+1,os.path.basename(i[1][0])),
            ColorConsole.printC(time.ctime(i[1][1]),'green')
            
          else:
            print '\n\t{0} {1:35s} {2}'.format(i[0] + 1,os.path.basename(i[1][0]), time.ctime(i[1][1])),
            
        except KeyError: print '\n\t{0} {1:35s} {2}'.format(i[0] + 1,os.path.basename(i[1][0]), time.ctime(i[1][1])),
      
      
      if list_target!=[]:
        print '\n\nThe most recent files in ',
        ColorConsole.printC(dir2,'red')
        print ' are:',
        
        for i in enumerate(list_target[:n]):     
          print '\n\t{0} {1:35s} {2}'.format(i[0] + 1, os.path.basename(i[1][0]), time.ctime(i[1][1])),
      else: 
        print '\n\n',
        ColorConsole.printC(dir2,'red')
        print 'is empty'

        
    except: print 'Error' #, sys.exc_info()[1]



  @staticmethod
  def printListCompareUpdate(lista_dir1, dir2, n=5):

    isChanged=False
    
    try:
      
      lista_dir2=Util.mostRecentFiles(dir2)

      #Create dictionaries: filename -> modified date
      d_2={}
      
      for i in lista_dir2:
        d_2[i[0]]=i[1]


     
      for i in lista_dir1:

        if d_2[i[0]]!=i[1]:
  
          isChanged=True;
          break
        else: pass

      if isChanged:
    
        if PrintUtil.sound: 

          platform_pc=platform.system()
          if platform_pc == 'Windows':     
            import winsound
            winsound.Beep(420, 1000)

        print '\n\n===================================='
        print 'UPDATE ',time.ctime(time.time())
        print '===================================='

        PrintUtil.printListCompare(dir2,lista_dir1,lista_dir2,n)
        print

        if PrintUtil.popup:
          TkinterDialog.showMessage('BinAlert','The folder '+dir2+' has changed!')

        return lista_dir2

      return []

    except: print 'Error',sys.exc_info()[1]


###############
  @staticmethod
  def printListOneDir(dir1, n=5):
      
    try:
      list_dir1=Util.mostRecentFiles(dir1)
        
      #STAMPA SOLO I FILE AGGIORNATI 
      print '\n\nThe most recent files in ',
      ColorConsole.printC(dir1,'red')
      print ' are:',
        
      for i in enumerate(list_dir1[:n]):
        print '\n\t{0} {1:35s} {2}'.format(i[0] + 1, os.path.basename(i[1][0]), time.ctime(i[1][1])),
          
    except: print 'Error!'

    return list_dir1

