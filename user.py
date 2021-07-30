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
    def find_user_by_username(cls, username):
        '''
        find_user_by_username method get a user based on provided username
        Args:
            username: user's username to search for
        Returns:
            user details that match the username
        '''
        for user in cls.user_list:
            if user.username == username:
                return user




    


