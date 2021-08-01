class User:
    '''
    Class that generates new instances of a users
    '''
    user_list = []

    def __init__(self, first_name, last_name, username, password):
        '''
        __init__ method helps in defining properties for the user object.
        Args:
            first_name: New user first name.
            last_name : New user last name.
            email : New user email address.
            phone_number: New user phone number.
            username: New user username
            password: New user password
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
    
    def save_user(self):
        '''
        save_user method saves user objects into user_list list
        '''
        User.user_list.append(self)

    @classmethod
    def is_unique_username(cls, username):
        '''
        is_unique_username method to check if a username is unique
        Args:
            username: user's username to search for
        Returns:
            Boolean: True or false depending on if a username exists or not
        '''
        if len(cls.user_list) > 0:
            for user in cls.user_list:
                if user.username == username:
                    return False
                else:
                    return True
        else:
            return True
            
    @classmethod
    def login_user(cls, username, password):
        '''
        login_user method gets a user based on given username and password
        Args:
            username: user's username to search and match password
            password: user provided password
        Returns:
            user details that match the username and password provided
        '''
        for user in cls.user_list:
            if user.username == username and user.password == password:
                return user

    


