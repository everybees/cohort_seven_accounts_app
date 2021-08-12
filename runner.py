from controller import functions


if __name__ == "__main__":
    message = """
            Welcome to Lovers Bank
Register with us,Kindly provide your details below
    """
    print(message)
    functions.create_user()
    message = """
    Do you want to create an account with us?
    type yes to proceed
    type no to cancel
    """
    user_input = input(message)

    if user_input == "yes":
        functions.user_request_for_account()
    else: 
        exit()
