import os
import sys
import time
import platform
import ColorConsole


class Util(object):

  #Funzione per avere sempre due cifre ogni campo della data

  @staticmethod
  def twoDigits(string):
    if len(string)==1:
      return '0'+string
    else: return string

  #Trasforma una tupla in una stringa con ogni campo di lunghezza di almeno due cifre

  @staticmethod
  def tupleToStr(tupl):
    output=''
    for i in tupl:
      output+=Util.twoDigits(str(i))
    return output

  #=============================================================================
  # List the n-most recent files of the folder
  #=============================================================================

  @staticmethod
  def mostRecentFiles(dir, relativePath=''):
    f_list = []
    path=os.path.join(dir,relativePath)
    listdir = os.listdir(path)
    
    for f in listdir:
      f_path=os.path.join(path,f)
      
      if os.path.isfile(f_path):
        modTime = round(os.stat(f_path).st_mtime)
        f_list.append((os.path.join(relativePath,f), modTime)) #add the tuple
        
      elif os.path.isdir(f_path):
        f_list.extend(Util.mostRecentFiles(dir,os.path.join(relativePath,f))) #extend the list
                                                                

    f_list = sorted(f_list, key=lambda f_list: f_list[1], reverse=True)
    
    return f_list


  @staticmethod
  def setNewValue(obj,nameValue,oldValue,attrbName,checkIsADir=True):

    while True:
      print nameValue,
      ColorConsole.printC(oldValue,'red')
      temp = raw_input('\nEnter the new (if any): ',)

      if checkIsADir: #Sometimes the input is not a folder
        if not os.path.isdir(temp):
          if temp:
            if os.path.isdir(os.path.dirname(temp)):
              os.mkdir(temp)
              break
            else: print ' Error: Input not valid.'; time.sleep(2)
          else: temp=oldValue; break # temp=''

        else: break

      else: temp=oldValue; break

    setattr(obj,attrbName,temp)
