import hashlib
import json
import os
import random
import string

def check_password(password):
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    special_characters = ["!", "@", "#", "$", "%", "^", "&", "*"]
    if not any(char in special_characters for char in password):
        return False
    return True

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def save_password(hashed_password):
    with open("passwords.json", "a+") as file:
        file.seek(0)
        data = file.read()
        if len(data) > 0:
            passwords = json.loads(data)
            if hashed_password in passwords:
                return False
        else:
            passwords = []
        passwords.append(hashed_password)
        file.seek(0)
        file.write(json.dumps(passwords))
    return True

def generate_password():
    length = 8
    all = string.ascii_letters + string.digits + "!@#$%^&*"
    password = "".join(random.sample(all, length))
    while not check_password(password):
        password = "".join(random.sample(all, length))
    return password

while True:
    print("The password must meet the following requirements:")
    print("1. It must contain at least 8 characters")
    print("2. It must contain at least one uppercase letter")
    print("3. It must contain at least one lowercase letter")
    print("4. It must contain at least one digit")
    print("5. It must contain at least one special character(!, @, #, $, %, ^, &, *)")
    password = input("Please entre a password, or entre 'random' to generate a random password: ")
    if password.lower() == 'random':
        password = generate_password()
        print("The generate random password is: ", password)
    if check_password(password):
        hashed_password = hash_password(password)
        if save_password(hashed_password):
            print("The password has been saved.")
            break
        else:
            print("The password already exists, please re-entre.")
    else:
        print("The password does not meet requirements, please re-entre.")
