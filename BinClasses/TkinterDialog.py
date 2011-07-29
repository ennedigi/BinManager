from tkMessageBox import showwarning
from Tkinter import Tk

def showMessage(title,text):

  root=Tk()
  root.withdraw()

  showwarning(title,text)
