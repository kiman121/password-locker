#!/usr/bin/env python3.9
from user import User
from credentials import Credentials

def is_unique_username(username):
    '''
    Function to check if the username is unique
    '''
    return User.is_unique_username(username)

def create_user(fname,lname,username,password):
    '''
    Function that creates a user instance
    '''
    new_user = User(fname,lname,username,password)
    return new_user

def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()

def main():
    '''
    Function that runs the password locker
    '''
    print("Hello, welcome to the most preferred password locker")
    print("How would you like to proceed?")
    print("\n")

    while True:
        print("li - login, rg - register")
        user_response = input().lower()

        if user_response == 'rg':
            print("Register new user")
            print("-"*20)
            f_name = input("First name: ")
            l_name = input("Last name: ")
            username = input("Username: ")
            password = input("Password: ")
            
            is_unique = is_unique_username(username)
            if is_unique:
                save_user(create_user(f_name,l_name,username,password))
                print("\n")
                print("Your locker account has been created. Proceed to login")
                print("\n")
            else:
                print("Username exists")
        elif user_response == 'li':
            print("Login")
            print("-"*20)
            username = input("Username: ")
            password = input("Password: ")


        else:
            print("Invalid shortcode. Please use the short codes")

if __name__ == '__main__':
    main()