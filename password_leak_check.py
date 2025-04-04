import hashlib 
import requests 



def check_password_pwned(password): 
    sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper() #encrypts password using secure hash algorithm 1 (SHA1 required to use the API)
    prefix, suffix = sha1_hash[:5], sha1_hash[5:] 

    url = f"https://api.pwnedpasswords.com/range/{prefix}" #requests to the URL uses the first 5 characters in the hashed password
    response = requests.get(url)

    if response.status_code == 200: #returns a list of leaked passwords that match the first 5 hashes of the password entered
        hashes = (line.split(":") for line in response.text.splitlines())
        for h, count in hashes: 
            if h == suffix: #loops through the lists of given SHA1 hashed passwords, and finds the password that matches the has password entered.
                print(f"Warning: Your password has been found in {count} breaches! Please change your password now.")
                return 
    print("Your password has not been found in any breaches")


password = input("Enter your password again, to check for a possible leak:")
check_password_pwned(password)




    