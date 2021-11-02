"""
Author: Vo Viet Thanh
Date: 21/10/2021
Program: Gathering Information from a File System
Solution:
    1.Request
    Write a program that allows the user to obtain information about the file system.
    2.Analysis
    File systems are tree-like structures
    At the top of the tree is the root directory (the term “directory” is a synonym for
    “folder,” among users of terminal-based systems). Under the root are files and
    subdirectories. Each directory in the system except the root lies within another
    directory called its parent. For example, in Figure 6-5, the root directory contains
    four files and two subdirectories. On a UNIX-based file system (the system that
    underlies macOS), the path to a given file or directory in the system is a string that
    starts with the / (forward slash) symbol (the root), followed by the names of the
    directories traversed to reach the file or directory. The / (forward slash) symbol also
    separates each name in the path. Thus, the path to the file for this chapter on Ken’s
    laptop might be the following:
    /Users/KenLaptop/Book/Chapter6/Chapter6.doc
    On a Windows-based file system, the \ symbol is used instead of the / symbol.
    The program we will design in this case study is named filesys.py. It provides
    some basic browsing capability as well as options that allow you to search for
    a given filename and find statistics on the number of files and their size in a
    directory. At program startup, the current working directory (CWD) is the directory
    containing the Python program file. The program should display the path of the
    CWD, a menu of command options, and a prompt for a command
    When the user enters a command number, the program runs the command,
    which may display further information, and the program displays the CWD and
    command menu again. An unrecognized command produces an error message,
    and command number 7 quits the program. Table 6-1 summarizes what the commands do.
    3.Design
    You can structure the program according to two sets of tasks: those concerned with
    implementing a menu-driven command processor, and those concerned with executing
    the commands. The first group of operations includes the main function. In the following
    discussion, we work top-down and begin by examining the first group of operations.
    As in many of the programs we have examined recently in this book, the main
    function contains a driver loop. This loop prints the CWD and the menu, calls other
    functions to input and run the commands, and breaks with a signoff message when
    the command is to quit. Here is the pseudocode:
    function main()
    while True
    print(os.getcwd())
    print(MENU)
    command = acceptCommand()
    runCommand(command)
    if command == QUIT
    print("Have a nice day!")
    break
    The function os.getcwd returns the path of the CWD. Note also that MENU and QUIT
    are module variables initialized to the appropriate strings before main is defined.
    The acceptCommand function loops until the user enters a number in the range of the
    valid commands. These commands are specified in a tuple named COMMANDS that is
    also initialized before the function is defined. The function thus always returns a valid
    command number.
    The runCommand function expects a valid command number as an argument. The
    function uses a multi-way selection statement to select and run the operation
    corresponding to the command number. When the result of an operation is returned,
    it is printed with the appropriate labeling.
    That’s it for the menu-driven command processor in the main function. Although there
    are other possible approaches, this design makes it easy to add new commands to
    the program.
    The operations required to list the contents of the CWD, move up, and move down
    are simple and need no real design work. They involve the use of functions in the os
    and os.path modules to list the directory, change it, and test a string to see if it is
    the name of a directory. The implementation shows the details.
    The other three operations all involve traversals of the directory structure in the
    CWD. During these traversals, every file and every subdirectory are visited. Directory
    structure is in fact recursive: each directory can contain files (base cases) and other
    directories (recursive steps). Thus, we can develop a recursive design for each
    operation.
    The countFiles function expects the path of a directory as an argument and
    returns the number of files in this directory and its subdirectories. If there are no
    subdirectories in the argument directory, the function just counts the files and returns
    this value. If there is a subdirectory, the function moves down to it, counts the files
    (recursively) in it, adds the result to its total, and then moves back up to the parent
    directory. Here is the pseudocode:
    function countFiles(path)
    count = 0
    lyst = os.listdir(path)
    for element in lyst
    if os.path.isfile(element)
    count += 1
    else:
    os.chdir(element)
    count += countFiles(os.getcwd())
    os.chdir("..")
    return count
    (continues)
    (continued)
    Copyright 2019 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
    Editorial review has deemed that any suppressed content does not materially affect the overall learning experience. Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.
    Copyright 2019 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part. WCN 02-200-203187
    Design with Recursive Functions
    The countBytes function expects a path as an argument and returns the total number
    of bytes in that directory and its subdirectories. Its design resembles countFiles.
    The findFiles function accumulates a list of the filenames, including their paths, that
    contain a given target string, and returns this list. Its structure resembles the other
    two recursive functions, but the findFiles function builds a list rather than a number.
    When the function encounters a target file, its name is appended to the path, and
    then the result string is appended to the list of files. We use the module variable
    os.sep to obtain the appropriate slash symbol (/ or \) on the current file system.
    When the function encounters a directory, it moves to that directory, calls itself with
    the new CWD, and extends the files list with the resulting list. Here is the pseudocode:
    function findFiles(target, path)
    files = []
    lyst = os.listdir(path)
    for element in lyst
    if os.path.isfile(element):
    if target in element:
    files.append(path + os.sep + element)
    else:
    os.chdir(element)
    files.extend(findFiles(target, os.getcwd()))
    os.chdir("..")
    return files
    The trick with recursive design is to spot elements in a structure that can be treated
    as base cases (such as files) and other elements that can be treated as recursive
    steps (such as directories). The recursive algorithms for processing these structures
    flow naturally from these insights.
    Implementation (Coding)
    ....
"""
import os, os.path
QUIT = '7'
COMMANDS = ('1', '2', '3', '4', '5', '6', '7')
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
    command = input("Enter a number: ")
    if command in COMMANDS:
        return command
    else:
        print("Error: command not recognized")
        return acceptCommand()
def runCommand(command):
    if command == '1':
        listCurrentDir(os.getcwd())
    elif command == '2':
        moveUp()
    elif command == '3':
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
def listCurrentDir(dirName):
    lyst = os.listdir(dirName)
    for element in lyst: print(element)
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