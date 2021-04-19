#!/usr/bin/python3

# Required library to generate passwords.
import secrets

# Required libary to use password options.
import string

import os, time # import os and time

# Password chars-options:
chars = string.digits + string.ascii_letters + string.punctuation

# block unicode symbol
b = "▁"
s = "            "

# generator function for main file
def generator():
    os.system('clear')
    print(" simplepg – Loading...")
    while True:
        # Waiting for input from user.
        time.sleep(0.640)
        os.system('clear')

        try: 
            userinput = int(input("Please enter the length of your password or 0 for fast mode: "))
            
        # Prints an error if input is invalid.
        except:
            os.system('clear')
            userinput = int(input("Invalid Input. Please enter a number: "))

        if userinput == 0:
            os.system('clear')
            
            for _ in range(5):
                print(''.join(secrets.choice(chars) for _ in range(12)), end="")
                print(s + ''.join(secrets.choice(chars) for _ in range(12)), end="")
                print(s + ''.join(secrets.choice(chars) for _ in range(12)), end="")
                print(s + ''.join(secrets.choice(chars) for _ in range(12)), end="")
                print(s + ''.join(secrets.choice(chars) for _ in range(12)), end="")
                print(s + ''.join(secrets.choice(chars) for _ in range(12)))
                
            
            break   
        
        
        # Prints the generated password and shows the lenth.
        

        os.system('clear')
        time.sleep(0.4)
        print("Generated password " + "(" + str(userinput) + " characters):\n")
        print(b*25)
        print()
        print(''.join(secrets.choice(chars) for _ in range(userinput)) + "\n\n" + b*25 + "\n")
        
        # Prints a rating (in terms of length).
                
        if userinput >=24:
            print("The generated password is very very strong, it is impossible to crack it.")
            
        elif userinput >=8:
            print("The generated password is very secure, and almost impossible to crack.")
        
        elif userinput <=8:
            print("The generated password is very easy to crack, I recommend a length of at least 8 characters.")
        time.sleep(1)
        # ask for exit or resume after first generated password
        exit = input("\nGenerate new password? [y/n]: ")

        # new_pass function
        def new_pass():
            while True:
                time.sleep(0.640)

                try: 
                    userinput = int(input("\n\nLength: ")) 

                except:
                    os.system('clear')
                    userinput = int(input("Invalid Input, try again: "))
                time.sleep(0.4)
                print("Password " + "(" + str(userinput) + " characters):\n")
                print(b*25)
                print()
                print(''.join(secrets.choice(chars) for _ in range(userinput)) + "\n\n" + b*25 + "\n")

                if userinput == 0:
                    print("A password with 0 characters does not exist.")

                elif userinput >=24:
                    print("The generated password is very very strong, it is impossible to crack it.")

                elif userinput >=8:
                    print("The generated password is very secure, and almost impossible to crack.")

                elif userinput <=8:
                    print("The generated password is very easy to crack, I recommend a length of at least 8 characters.")
                # ask for exit or resume after NEXT generated password      
                time.sleep(0.7)
                exit = input("\nGenerate new password? [y/n]: ")
                if exit == "n":
                    time.sleep(0.3)
                    break
                elif exit == "y":
                    new_pass()
                    break
                else:
                    new_pass()
                    break

                
        if exit == "n":
            time.sleep(0.3)
            os.system('clear')
            break
        elif exit == "y":
            os.system('clear')
            new_pass()
            break
        else:
            new_pass()
            break