import os
import time

class Commands(dict):
    def __init__(self,com):
        self.com = com
        self.message = os.popen(com).readlines()

    def __repr__(self):
       self.__setitem__('cmd', self.foo)
       self.__setitem__('output', self.bar)
       return super().__repr__()

def Intro():
  print("""---------------Şahan Hasret----------------
  ---------------Fatma Şahiner----------------
  ----------------Emir Öztürk-----------------""")
  time.sleep(2)
  print("""Welcome to Linux Easy Terminal
  With this program, you can use linux without knowing the commands.""")
def LinuxUpgrade():
  for msg in Commands("sudo apt-get upgrade").message:
     print(msg)
  print("UPGRADE IS COMPLETE")
def LinuxUpdate():
  for msg in Commands("sudo apt-get update").message:
     print(msg)
  print("UPDATE IS COMPLETE")
def LinuxInstall(packageName):
  for msg in Commands("sudo apt-get install "+ packageName).message:
     print(msg)
  print("PACKAGE IS INSTALL")
def LinuxSudoRemoveEmpty(directory):
  Commands("sudo rm "+directory)
  print("FOLDER IS REMOVE")
def LinuxSudoRemoveNotEmpty(directory):
  directory = input("--Drag and Drop Folder to Terminal--")
  Commands("sudo rm -r"+directory)
  print("FOLDER IS REMOVE")
def LinuxSudoRemoveFile(fileName):
  fileName = input("--Drag and Drop File to Terminal--")
  Commands("sudo rm "+fileName)
  print("FILE IS REMOVE")
def GitClone(git):
  for msg in Commands("git clone "+git).message:
     print(msg)
def CreateFolder(folder):
  folder = input("Write to Folder Name")
  Commands("mkdir "+folder)
def TurkishKeyboard():
  Commands("setxkbmap tr")
  print("KEYBOARD TR")

#--------------------------------------------------

Intro()
choice = input("""
Choice:
1. Update
2. Upgrade 
3. Turkish Keyboard Set
4. Package Installer
""")

if choice == "1":
    LinuxUpdate()
if choice == "2":
    LinuxUpgrade
if choice == "3":
    TurkishKeyboard()
if choice == "4":
  packageName = input("Package Name: ")
  LinuxInstall(packageName)
if choice == "5":
  git = input("Copy And Paste GitHub Link")
  GitClone(git)

  


