'''Create a simple bank account class, BankAccount, with the following specifications:
-The BankAccount class should have an attribute balance which starts at 0.
-It should have an instance method deposit that allows an amount to be added to the balance.
-It should have an instance method withdraw that allows an amount to be taken from the balance.
If the balance is less than the withdrawal amount, print a message that says "Insufficient funds".
-Add a class method from_balance that takes a starting balance as an argument
and returns a new BankAccount instance with that starting balance.
-Add a static method transfer that takes two BankAccount instances and an amount as arguments.
It should withdraw the amount from the first account and deposit it into the second account.'''
#
# class BankAccount:
#     def __init__(self,):
#         self.balance = 0
#
#     def deposit(self, amount):
#         self.balance += amount
#
#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#         else:
#             print("The balance is insufficient for this transaction")
#
#     @classmethod
#     def from_balance(cls, starting_balance,):
#         account = cls()
#         account.balance = starting_balance
#         return account
#
#     @staticmethod
#     def transfer(from_account, to_another_account, amount):
#         from_account.withdraw(amount)
#         to_another_account.deposit(amount)
#
#     def saving():
#     create_account1 = BankAccount.from_balance(50000)
#     create_account2 = BankAccount()
#
#     BankAccount.transfer("account_create1, create_account2", 40000)
#     print("Balance from created account1:", create_account1.balance)
#     print("Balance from created account2:", create_account2.balance)
#
#     print("Balance from created account1:", create_account1.balance)
#     print("Balance from created account2:", create_account2.balance)

''' EX5 
-The SpaceStation class should have an attribute astronauts which is a list of dictionaries. 
Each dictionary represents an astronaut and has keys: name, nationality, and mission_duration.
-It should have an instance method add_astronaut that takes a name, nationality, and mission duration, 
creates a new astronaut dictionary, and adds it to the astronauts list.
-It should have an instance method find_astronaut that takes a name and returns the astronaut dictionary 
with that name, or None if no such astronaut is found.
-Add a class method from_astronaut_list that takes a list of astronauts (each represented as a dictionary) 
and returns a new SpaceStation instance with those astronauts.
-Add a static method is_long_term_mission that takes an astronaut dictionary and returns 
True if the astronaut's mission duration is more than 6 months, and False otherwise.
-Add an instance method remove_astronaut that takes a name and removes the astronaut with 
that name from the astronauts list.'''

class SpaceStation:
    def __init__(self):
        self.astronauts = [{"name": Python, "nationality": codeacademy, "mission_duration": 7}]
    def add_astronaut(self, name, nationality, mission_duration):
        astronaut = {"name": name, "Pyrhon": nationality, "Codeacademy": "mission_duration": 7}
        self.astronauts.append(astronaut)

    def find_astronaut(self, name):
        for astronaut in self.astronauts:
            if astronaut["name"] == name:
                return astronaut
        return None
    @classmethod
    def from_astronaut_list(cls, astronaut_list):
        space_station = cls()
        space_station.astronauts = astronaut_list
        return space_station
    @staticmethod
    def is_long_term_mission(astronaut):
        return astronaut["mission_duration"] > 6/12
    else:
    return false

    def remove_astronaut(self, name):
        for astronaut in self.astronauts:
            if astronaut["name"] == name:
                self.astronauts.remove(astronaut)
                break

station = SpaceStation.from_astronaut_list(astronauts)
station.add_astronaut("Sara", "France", 9)
print(station.astronauts)





