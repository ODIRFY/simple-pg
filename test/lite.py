import secrets, string
chars = string.digits + string.ascii_letters + string.punctuation
uinput = int(input("Enter length: "))
print(''.join(secrets.choice(chars) for _ in range(uinput)))