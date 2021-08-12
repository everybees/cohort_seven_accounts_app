from models.accounts import IndividualAccount
from models.information import UserInformation
import json

# user data
user_data_file = open("user_data.json", "r+")

user_data_file_content = json.load(user_data_file)


def check_string(string):
    while True:
        input_string = input(string)
        if input_string != "":
            return input_string
        else:
            print("Enter a valid input.")


def create_user():
    first_name = check_string("Enter your first name: ")
    last_name = check_string("Enter your last name: ")
    phone_number = check_string("Enter your phone number: ")
    password = check_string("Enter your password: ")

    user = UserInformation(first_name, last_name, phone_number, password)

    user_object = {
        "id": len(user_data_file_content) + 1,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "phone_number": user.phone_number,
        "password": user.password,
        "username": user.username,
        "bvn": user.bvn,
        "account_type": user.account_type
    }

    user_data_file_content['user_data'].append(user_object)

    user_data_file.seek(0)

    json.dump(user_data_file_content, user_data_file, indent=4)

    user_data_file.close()


def check_bvn_valid(bvn):
    if bvn.startswith("4"):
        return True
    else:
        return False


def user_request_for_account(phone_number, account_type, bvn, username):
    print(user_data_file_content)

    for user_data in user_data_file_content:
        if phone_number == user_data['phone_number']:
            bvn_valid = check_bvn_valid(bvn)
            user_data['username'] = username
            user_data['account_type'] = account_type
            user_data['bvn'] = bvn

            user_data_file.seek(0)
            json.dump(user_data_file_content, user_data_file, indent=4)
            user_data_file.close()

            if bvn_valid and account_type != "":
                if account_type == "individual_account":
                    user_account = IndividualAccount(user_data, "0000001", "individual_account", 0.00, "1234")

