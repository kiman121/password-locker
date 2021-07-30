import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the credentials class behaviours
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        setUp method to run before each test case
        '''
        self.new_credentials = Credentials("mwas2021", "facebook", "mwas", '123')

    def tearDown(self):
        '''
        tearDown method cleans up after every test case run
        '''
        Credentials.credentials_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialised properly
        '''
        self.assertEqual(self.new_credentials.user_id, "mwas2021")
        self.assertEqual(self.new_credentials.site_name,"facebook")
        self.assertEqual(self.new_credentials.username,"mwas")
        self.assertEqual(self.new_credentials.password,"123")
    
    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the credentials object is saved into
        the credentials list
        '''
        # Save the new credentials
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)
    
    def test_save_multiple_credentials(self):
        '''
        test_save_multiple_credentials test case to check if we can save multiple credentials 
        to our credentials_list 
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("dama2021", "twitter", "dama2021", "1234")
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 2)

    def test_find_credentials_by_site_name(self):
        '''
        test_find_credentials_by_site_name test case to check if we can find credentials by site name and display information
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("dama2021", "twitter", "dama2021", "1234")
        test_credentials.save_credentials()

        found_credentials = Credentials.find_credentials_by_site_name("twitter")
        self.assertEqual(found_credentials.user_id, test_credentials.user_id)