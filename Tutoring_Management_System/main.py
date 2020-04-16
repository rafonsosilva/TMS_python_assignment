from objects import *
from functions import * 
import sqlite3
from contextlib import closing

def main():
    DB_FILE = "C:/Users/rafon/Documents/GBC/COMP2152_Python/Database/tms_database.db"
    conn = sqlite3.connect(DB_FILE)

    main_menu()

        
    
if __name__ == "__main__":
    main()