import unittest

from unIpass_main import password_options


class TestGenerator(unittest.TestCase):
    """Test case for generator function"""

    def test_length(self):
        """Tests it comes up with the n length"""
        result = password_options.generator(17)

        self.assertEqual(len(result), 17)


class TestGetPassword(unittest.TestCase):
    """Test case for get_password"""

    def setUp(self):    # TODO: Might be able to not need this
        """Setting up the dictionary variable"""
        self.dictionary = {'bank': 'ABC', 'insta': 'DEF', 'face': 'GHI'}

    def test_get_password_gets_password(self):
        """Tests that it finds a password when the account is in dictionary"""
        result = password_options.get_password('bank', self.dictionary)

        self.assertEqual(result, 'ABC')

    def test_case_sensitivity(self):
        """Tests that it ignores case of account_name"""
        result = password_options.get_password('BANK', self.dictionary)

        self.assertEqual(result, 'ABC')

    def test_get_password_wont_get_password(self):
        """Tests that it will return a message if password isn't in dictionary"""
        result = password_options.get_password('spam', self.dictionary)

        self.assertIsNone(result)



