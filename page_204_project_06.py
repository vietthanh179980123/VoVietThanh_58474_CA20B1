"""
Author: Vo Viet Thanh
Date: 23/10/2021
Program: Add a command to this chapter’s case study program that allows the user to
view the contents of a file in the current working directory. When the command
is selected, the program should display a list of filenames and a prompt for the
name of the file to be viewed. Be sure to include error recovery.
Solution:
    ....
"""
import os, os.path
QUIT='8'
COMMANDS = ('1', '2', '3', '4', '5', '6', '7', '8')
MENU = """1 List the current directory
2 Move up
3 Move down
4 Number of files in the directory
5 Size of the directory in bytes
6 Search for a filename
7 Quit the program"""
def main():
    while True:
        print(os.getcwd())
        print(MENU)
        command = acceptCommand()
        runCommand(command)
        if command == QUIT:
            print("Have a nice day!")
            break
def acceptCommand():
    command = str(input("Enter a number: "))
    if not command in COMMANDS:
        print("Error: command not recognized")
    else:
        return command
def runCommand(command):
    if command == '1':
        print("called listcurrentdir")
        listCurrentDir(os.getcwd())
    elif command == '2':
        print("called moveup")
        moveUp()
    elif command == '3':
        print("called movein")
        moveDown(os.getcwd())
    elif command == '4':
        print("The total number of files is", \
    countFiles(os.getcwd()))
    elif command == '5':
        print("The total number of bytes is", \
        countBytes(os.getcwd()))
    elif command == '6':
        target = input("Enter the search string: ")
        fileList = findFiles(target, os.getcwd())
        if not fileList:
            print("String not found")
        else:
            for f in fileList:
                print(f)
    elif command == 7:
        print("called moveup")
        viewfile(os.getcwd())
def viewfile(dirname):
    lyst=list(filter(os.path.isfile, os.listdir(dirname)))
    if len(lyst)==0:
        print("There are no files in this directory")
    else:
        while True:
            print("Files in" + dirname + ":")
            for element in lyst:
                print(element)
                filename = input("Enter a file name from these names: ")
                if not filename in lyst:
                    print("Sorry, there is a an error in your file name")
                else:
                    f=open(filename,'r')
                    print(f.read)
                    break
def listCurrentDir(dirName):
    lyst = os.listdir(dirName)
    for element in lyst:
        print(element)
def moveUp():
    os.chdir("..")
def moveDown(currentDir):
    newDir = input("Enter the directory name: ")
    if os.path.exists(currentDir + os.sep + newDir) and \
        os.path.isdir(newDir):
        os.chdir(newDir)
    else:
        print("ERROR: no such name")
def countFiles(path):
    count = 0
    lyst = os.listdir(path)
    for element in lyst:
        if os.path.isfile(element):
            count += 1
        else:
            os.chdir(element)
            count += countFiles(os.getcwd())
            os.chdir("..")
    return count
def countBytes(path):
    count = 0
    lyst = os.listdir(path)
    for element in lyst:
        if os.path.isfile(element):
            count += os.path.getsize(element)
        else:
            os.chdir(element)
            count += countBytes(os.getcwd())
            os.chdir("..")
    return count
def findFiles(target, path):
    files = []
    lyst = os.listdir(path)
    for element in lyst:
        if os.path.isfile(element):
            if target in element:
                files.append(path + os.sep + element)
    else:
        os.chdir(element)
        files.extend(findFiles(target, os.getcwd()))
        os.chdir("..")
    return files
if __name__ == "__main__":
    main()
