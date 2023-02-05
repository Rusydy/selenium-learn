import unittest

# Import the class to be tested
import Person as PersonClass # this import is case sensitive and must be the same as the file name

class Testing(unittest.TestCase):
    person = PersonClass.Person()
    user_id = []
    user_name = []

    # test case function to check the Person.set_name function
    def test_0_set_name(self):
        print('Start test_0_set_name')

        for i in range(8):
            # initialize a name
            user_name = 'user_{}'.format(i)

            # store the name into the list variable
            self.user_name.append(user_name)

            # get the user name from the Person class
            user_id = self.person.set_name(user_name)

            # check if the obtained user id is null or not
            self.assertIsNotNone(user_id)

            # store the user id to the list variable
            self.user_id.append(user_id)

        print("user_id length = ", len(self.user_id))
        print(self.user_id)
        print("user_name length = ", len(self.user_name))
        print(self.user_name)
        print("\nFinish set_name test\n")

    # test case function to check the Person.get_name function
    def test_1_get_name(self):
        print('Start test_1_get_name')

        length = len(self.user_id)  # total number of stored user information

        for i in range(length):
            if i < length:
                self.assertEqual(self.person.get_name(self.user_id[i]), self.user_name[i])
            else:
                self.assertEqual(self.person.get_name(i), 'There is no such user')
        
        print("\nFinish get_name test\n")

if __name__ == '__main__':
    unittest.main()

# Reference
# https://www.digitalocean.com/community/tutorials/python-unittest-unit-test-example