class UserInformation:
    def __init__(self, first_name, last_name, phone_number, password):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.bvn = ""
        self.username = ""
        self.password = password
        self.account_type = ""

    def __str__(self):
        return self.first_name + " " + self.last_name
