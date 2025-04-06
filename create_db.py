import sqlite3 
import pandas as pd 

def create_pass_db(db_name = "password_hashes.db"): #database creation 
    connection = sqlite3.connect(db_name)
    conn = connection.cursor()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS leaks (
            hash TEXT PRIMARY KEY
        )
    """)
    connection.commit()
    connection.close()
    print("Database and table created.")

#create_pass_db() ran once

def populate_pass_db(file_path, db_name="password_hashes.db"): #populate the new database with hashed passwords 
    connection = sqlite3.connect(db_name)
    conn = connection.cursor()

    with open(file_path, 'r') as f: 
        for line in f: 
            hash_value = line.strip().upper()
            if len(hash_value) == 40: #basic encryption format validation
                conn.execute("INSERT OR IGNORE INTO leaks (hash) VALUES (?)", (hash_value,))
    connection.commit()
    connection.close()
    print("Database populated.")

#populate_pass_db("password_hashes.txt") ran once

def update_schema(db_name = "password_hashes.db"): #udpate the table to add a column to show how many leaks the hashed password has been in by using the API
    connection = sqlite3.connect(db_name) 
    conn = connection.cursor()

    try: 
        conn.execute("ALTER TABLE leaks ADD COLUMN confirmed_leaks INTEGER DEFAULT 0") 
    except sqlite3.OperationalError:
        print("Column exists")
    connection.commit()
    connection.close()
    print("Column created.")

#update_schema() ran once 

def view_table(db_name="password_hashes.db"): #view the database
    conn = sqlite3.connect(db_name)
    df = pd.read_sql_query("SELECT * FROM leaks", conn)
    conn.close()
    print(df)

view_table() #view the database



    
