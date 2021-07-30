class Credentials:
    '''
    Class generates new instances of credentials
    '''
    def __init__(self, user_id, site_name, username, password):
        '''
        __init__ method helps in defining properties for the user object.
        Args:
            user_id: New credentials user id.
            site_name : New credentials site name.
            username: New credentials username
            password: New credentials password
        '''
        self.user_id = user_id
        self.site_name = site_name
        self.username = username
        self.password = password