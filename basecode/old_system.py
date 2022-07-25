# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 20:09:50 2022

@author: sanit
"""

class BankingSystem:

    def __init__(self):
        self.username_list = ["Boris", "Chloe", "David"]
        self.usernames_dictionary = {"Arthur" : "123", "Boris" : "ABC", "Chloe" : "1+x" , "David" : "aBC"}
        self.acts_types = {"Arthur" : "admin", "Boris" : "customer", "David" : "customer", "Chloe" : "customer"}
        self.balance = {"Boris" : 1000, "Chloe" : [1000,4000], "David" : [200 , 5000]}
        self.address = {"Boris" : "10 London Road", "Chloe" : "99 Queens Road", "David" : "2 Birmingham Street"}
        self.acc_types = {"Boris" : "current account", "Chloe" : ["current account","savings account"], "David" : ["savings account","savings account"]}
        self.overdraft = {"Boris" : 100, "Chloe" : [100,0]}
        self.interest = {"Chloe" : [0,2.99], "David" : [0.99,4.99]}

    def run_app(self):
        while True:
            username = input("What is your username? ")
            users_password = input("What is your password? ")

            if username in self.usernames_dictionary:

                if self.usernames_dictionary[username] == users_password:
                    print("You are logged in")
                    break
                else:
                    print("Incorrect password")


        if self.acts_types[username] == "admin":
            print("Please select an option:")
            print(" 1 - Customer summary")
            print(" 2 - Financial summary")
            user_input = input("Enter a number for your option: ")
            if user_input == "1":

                print("Boris account 1 -")
                print(self.username_list[0])
                print(self.address["Boris"])
                print(self.balance["Boris"])
                print(self.acc_types["Boris"])
                print(self.overdraft["Boris"])
                print("--")
                print("Chloe current account 1 -")
                print(self.username_list[1])
                print(self.address["Chloe"])
                print(self.balance["Chloe"][0])
                print(self.acc_types["Chloe"][0])
                print(self.overdraft["Chloe"][0])
                print("--")
                print("Chloe savings account 1 -")
                print(self.acc_types["Chloe"][1])
                print(self.interest["Chloe"][1])
                print(self.balance["Chloe"][1])
                print("--")
                print("David savings account 1 -")
                print(self.username_list[2])
                print(self.address["David"])
                print(self.balance["David"][0])
                print(self.acc_types["David"][0])
                print(self.interest["David"][0])
                print("David savings account 2 -")
                print((self.balance["David"][1]))
                print(self.acc_types["David"][1])
                print(self.interest["David"][1])


            elif user_input == "2":
                print("Boris' account --")
                print(self.username_list[0])
                print("There are",(self.acc_types["Boris"]),"account open in this bank account.")
                print("The total balance of all accounts is :£",(self.balance["Boris"]))
                print("--")
                print("Chloe's account - ")
                print(self.username_list[1])
                print("There are",len(self.acc_types["Chloe"]),"account open in this bank account.")
                print("The total balance of all accounts is :£",sum(self.balance["Chloe"]))
                forecast_chloe = self.balance["Chloe"][1] * (self.interest["Chloe"][1] / 100)
                forecast_chloe2 = self.balance["Chloe"][1] + self.balance["Chloe"][0] + forecast_chloe
                print(forecast_chloe2)
                print("--")
                print("David's account  -")
                print(self.username_list[2])
                print("There are",len(self.acc_types["David"]),"account open in this bank account.")
                print("The total balance of all accounts is :£",sum(self.balance["David"]))
                forecast_david_Savings1 = self.balance["David"][0] * (self.interest["David"][0] / 100)
                forecast_david2 = self.balance["David"][0] + forecast_david_Savings1
                forecast_david3 = self.balance["David"][1] * (self.interest["David"][1] / 100)
                forecast_david4 = self.balance["David"][1] + forecast_david3
                print(forecast_david4 + forecast_david2)

        elif username == "Boris":
            while True:
            # how do we run this code underneath?
                print("Please select an option:")
                print(" 1 - View account")
                print(" 2 - View summary")
                print(" 3 - Quit")
                user_input = input("Enter a number for your option: ")

                if user_input == "1":
                    print("--Account list--")
                    print("Please select an option")
                    print(" 1 - Current account:£", self.balance["Boris"])
                    boris_option = input("Enter a number to selection your option: ")

                    if boris_option == "1":
                        print("You selected 1 - Current account:", )
                        print("Please select an option")
                        print(" 1 - Deposit")
                        print(" 2 - Withdraw")
                        print(" 3 - Go back")
                        boris_option_var = input("Enter a number to select your option: ")

                        if boris_option_var == "1":
                            deposit_amount =  int(input("Please enter how you'd like to deposit: "))
                            new_balance = deposit_amount + self.balance["Boris"]
                            self.balance["Boris"] = new_balance

                        elif boris_option_var == "2":
                            withdraw_amount =  int(input("Please enter how you'd like to withdraw: "))
                            new_balance = withdraw_amount - self.balance["Boris"]
                            self.balance["Boris"] = new_balance

                        elif boris_option_var == "3":
                            pass

                elif user_input == "2":
                    print("There are",len(self.acc_types["Boris"]),"account open in this bank account.")
                    print("The total balance of all accounts is :£",(self.balance["Boris"]))
                    print(self.address["Boris"])
                    break

                elif user_input == "3":
                    break

        elif username == "Chloe":
            while True:
            # how do we run this code underneath?
                print("Please select an option:")
                print(" 1 - View account")
                print(" 2 - View summary")
                print(" 3 - Quit")
                user_input = input("Enter a number for your option: ")

                if user_input == "1":
                    print("--Account list--")
                    print("Please select an option")
                    print(" 1 - Current account:£", self.balance["Chloe"])
                    chloe_option = input("Enter a number to selection your option: ")

                    if chloe_option == "1":
                        print("You selected 1 - Current account:", )
                        print("Please select an option")
                        print(" 1 - Deposit")
                        print(" 2 - Withdraw")
                        print(" 3 - Go back")
                        chloe_option_var = input("Enter a number to select your option: ")

                        if chloe_option_var == "1":
                            deposit_amount =  int(input("Please enter how you'd like to deposit: "))
                            new_balance = deposit_amount + self.balance["Chloe"]
                            self.balance["Chloe"] = new_balance

                        elif chloe_option_var == "2":
                            withdraw_amount =  int(input("Please enter how you'd like to withdraw: "))
                            new_balance = withdraw_amount - self.balance["Chloe"]
                            self.balance["Chloe"] = new_balance

                        elif chloe_option_var == "3":
                            pass

                elif user_input == "2":
                    print("There are",len(self.acc_types["Chloe"]),"account open in this bank account.")
                    print("The total balance of all accounts is :£",sum(self.balance["Chloe"]))
                    print(self.address["Chloe"])
                    break

                elif user_input == "3":
                    break

        elif username == "David":
             while True:
             # how do we run this code underneath?
                 print("Please select an option:")
                 print(" 1 - View account")
                 print(" 2 - View summary")
                 print(" 3 - Quit")
                 user_input = input("Enter a number for your option: ")

                 if user_input == "1":
                     print("--Account list--")
                     print("Please select an option")
                     print(" 1 - Current account:£", self.balance["David"])
                     david_option = input("Enter a number to selection your option: ")

                     if david_option == "1":
                         print("You selected 1 - Current account:", )
                         print("Please select an option")
                         print(" 1 - Deposit")
                         print(" 2 - Withdraw")
                         print(" 3 - Go back")
                         david_option_var = input("Enter a number to select your option: ")

                         if david_option_var == "1":
                             deposit_amount =  int(input("Please enter how you'd like to deposit: "))
                             new_balance = deposit_amount + self.balance["David"]
                             self.balance["David"] = new_balance

                         elif david_option_var == "2":
                             withdraw_amount =  int(input("Please enter how you'd like to withdraw: "))
                             new_balance = withdraw_amount - self.balance["David"]
                             self.balance["David"] = new_balance

                         elif david_option_var == "3":
                             pass

                 elif user_input == "2":
                     print("There are",len(self.acc_types["David"]),"account open in this bank account.")
                     print("The total balance of all accounts is :£",sum(self.balance["David"]))
                     print(self.address["David"])
                     break

                 elif user_input == "3":
                     break

p1=BankingSystem()
p1.run_app()