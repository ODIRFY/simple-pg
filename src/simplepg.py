#!/usr/bin/python3

# Required library to generate passwords.
import secrets

# Required libary to use password options.
import string

import os, time # import os and time

# Password chars-options:
chars = string.digits + string.ascii_letters + string.punctuation
    
class generator():
    print("Welcome to simplepg!")
    while True:
        # Waiting for input from user.
        time.sleep(0.640)
        os.system('clear')

        try: 
            userinput = int(input("Please enter the length of the password: \n"))
        # Prints an error if input is invalid.
        except:
            print("Invalid Input. Please enter a number: ")
            userinput = int(input(""))

        # Prints the generated password and shows the lenth.
        os.system('clear')
        time.sleep(1)
        print("Generated password is: ")
        print("————————————————————————————————————\n" + ''.join(secrets.choice(chars) for _ in range(userinput)) + "\n\n       (" + str(userinput) + " characters)\n" + "————————————————————————————————————\n\n"
        
        # Prints a rating (in terms of length).
        + str("Rating: "), end="")
        
        if userinput == 0:
            print("A password with 0 characters does not exist.")
            
            
        elif userinput >=24:
            print("The generated password is very very strong, it is impossible to crack it.")
        
        elif userinput >=8:
            print("The generated password is very secure, and almost impossible to crack.")

        elif userinput <=8:
            print("The generated password is very easy to crack, " +
            "I recommend a length of at least 8 characters.")
        
        # ask for exit or resume
        exit = input("\n——\nPress Enter to resume, or type 'q' for exit. ")

        if exit == "q":
            os.system('clear')
            time.sleep(0.2)
            print("Exit!")
            time.sleep(0.4)
            os.system('clear')
            break