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
        Credentials.user_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialised properly
        '''
        self.assertEqual(self.new_credentials.user_id, "mwas2021")
        self.assertEqual(self.new_credentials.site_name,"facebook")
        self.assertEqual(self.new_credentials.username,"mwas")
        self.assertEqual(self.new_credentials.password,"123")