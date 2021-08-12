import unittest

from models.information import UserInformation


class BankTest(unittest.TestCase):
    
    def test_individual_account_request(self):
        first_name = "John"
        last_name = "Doe"
        phone_number = "08097685743"
        bvn = "43454566763456"

        user_account_details = UserInformation(
            first_name, last_name, phone_number, bvn
        )

        self.assertEqual(user_account_details.account_type, "individual_account")
        self.assertEqual(user_account_details.bvn.startswith('4'), True)
        self.assertEqual(len(user_account_details.bvn) == 14, True)
        self.assertEqual(type(user_account_details.first_name) is str, True)
        self.assertEqual(type(user_account_details.last_name) is str, True)
