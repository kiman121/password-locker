import unittest
from user import User


class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        setUp method to run before each test case
        '''
        self.new_user = User("Patrick", "Mwangi", "mwas2021", '1234')

    def tearDown(self):
        '''
        tearDown method cleans up after every test case run
        '''
        User.user_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialised properly
        '''
        self.assertEqual(self.new_user.first_name, "Patrick")
        self.assertEqual(self.new_user.last_name, "Mwangi")
        self.assertEqual(self.new_user.username, "mwas2021")
        self.assertEqual(self.new_user.password, '1234')

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
        the user list
        '''
        # Save the new user
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user users 
        to our user_list 
        '''
        self.new_user.save_user()
        test_user = User("Damaris", "Mwangangi", "dama2021", "123")
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)

    def test_is_unique_username(self):
        '''
        test_is_unique_username test case to check if a username exists (boolean)
        '''
        self.new_user.save_user()

        is_unique_username = User.is_unique_username("liam2021")
        self.assertTrue(is_unique_username)

    def test_login_user(self):
        '''
        test_login_user test case to check if a user is successfuly logged in
        '''
        self.new_user.save_user()
        test_user = User("Grace", "Kakwasi", "grace2021", "12")
        test_user.save_user()

        logged_in_user = User.login_user("grace2021","12")
        self.assertEqual(logged_in_user.first_name, test_user.first_name)

    

    if __name__ == '__main__':
        unittest.main()

