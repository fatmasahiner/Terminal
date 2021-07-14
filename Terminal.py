import os
import time

def Intro():
  print("""---------------Şahan Hasret----------------
  ---------------Fatma Şahiner----------------""")
  time.sleep(2)
  print("""Welcome to Linux Easy Terminal
  With this program, you can use linux without knowing the commands.""")
def LinuxUpgrade():
  os.system("sudo apt-get upgrade")
  print("UPGRADE IS COMPLETE")
def LinuxUpdate():
  os.system("sudo apt-get update")
  print("UPDATE IS COMPLETE")
def LinuxInstall(packageName):
  os.system("sudo apt-get install "+ packageName)
  print("PACKAGE IS INSTALL")
def LinuxSudoRemoveEmpty(directory):
  os.system("sudo rm "+directory)
  print("FOLDER IS REMOVE")
def LinuxSudoRemoveNotEmpty(directory):
  directory = input("--Drag and Drop Folder to Terminal--")
  os.system("sudo rm -r "+directory)
def LinuxSudoRemoveFile(fileName):
  fileName = input("--Drag and Drop File to Terminal--")
  os.system("sudo rm "+file)
def GitClone(git):
  os.system("git clone "+git)
def CreateFolder(folder):
  folder = input("Write to Folder Name")
  os.system(folder)
def TurkishKeyboard():
  os.system("setxkbmap tr")

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

  


