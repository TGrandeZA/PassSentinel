import requests
import sqlite3 
import time 
import schedule 
from create_db import view_table

def check_db_hash(db_hash): #check if each hash is in SHA1 format for API use.
    prefix = db_hash[:5]
    suffix = db_hash[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Error fetching API data.❌")
        return False

    hash_suffixes = (line.split(':')[0] for line in response.text.splitlines())
    return suffix in hash_suffixes

def verify_all_hashes(db_name="password_hashes.db", limit=10): 

    print("Checking for leaks...⏳")
    connection = sqlite3.connect(db_name)
    conn = connection.cursor()

    conn.execute("SELECT hash FROM leaks LIMIT ?", (limit,))
    hashes_to_check = conn.fetchall()

    for (hash_val,) in hashes_to_check:
        leaked = check_db_hash(hash_val)
        if leaked:
            conn.execute("UPDATE leaks SET confirmed_leaks = confirmed_leaks + 1 WHERE hash = ?", (hash_val,)) 
        conn.execute("UPDATE leaks SET status = ? WHERE hash = ?", ('LEAKED ⚠️' if leaked else 'SAFE ✅', hash_val))
        
    connection.commit()
    connection.close()

verify_all_hashes(limit=100) #check all hashed passwords in the database if they've been leaked (Limits it to 100 passwords ).
view_table() #view the database

#Automation. passwords must be verified for leaks every day at 09:00
def job(): 

    verify_all_hashes(limit=100) #check all hashed passwords in the database if they've been leaked (Limits it to 100 passwords ).
    view_table() #view the database

schedule.every().day.at("09:00").do(job)

while True: 
    schedule.run_pending()
    time.sleep(60)


