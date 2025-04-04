import re 
import math 

#check password strength and calculate entropy
def check_password_strength(password): 
    
    #password criteria 
    length_criteria = len(password) >= 12 #length must be atleast 12 characters
    uppercase_criteria = bool(re.search(r'[A-Z]', password)) #atleast 1 uppercase
    lowercase_criteria = bool(re.search(r'[a-z]', password)) #atleast 1 lowercase
    digit_criteria = len(re.findall(r'[0-9]', password)) > 1 # >1 digit
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password)) #atleast 1 special character
    
    #Calculate Entropy
    char_set_size = 0 
    #define possible number of characters for each
    if uppercase_criteria: 
        char_set_size += 26 
    if lowercase_criteria: 
        char_set_size += 26 
    if digit_criteria: 
        char_set_size += 10
    if special_char_criteria: 
        char_set_size += 32

    #(Entropy = LxLog2(N))
    entropy = len(password) * math.log2(char_set_size) if char_set_size > 0 else 0 
    # Classify strength based on entropy
    if entropy > 80:
        strength = "Very Strong"
    elif entropy > 60:
        strength = "Strong"
    elif entropy > 40:
        strength = "Moderate"
    else:
        strength = "Weak"


    #print result 
    print(f"Password Strength: {strength}")
    print(f"Entropy: {entropy:.2f} bits")

    #Password strength recommendations
    print("Recommendations:")
    if not length_criteria: print("- Use at least 12 characters in the password")
    if not uppercase_criteria: print("- Add atleast one uppercase letter in the password")
    if not lowercase_criteria: print("- Add atleast one lowercase letter in the password")
    if not digit_criteria: print("- Include more than one number in the password")
    if not special_char_criteria: print("- Use special characters in the password")

    

#User input
password = input("Enter a password:") 
check_password_strength(password)










    