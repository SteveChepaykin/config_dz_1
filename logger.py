from datetime import datetime

def log(uname, command, status):
    with open("logger.txt", 'a') as logFile:
        logFile.write(f"({datetime.now()}) {uname}: {command}, {status}\n");