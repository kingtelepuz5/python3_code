import sqlite3
from sqlite3 import  Error

def create_connection(path):
    connecntion = None
    try:
        connecntion = sqlite3.connect(path)
        print("Connection to SQLite DB succesful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connecntion
    
