# Required library to generate passwords.
import secrets
# Required libary to use password options.

import string
# Password chars-options:
chars = string.digits + string.ascii_letters + string.punctuation

class generator():
    # Waiting for input from user.
    try: 
        userinput = int(input("Please enter the length of the password: \n"))
    # Prints an error if input is invalid.
    except:
        print("Invalid Input. Please enter a number: ")
        userinput = int(input(""))

    # Prints the generated password and shows the lenth.
    print("Generated password is: ")
    print("————————————————————————————————————\n" + ''.join(secrets.choice(chars) for _ in range(userinput)) + "\n\n       (" + str(userinput) + " characters)\n" + "————————————————————————————————————\n\n"
    # Prints a rating (in terms of length).
    + str("Rating:"))
    if userinput == 0:
        print("A password with 0 characters is unfortunately not known to me... -_-")
        
        
    elif userinput >=24:
        print("The generated password is very very strong, it is impossible to crack it. Now you are on the safe side!")
       
    elif userinput >=8:
        print("The generated password is very secure, and almost impossible to crack.")
    
    elif userinput <=8:
        print("The generated password is very easy to crack, " +
        "I recommend a length of at least 8 characters.")
   
