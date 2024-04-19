class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self.__balance = balance

    def deposit(self, money_deposited):
        self.__balance += money_deposited
        print('Total balance now is ', self.__balance)

    def withdrawal(self, money_withdrawn):
        self.__balance -= money_withdrawn
        print('Total balance is ', self.__balance)

class customer(BankAccount):
    def __init__(self, name, account_number, balance):
        super().__init__(account_number, balance)
        self.name = name

    def deposit1(self, money_deposited):
        super().deposit(money_deposited)

first_customer = customer('Jai', 23330, 10000000)
first_customer.deposit1(900000)
print(first_customer._account_number)
print(first_customer._BankAccount__balance)

second_customer = BankAccount(2900034, 10000000)
second_customer.deposit(1000)

# The reason print(first_customer._customer__balance) doesn't work is because name mangling in Python is applied at the class level, not at
# the instance level. When you define a class with a double underscore attribute like __balance, Python actually renames the attribute to_BankAccount__balance internally to enforce the idea of "name
# mangling". This renaming is done at the class level, so it affects all instances of the class, including instances of any subclasses.