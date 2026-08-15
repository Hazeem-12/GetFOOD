import hashlib
import os

USER_FILE = "user.txt"


def hash_password(password, salt=None):
    if salt is None:
        salt = os.urandom(16)
    else:
        salt = bytes.fromhex(salt)
    hashed = hashlib.sha256(salt + password.encode()).hexdigest()
    return salt.hex(), hashed


def username_exists(user_name):
    try:
        with open(USER_FILE, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if parts[0] == user_name:
                    return True
    except FileNotFoundError:
        return False
    return False


def sign_up():
    while True:
        user_name = input("Choose a username: ").strip()
        password = input("Enter a password: ")

        if len(user_name) < 5:
            print("Username too short, try again")
        elif username_exists(user_name):
            print("Username already exists, try again")
        else:
            salt, hashed_password = hash_password(password)
            with open(USER_FILE, "a") as file:
                file.write(f"{user_name},{salt},{hashed_password}\n")
            print(f"Welcome {user_name} to getfood")
            break

    proceed = input("Will you like to proceed to login (y/n): ").strip().lower()
    if proceed == "y":
        return login()
    else:
        print("Okay, press enter to go back to main menu")
        return False

def login():
    while True:
        user_login = input("Enter your username: ").strip()
        password_login = input("Enter your password: ")
        try:
            with open(USER_FILE, "r") as file:
                found = False
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    parts = line.split(",")
                    if len(parts) != 3:
                        continue
                    stored_user, stored_salt, stored_hash = parts

                    if stored_user == user_login:
                        found = True
                        new_salt, new_hash = hash_password(password_login, stored_salt)
                        if new_hash == stored_hash:
                            print("Login successful")
                            return user_login
                        else:
                            print("Incorrect password")
                            return False
                if not found:
                    print("Username not found")
                    return False
        except FileNotFoundError:
            print("No users registered yet")
            return False


def main():
    while True:
        print("======= WELCOME =======")
        print("\n1. Sign up")
        print("2. Login")
        print("========================")

        user = input("Enter a choice: ")
        if user == "1":
            sign_up()
            break
        elif user == "2":
            login()
            break
        else:
            print("Invalid input")


if __name__ == "__main__":
    main()