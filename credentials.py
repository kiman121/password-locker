from os import stat
import pyperclip
import string
import secrets

class Credentials:
    '''
    Class generates new instances of credentials
    '''
    credentials_list = []

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

    def save_credentials(self):
        '''
        save_credentials method saves credentials objects into credentials list
        '''
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        '''
        delete_credentials method deletes saved credentails from the credentails_list
        '''
        Credentials.credentials_list.remove(self)

    @classmethod
    def find_credentials_by_site_name(cls, site_name,user_id):
        '''
        find_credentials_by_site_name method takes in a site name and returns 
        credentials that match the site name
        Args:
            site_name: site name to search for
        Returns:
            credentials that match the site name
        '''
        for credentials in cls.credentials_list:
            if credentials.site_name == site_name and credentials.user_id == user_id:
                return credentials

    @classmethod
    def credentials_exist(cls, site_name, user_id):
        '''
        Method that checks if credentials exists
        Args:
            site_name: Site name to search if it exists
        Returns:
            Boolean: True or false if credentials exist
        '''
        status = False
        if len(cls.credentials_list) > 0:
            for credentials in cls.credentials_list:
                if credentials.site_name == site_name and credentials.user_id == user_id:
                    status = True         
        return status

    @classmethod
    def has_credentials(cls, user_id):
        '''
        Method that checks if user has credentials
        Args:
            user_id: user id to search if it exists
        Returns:
            Boolean: True or false if credentials exist
        '''
        status = False
        if len(cls.credentials_list) > 0:
            for credentials in cls.credentials_list:
                if credentials.user_id == user_id:
                    status = True         
        return status


    @classmethod
    def display_credentials(cls):
        '''
        Method that returns the contact list
        '''
        return cls.credentials_list

    @classmethod
    def copy_credentials(cls, site_name, user_id):
        '''
        Method that copies the matched credentials
        Args:
            site_name: Site name to match
        Return:
            Matched credentials
        '''
        matched_credentials = cls.find_credentials_by_site_name(site_name, user_id)
        pyperclip.copy("site_name:"+matched_credentials.site_name + ", username:" +
                       matched_credentials.username+", password:"+matched_credentials.password)

    def autogenerate_password():
        '''
        Method to autogenerate passwords
        '''
        str = string.ascii_letters + string.digits
        return ''.join(secrets.choice(str) for i in range(10))