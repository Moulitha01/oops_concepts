class SecureUser:
    name = None
    acc_no = 3574378237957

    def __init__(self, name, atm_pin):
        self.name = name
        self._atm_pin = atm_pin

    def get_pin(self, attempt):
        if attempt == self._atm_pin:
            print("PIN is correct")

            self.deposit_cash()
            self.cash_withdrawal()

        else:
            print("Your password is incorrect")

    def deposit_cash(self):
        print("Deposit cash")

    def cash_withdrawal(self):
        print("Withdraw cash")


user_data = SecureUser("Ravi", 6789)

user_data.get_pin(6789)