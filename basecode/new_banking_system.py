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

    # add a saving account to self.accounts
    def add_saving_account(self,balance, interest):
        self.accounts.append(SavingAccount(balance,interest))
        # print("Printingggggg accounts list")
        # for account in self.accounts:
        #     print(account)

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
        if amount <= self.balance:
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
        # Do not add any parameter to this method.
        # Delete "pass" after adding code into this method.


    def user_logged_in(self,customer):
        print("Please select an option:")
        print(" 1 - View Account")
        print(" 2 - View summary")
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



    def view_account(self,customer):
        print("-- Account list --")
        print("Please select an option:")
        i=0
        for account in customer.accounts:
            i+=1
            if isinstance(account, CurrentAccount):
                accountType="Current account: "
            elif isinstance(account, SavingAccount):
                accountType="Saving account: "

            message=str(i)+" - "+accountType+str(account.balance)
            print(message)
        continueFromHere=False
        while continueFromHere==False:
            user_input=input("Enter a number to select your option:")
            if int(user_input)<=i:
                continueFromHere=True
                self.display_selected_account_info(customer,i,accountType,account.balance)



    def display_selected_account_info(self,customer,i,accountType,balance):
        print("You selected "+str(i) +" - "+accountType+str(balance))
        print("Please select an option:")
        print("1 - Deposit")
        print("2 - Withdraw")
        print("3 - Go Back")
        user_input=input("Enter a number to select your option:")
        if user_input=="1":
            amount=input("Enter the deposit amount: ")
            customer.accounts[i-1].deposit(int(amount))
            self.user_logged_in(customer)
        elif user_input=="2":
            amount=input("Enter the withdraw amount: ")
            customer.accounts[i-1].withdraw(int(amount))
            self.user_logged_in(customer)
        else:
            self.user_logged_in(customer)



    def view_summary(self,customer):
        print("------------------------------------")
        print("Total number of accounts in the bank:",customer.get_total_accounts())
        print("Total balance of all accounts in the bank:",customer.get_total_balance())
        print("Address:",customer.address)
        print("------------------------------------")


    def Admin_logged_in(self):
        print("1 - Customer summary")
        print("2 - Financial forecast")
        print("3 - Transfer Money - GUI")
        print("4 - Account management - GUI")
        admin_input=input("Enter a number to select your option: ")
        if admin_input=="1":
            self.print_user_data_for_admin()
        elif admin_input=="2":
            self.financial_forecast()
        else:
            pass


    def print_user_data_for_admin(self):
        for customer in self.customers:
            print("- "+customer.username) 
            print("- "+customer.address) 

            for account in customer.accounts:
                if isinstance(account, CurrentAccount):
                    accountType="Current account: "
                elif isinstance(account, SavingAccount):
                    accountType="Saving account: "

                message="- "+accountType+str(account.balance)
                print(message)
            print('-------------------')


    def financial_forecast(self):
        for customer in self.customers:
            print("- "+customer.username)
            print("- "+str(customer.get_total_accounts()))
            totalForecastMoney=0
            for account in customer.accounts:
                if isinstance(account, CurrentAccount):
                    totalForecastMoney+=account.balance
                elif isinstance(account, SavingAccount):
                    totalForecastMoney+=account.balance+account.balance*account.interest

                message="- total forecast money: "+str(totalForecastMoney)
                print(message)


    def run_app(self):
        print("Your banking system should run by calling this method.")
        username = input("What is your username? ")
        password = input("What is your password? ")
        userLoggedIn=False
        for customer in self.customers:
            if username == customer.username and password==customer.password:
                userLoggedIn=True
                self.user_logged_in(customer)
        if username == self.admin.name and password==self.admin.password:
            self.Admin_logged_in()
            





p1=BankingSystem()
p1.run_app()