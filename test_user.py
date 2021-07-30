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

    def test_find_user_by_username(self):
        '''
        test_find_user_by_username test case to if we find a user by username and display information
        '''
        self.new_user.save_user()
        test_contact = User("Liam", "Nyamu", "liam2021", "12345")
        test_contact.save_user()

        found_user = User.find_user_by_username("liam2021")
        self.assertEqual(found_user.first_name, test_contact.first_name)

    if __name__ == '__main__':
        unittest.main()


# python3 -m unittest test_user.py
