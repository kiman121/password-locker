# GitHub Search Web Application
#### A Password locker app where interested users can store their different site login credentials.

#### By **Patrick Mwangangi**
## Description
This a nifty application (runs on a terminal) created to serve as a platform where interested users are able to sign up for a password locker and store their different site login credentials. The application offers capabilities such as viewing (stored credentials), deleting (credentials that are no longer in use), password autogeneration (optional) among others.

Further to the above usage, this master piece was created as practice on concepts learnt in Python (at Moringa School).

## System behavior
For interested users, the application will be able to:
1. Create a new locker account. On creation, the following details will be captured:
    - first_name 
    - last_name
    - username (Check if a username is unique) and 
    - passord 

2. Login a user:
    - authenticate user login credentials (validated username and password)
    - login user if authenticated

3. Create/add existing account credentials. The follwing details will be captured:
    - user_id (be provided after successful login)
    - site name
    - username
    - password (give option to autogenerate or user enters his/her password)

4. Dsiplay a list of a users credentials with the following details:
    - site name
    - username and 
    - password
5. Remove/delete credentials that a user no longer needs

## Setup/Installaction Requirements
- Clone the repository (repo).

    ```
    git clone https://github.com/kiman121/password-locker.git
    ```


- To run the program, open your terminal and navigate to the program files.
- Run "chmod +x run.py" to make the program executable.
- Open the application by running the "./run.py"
- Now the program is up and running and you will get a series of short-codes to assit on decisioning:
    
    1. For new users:
        - They will be required to register before they login
        - The provided options and short codes are: 
            - li - login, 
            - rg - register and 
            - ex - exit.
        - Should one choose to terminate the program, the "ex" option will do the trick!
    2. For successfully loggedin users:
        - They will be able to created/add, delete, copy, search and or view their credentials as they will.
        - The provided options and short codes are: 
            - ac - add credentials, 
            - sc - search credentials, 
            - dc - display credentials, 
            - lo - log out, 
            - del - delete credentials and
            - cpy - copy credentials.
        - The "lo" option allows a user to log out of the system without terminating the program.
        - This means that the same or different user can at that point sigin in an view their details independently.
    3. While creating the credentials, 
        - The user is given an option to key in his/her or allow the system to autogenerate the password.
        - The short codes are: 
            - ag - autogenerate and
            - ep - enter password

## Known Bugs

No Known bugs

## Technology Used
- Python

## Support and contact details

If you want to contact us, email us on info@password-locker.com

### License

[MIT licence](https://github.com/kiman121/password-locker/blob/master/LICENCE)
Copyright (c) 2021 **Password-locker inc**
