from datetime import datetime
import csv

def log(uname, command, status):
    with open("logger.csv", 'a', newline='') as logFile:
        spamwriter = csv.writer(logFile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([datetime.now(), uname, command, status])