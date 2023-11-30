import psycopg2
import pandas as pd

def getConn():
    #function to retrieve the password, construct
    #the connection string, make a connection and return it.
    #The pw.txt file will have the password to access the PGAdmin given to you by Russell Smith
    pwFile = open("pw.txt", "r")
    pw = pwFile.read();
    pwFile.close()


def clearOutput():
    with open("output.txt", "w") as clearfile:
        clearfile.write('')
        

def clearOutput():
    with open("output.txt", "w") as clearfile:
        clearfile.write('')
        

def writeOutput(output):
    with open("output.txt", "a") as myfile:
        myfile.write(output)


