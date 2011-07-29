'''
Created on Apr 22, 2011

@author: Nicola Di Giorgio

Ver 1.0.4d
'''


#Novita
#Message pop-up with the Alerter


#===DA FARE
#Copia XSmile.doc

#NOTE
#You can use . and .. as you specify the folder
#


import os
import sys
from BinClasses import *


#===============================================================================
# Set the parameters given launching the script 
#===============================================================================
def start():
  args = sys.argv[1:]
  if not args: 
    Main()
  else:
    if args[0] == '--help':
      print "Usage: [-src=source] [-trg=target] [-alertDir=folder1;folder2;... folders for the BinAlerter]"+\
          "[-zipTarget=target for the Zipper] [-transDir=ToBeTranslated folder]"+\
          "[-opt= option: 'copy','zip','alerter','trans'] [-sound=yes|no]"+\
          "[-popup=yes|no] [-delay= delay of the BinAlerter] [-x64=yes|no]"
      
      sys.exit(0)
    
    else:
      source = ''
      target = ''
      dirAlert=''
      zipTarget=''
      transDir=''
      option = ''
      sound=''
      popup=''
      delay=''
      x64=''
      for i in args:
        
        if i[:5] == '-src=': source = i[5:]
        elif i[:5] == '-trg=': target = i[5:]

        elif i[:12] == '-alerterDir=':
          dirAlert = i[12:]
          dirAlert=dirAlert.split(';')

        elif i[:11] == '-zipTarget=':
          zipTarget = i[11:]
          
        elif i[:10] == '-transDir=': transDir = i[10:]
        elif i[:5] == '-opt=': option = i[5:]
        elif i[:7] == '-sound=': sound = i[7:]
        elif i[:7] == '-popup=': popup = i[7:]
        elif i[:7] == '-delay=': delay = i[7:]
        elif i[:5] == '-x64=': x64 = i[5:]
        else:
          if not source: source = i;
          elif not target: target = i;
          elif not dirAlert: dirAlert = i.split(';');
          elif not zipTarget: zipTarget = i;
          elif not transDir: transDir=i;
          elif not option: option = i;
          elif not sound: sound = i;
          elif not popup: popup = i;
          elif not delay: delay = i;
          elif not x64: x64 = i;

    Main(source, target, dirAlert, zipTarget, transDir, option, sound,popup,delay,x64)  
    

if __name__ == '__main__':
  start()


#Main('/home/nicola/eulero', '/home/nicola/Desktop/TEST_BIN', ['/home/nicola/#Desktop/RepManager'], '', '')

