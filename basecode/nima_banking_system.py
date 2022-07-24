############## BankingSystem ################
# Student Name:
# Student ID:
######################################



class Admin:

    def __init__(self, name, password):
        self.name = name
        self.password = password











# Customer and Admin




class Customer:

    def __init__(self, username, password, address):
        self.username = username
        self.password = password
        self.address = address
        self.accounts = []

    # add a current account to self.accounts
    def add_current_account(self,balance, overdraft):
        alreadyExists=False
        # only one current account allowed per user
        # Add an if here to check if there is an existing current account then dont add another one with instanceOf function in python
        for account in self.accounts:
            alreadyExists=isinstance(account, CurrentAccount)
        if(alreadyExists!=True):
            self.accounts.append(CurrentAccount(balance,overdraft))
            print("We are creatingggg a current account")    

    # add a saving account to self.accounts
    def add_saving_account(self,balance, interest):
        self.accounts.append(SavingAccount(balance,interest))

    # return the total balance of all the accounts combined
    def get_total_balance(self):
        totalBalance=0
        for account in self.accounts:
            totalBalance+=account.balance
        return totalBalance

    def get_total_accounts(self):
        return len(self.accounts)

    # function to display the user information - name, address & accounts
    def display(self):
        pass



# current and savings account
class Account:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        # overload this function for current account to take care of overdraft limits
        if(amount <= self.balance):
            self.balance = self.balance - amount
        else:
            pass

class SavingAccount(Account):

    def __init__(self, balance, interest):
        super().__init__(balance)
        self.interest = interest


class CurrentAccount(Account):

    def __init__(self, balance, overdraft):
        super().__init__(balance)
        self.overdraft = overdraft

    def withdraw(self,balance,amount):
        if amount>self.balance:
            print("Withdraw not possible")
        else:
            super().__init__(balance-amount)
            print("withdraw successful") 




class BankingSystem:

    def __init__(self):
        self.admin = Admin("Arthur", "123")

        self.customers = []

        self.customers.append(Customer("Boris", "ABC", "10 London Road"))
        self.customers.append(Customer("Chloe", "1+x", "99 Queens Road"))
        self.customers.append(Customer("David", "abc", "2 Birmingham Street"))

        self.customers[0].add_current_account(1000,100)
        self.customers[1].add_current_account(1000,100)
        self.customers[1].add_saving_account(4000,2.99)
        self.customers[2].add_saving_account(200,0.99)
        self.customers[2].add_saving_account(5000,4.99)
        print("-----------------------------------------------------")
        print(self.customers[0].username)
        print(self.customers[0].accounts[0].balance)
        print(self.customers[0].accounts[0].overdraft)
        # Do not add any parameter to this method.
        # Delete "pass" after adding code into this method.

        



    def user_logged_in(self,customer):
        print("Please select an option:")
        print(" 1 - Customer summary")
        print(" 2 - Financial summary")
        print(" 3 - Quit")
        correctOption=False
        while correctOption==False:
            selectedOption = input("Enter a number for your option: ")
            if selectedOption=="1":
                self.view_account(customer)
                correctOption=True
            elif selectedOption=="2":
                self.view_summary(customer)
                correctOption=True
            elif selectedOption=="3":
                return
                correctOption=True
            else:
                print("Enter a valid option")

    def view_account(self):
        print("You have selected 1")

    def view_summary(self,customer):
        print("------------------------------------")
        print("Total number of accounts in the bank:",customer.get_total_accounts())
        print("Total balance of all accounts in the bank:",customer.get_total_balance())
        print("Address:",customer.address)
        print("------------------------------------")




    def run_app(self):
        print("Your banking system should run by calling this method.")
        username = input("What is your username? ")
        password = input("What is your password? ")
        userLoggedIn=False
        for customer in self.customers:
            if username == customer.username and password==customer.password:
                userLoggedIn=True
                self.user_logged_in(customer)
        # if userLoggedIn:
            





p1=BankingSystem()
p1.run_app()