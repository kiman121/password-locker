#!/usr/bin/env python3.9
from user import User
from credentials import Credentials
import pyperclip


def is_unique_username(username):
    '''
    Function to check if the username is unique
    '''
    return User.is_unique_username(username)


def create_user(fname, lname, username, password):
    '''
    Function that creates a user instance
    '''
    new_user = User(fname, lname, username, password)
    return new_user


def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()


def login(username, password):
    '''
    Function to login a user
    '''
    user_details = User.login_user(username, password)
    return user_details


def create_credentials(user_id, site_name, username, password):
    '''
    Function that creates a credentials instance
    '''
    new_credentials = Credentials(user_id, site_name, username, password)
    return new_credentials


def save_credentials(credentials):
    '''
    Function to save credentials
    '''
    Credentials.save_credentials(credentials)

def has_records(user_id):
    '''
    Function that checks if a user has records
    '''
    return Credentials.has_credentials(user_id)

def display_contacts():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credentials()


def check_existing_credentials(site_name, user_id):
    '''
    Function that check if credentials exist with given site_name
    '''
    return Credentials.credentials_exist(site_name, user_id)


def find_credentials(site_name,user_id):
    '''
    Function that finds credentials by site name and returns the credentials
    '''
    return Credentials.find_credentials_by_site_name(site_name,user_id)


def delete_credentials(credentials):
    '''
    Function to delete credentials
    '''
    Credentials.delete_credentials(credentials)


def copy_site_password(site_name, user_id):
    '''
    Function that copies password for selected site
    '''
    Credentials.copy_credentials(site_name, user_id)

    copied_credentials = pyperclip.paste()

    credential_attributes = {}

    attributes = copied_credentials.split(", ")
    for attribute in attributes:
        credential_attributes[attribute.split(
            ":")[0]] = attribute.split(":")[1]

    return credential_attributes


def autogenerate_password():
    '''
    Function to autogenerate passwords
    '''
    return Credentials.autogenerate_password()


def main():
    '''
    Function that runs the password locker
    '''
    print("Hello, welcome to the most preferred password locker")
    print("How would you like to proceed?")
    print("\n")

    process = True

    while process:
        print("Options: li - login, rg - register, ex - exit")
        user_response = input("Option: ").lower().strip()

        if user_response == 'rg':
            print("\n")
            print("Register new user")
            print("-"*20)
            f_name = input("First name: ").strip()
            l_name = input("Last name: ").strip()
            username = input("Username: ").strip()
            password = input("Password: ").strip()

            is_unique = is_unique_username(username)
            if is_unique:
                save_user(create_user(f_name, l_name, username, password))
                print("\n")
                print("Your locker account has been created. Proceed to login")
                print("\n")
            else:
                print("Username exists")
        elif user_response == 'li':
            print("\n")
            print("Login")
            print("-"*20)

            username = input("Username: ").strip()
            password = input("Password: ").strip()

            user_details = login(username, password)

            print(user_details)

            if user_details != None:
                logged_in_user_id = user_details.username
                print("\n")
                print(f"Welcome {user_details.first_name}")
                while True:
                    
                    print(
                        "Choose action: ac - add credentials, sc - search credentials, dc - display credentials, lo - log out, del - delete credentials, cpy - copy credentials")
                    action = input("Action: ").lower().strip()
                    if action == "ac":
                        user_id = logged_in_user_id
                        site_name = input("Site name: ").lower().strip()
                        user_name = input("Username: ").strip()
                        while True:
                            print(
                                "Password options: ag - autogenerate, ep - enter password")
                            password_option = input("Option: ").lower().strip()
                            if password_option == "ag":
                                pass_word = autogenerate_password()
                                break
                            elif password_option == "ep":
                                pass_word = input("Password: ").strip()
                                break
                            else:
                                print("\n")
                                print(
                                    "Invalid option! Please choose from the provided options.")

                        save_credentials(create_credentials(
                            user_id, site_name, user_name, pass_word))
                        print(
                            f"New credentials for {site_name}|{user_name} added.")
                        print("\n")
                    elif action == "dc":
                        
                        if has_records(logged_in_user_id):
                            print("\n")
                            print("Your credentials:")
                            print("-"*20)

                            count = 1
                            for credentials in display_contacts():
                                if credentials.user_id == logged_in_user_id:
                                    print(f"{count}){credentials.site_name}")
                                    print(
                                        f"   Username: {credentials.username}")
                                    print(
                                        f"   Password: {credentials.password}")

                                    count += 1
                                    print("\n")
                        else:
                            print("\n")
                            print("No credentials to display")
                    elif action == "sc":
                        site_name = input(
                            "Site name to search: ").lower().strip()
                        if check_existing_credentials(site_name, logged_in_user_id):
                            search_credentials = find_credentials(
                                site_name, logged_in_user_id)
                            print(
                                f"Credentials for {search_credentials.site_name}:")
                            print("-"*25)

                            print(f"  Username: {search_credentials.username}")
                            print(f"  Password: {search_credentials.password}")
                            print("\n")
                        else:
                            print("\n")
                            print(f"{site_name} credentials do not exist")
                            print("\n")
                    elif action == "del":
                        site_name_to_delete = input(
                            "Site name to delete: ").lower().strip()
                        if check_existing_credentials(site_name_to_delete, logged_in_user_id):
                            search_credentials = find_credentials(
                                site_name_to_delete, logged_in_user_id)
                            delete_credentials(
                                search_credentials)

                            print(
                                f"{search_credentials.site_name} credentials have been deleted!!")
                                
                            if has_records(logged_in_user_id):
                                print("\n")
                                print("Your credentials:")
                                print("-"*20)

                                count = 1
                                for credentials in display_contacts():
                                    if credentials.user_id == logged_in_user_id:
                                        print(f"{count}){credentials.site_name}")
                                        print(
                                            f"   Username: {credentials.username}")
                                        print(
                                            f"   Password: {credentials.password}")

                                        count += 1
                                        print("\n")
                        else:
                            print("\n")
                            print(
                                f"{site_name_to_delete} credentials do not exist")
                            print("\n")
                    elif action == "cpy":
                        site_name_to_copy = input(
                            "Site name to copy: ").strip().lower()
                        if check_existing_credentials(site_name_to_copy, logged_in_user_id):
                            print("\n")
                            copied_credentials = copy_site_password(
                                site_name_to_copy, logged_in_user_id)

                            print("Copied credentials:")
                            print(
                                f"   Site name: {copied_credentials['site_name']}")
                            print(
                                f"   Username: {copied_credentials['username']}")
                            print(
                                f"   Password: {copied_credentials['password']}")
                            print("\n")
                        else:
                            print("\n")
                            print(
                                f"{site_name_to_copy} credentials do not exist")
                            print("\n")
                    elif action == "lo":
                        print("Logged out: nice having you.")
                        break
                    else:
                        print("\n")
                        print("Invalid action!!")
            else:
                print("\n")
                print("Invalid username or password!!")
        elif user_response == 'ex':
            print("Bye...")
            process = False
        else:
            print("\n")
            print("Invalid option! Please choose from the provided options.")


if __name__ == '__main__':
    main()
