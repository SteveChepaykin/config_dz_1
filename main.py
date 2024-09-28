from zipfile import ZipFile, Path as zipPath
import os
import sys
from logger import log;

currentPath = "/";

def cmdclear(*args):
    try:
        os.system('cls')
        log(username, "clear", "SUCCESS")
    except: 
        print("Error in Clear")
        log(username, "clear", "ERROR")

def cmdexit(args):
    try:
        sys.exit("Bye!")
        log(username, "exit", "SUCCESS")
    except SystemExit as message:
        print(message)
        log(username, "exit", "ERROR")

def cmdcd(args):
    global ziparch
    global zipRoot
    try:
        if(len(args) == 0):
            print("Please provide a directory name to change to.")
            log(username, "cd", "NO DIR")
        else:
            nextname = args[0]
            if(nextname == ".."):
                if(zipRoot.at == "home/"):
                    print("You are at the root.")
                    log(username, "cd", "AS ROOT")
                else:
                    zipRoot = zipPath(ziparch, at=str(zipRoot.parent.at));
                    log(username, "cd", "SUCCESS")
            else:
                mem = find_target_dir_in_current(nextname, zipRoot)
                if(mem != None):
                    zipRoot = zipRoot.joinpath(nextname)
                    log(username, "cd", "SUCCESS")
                else: 
                    print("no such directory.")
                    log(username, "cd", "NO DIR")
    except:
        print("Error in CD")
        log(username, "cd", "ERROR")

def cmdls(args):
    global zipRoot
    try:
        get_zipfile_dir_members(zipRoot)
        log(username, "ls", "SUCCESS")
    except:
        print("Error in LS")
        log(username, "ls", "ERROR")
        
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
        arg2 = args[1]
    except:
        print("Requires at least 2 arguments.")
        log(username, "rev", "NO ARGS")
    if arg1 == "-t":
        try:
            print((arg2)[::-1])
            log(username, "rev text", "SUCCESS")
        except:
            print("Error in Rev with Text")
            log(username, "rev text", "ERROR")
    elif arg1 == "-f":
        try:
            zipRoot = zipRoot.joinpath(arg2)
            if zipRoot.exists() and zipRoot.is_file():
                stroki = zipRoot.read_text()
                print(stroki[::-1]) 
                log(username, "rev file", "SUCCESS")
            else:
                print("Cannot reach this file.")
                log(username, "rev file", "NO FILE")
            zipRoot = zipPath(ziparch, at=str(zipRoot.parent.at));
        except:
            print("Error in Rev with File")
            log(username, "rev file", "ERROR")


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