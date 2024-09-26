import os

def cmdclear(*args):
    try:
        os.system('cls')
    except: 
        print("Error in Clear")