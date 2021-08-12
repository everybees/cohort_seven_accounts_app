class IndividualAccount():
    def __init__(self, account_owner, account_number, account_type, account_balance, pin):
        self.account_owner = account_owner
        self.account_number = account_number
        self.account_type = account_type
        self.account_balance = account_balance
        self.pin = pin

    def __str__(self):
        return self.account_number

        #lovie
