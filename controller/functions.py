from exception.exceptions import UserNotFoundException
from models.accounts import IndividualAccount
from models.information import UserInformation
import json

user_data_file = open("../user_data.json", "r+")

user_data_file_content = json.load(user_data_file)


# def check_string(string):
#     while True:
#         input_string = input(string)
#         if input_string != "":
#             return input_string
#         else:
#             print("Enter a valid input.")

def print_error(err):
    print("\033[91m" + str(err) + "\033[0m")


def check_string(string):
    while True:
        try:
            print()
            input_string = input(string)
            if input_string != "":
                return input_string
            else:
                raise ValueError("Invalid input, try again!")
        except ValueError as err:
            print_error(err)


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
    return bool(bvn.startswith("4"))


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


def get_user(user_id):
    index = -1
    for user in user_data_file_content["user_data"]:
        index += 1
        if user_id == user["id"]:
            return user, index
    raise UserNotFoundException(f"User with id = {user_id} does not exist in our record")


def get_all_user():
    return user_data_file_content["user_data"]


def update_user(user_id, first_name="", last_name="", phone_number=""):
    try:
        user, index = get_user(user_id)
        if first_name != "" and first_name != user["first_name"]:
            user["first_name"] = first_name
        if last_name != "" and last_name != user["last_name"]:
            user["last_name"] = last_name
        if phone_number != "" and phone_number != user["phone_number"]:
            user["phone_number"] = phone_number

        user_data_file_content['user_data'][index] = user

        user_data_file.seek(0)

        json.dump(user_data_file_content, user_data_file, indent=4)

        user_data_file.close()
    except UserNotFoundException as err:
        print_error(err)


print(get_user(4))

update_user(4, "John")
