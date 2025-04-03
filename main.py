import re 
import math 

#check password strength and calculate entropy
def check_password_strength(password): 
    
    #Check password criteria 
    length_criteria = len(password) >= 12 
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    digit_criteria = bool(re.search(r'/d', password)) 
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password)) 

    #Calculate Entropy (Entropy = LxLog2(N))
    char_set_size = 0 
    if uppercase_criteria: 
        char_set_size += 26 
    if lowercase_criteria: 
        char_set_size += 26 
    if digit_criteria: 
        char_set_size += 10
    if special_char_criteria: 
        char_set_size += 32

    entropy = len(password) * math.log2(char_set_size) if char_set_size > 0 else 0 
    if length_criteria and uppercase_criteria and lowercase_criteria and digit_criteria and special_char_criteria:
        strength = "Very Strong"
    elif length_criteria and (uppercase_criteria + lowercase_criteria + digit_criteria + special_char_criteria >= 3):
        strength = "Strong"
    elif length_criteria and (uppercase_criteria + lowercase_criteria + digit_criteria + special_char_criteria >= 2):
        strength = "Moderate"
    else:
        strength = "Weak"

    #print result 
    print(f"Password Strength: {strength}")
    print(f"Entropy: {entropy:.2f} bits")

    #Password strength suggestions
    print("Recommendations:")
    if not length_criteria: print("- Use at least 12 characters!")
    if not uppercase_criteria: print("- Add uppercase letters!")
    if not lowercase_criteria: print("- Add lowercase letters!")
    if not digit_criteria: print("- Include numbers!")
    if not special_char_criteria: print("- Use special characters (!@#$%^&*)!")

password = input("Enter a password:") 
check_password_strength(password)




    