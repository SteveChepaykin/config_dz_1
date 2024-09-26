from zipfile import ZipFile, Path as zipPath
import os
import sys

currentPath = "/";

def getLastDirInPath():
    if(currentPath == "home/"):
        return "home"
    i = currentPath[:-1].rfind("/")
    res = currentPath[(i+1):-1]
    return res


def cmdexit(args):
    try:
        sys.exit("Bye!")
    except SystemExit as message:
        print(message)

def cmdcd(args):
    global ziparch
    global zipRoot
    try:
        if(len(args) == 0):
            print("Please provide a directory name to change to.")
        else:
            nextname = args[0]
            if(nextname == ".."):
                if(zipRoot.at == "home/"):
                    print("You are at the root.")
                else:
                    zipRoot = zipPath(ziparch, at=str(zipRoot.parent.at));
            else:
                mem = find_target_dir_in_current(nextname, zipRoot)
                if(mem != None):
                    zipRoot = zipRoot.joinpath(nextname)
                else: 
                    print("no such directory.")
    except:
        print("Error in CD")

def cmdls(args):
    global zipRoot
    try:
        get_zipfile_dir_members(zipRoot)
    except:
        print("Error in LS")
        
def find_target_dir_in_current(target_dir_name, root):
    for member in root.iterdir():
        if member.is_dir():
            if(member.name == target_dir_name):
                return member

def get_zipfile_dir_members(root):
        for file_name in root.iterdir():
            print(f'{file_name.name}')

def cmdrev(args):
    global zipRoot
    global ziparch
    try:
        arg1 = args[0];
    except:
        print("Requires at least 2 arguments.")
    if arg1 == "-t":
        try:
            print((args[1])[::-1])
        except:
            print("Error in Rev with Text")
    elif arg1 == "-f":
        try:
            zipRoot = zipRoot.joinpath(args[1])
            if zipRoot.exists() and zipRoot.is_file():
                stroki = zipRoot.read_text()
                print(stroki[::-1]) 
            else:
                print("Cannot reach this file.")
            zipRoot = zipPath(ziparch, at=str(zipRoot.parent.at));
        except:
            print("Error in Rev with File")

def cmdclear(*args):
    try:
        os.system('cls')
    except: 
        print("Error in Clear")



hostname, username, zipname = input("Enter host, user, zip for file system: ").split()

commands = [["ls", cmdls], ["cd", cmdcd], ["exit", cmdexit], ["rev", cmdrev], ["clear", cmdclear]]
with ZipFile(zipname, 'r') as ziparch:
    zipRoot = zipPath(ziparch).joinpath("home")

    while True:
        line = input(f"{username}@{hostname}#{zipRoot.filename} ")
        splitted = line.split(" ")

        cmd = list(filter(lambda a: a[0] == splitted[0], commands))
        if len(cmd) == 0:
            print("Unknown command!")
            continue
        cmd = cmd[0]
        if cmd[1] == None:
            print("Unimplemented command!")
            continue
        if cmd[0] == "exit":
            cmdexit(splitted[1:])
            break
        cmd[1](splitted[1:])