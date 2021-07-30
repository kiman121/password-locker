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
        self.new_user = User("Patrick", "Mwangi", "0722334455", "mwangi@ms.com", "mwas2021",'1234')
    
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
        self.assertEqual(self.new_user.email, "0722334455")
        self.assertEqual(self.new_user.phone_number, "mwangi@ms.com")
        self.assertEqual(self.new_user.username, "mwas2021")
        self.assertEqual(self.new_user.password, '1234')
    
    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
        the user list
        '''
        # Save the new user
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
    
    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user users 
        to our user_list 
        '''
        self.new_user.save_user()
        test_user = User("Damaris", "Mwangangi", "0712345678","dama2021","dama@ms.com","123")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)












    if __name__ == '__main__':
        unittest.main()



# python3 -m unittest test_user.py
