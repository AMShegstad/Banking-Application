
"""
Alexander Shegstad
09/27/2022
Module 9 Assignment

For this module, we will work with classes by creating a banking program. Your program will use the inheritance diagram 
from this week in order to create a parent class and two child classes. Your program will create an object of each type: (CheckingAccount and SavingsAccount).
Your program will use the following data:
Balance: $200, $25
Fees: $5
Minimum Balance: $50
Interest Rate: 2%
You will need to run the program twice. Once with the account balance of $200 and once with the account balance of $25.
Since the second run of the program will have a balance lower than the minimum balance, a message should be output letting 
the user know that their account is below the minimum balance. Incorporate the good coding practices you have learned up to 
this point in the course such as Try/Except Blocks, allow the user to continue to run the program, and to exit the program, 
formatting methods, etc.

I hard-coded to values in the computer, and if you withdraw enough from checking to dip below your minimum threshold,
you will recieve a message informing you that you must make a deposit for risk having to pay the fees. 

I'd love to hear your thoughts on the readability of this code. Can I be improving it?
"""

class BankAccount():
    """A class for bank accounts"""

    def __init__ (self, accountNumber, balance):
        self.accountNumber = accountNumber
        self.balance = float(balance)

        def getAccountNumber(self):
            # Get name 
            return self.accountNumber

        def setBalance(self):
            # Set the balance amount.
            self.setBalance = float(balance)

    def depositCash(self):
            # Add to the balance.
            deposit = float(input("How much would you like to deposit?\n"))
            # Try/Except block to prevent letters from being entered
            try:
                deposit = float(deposit)
            except ValueError:
                print("Invalid input. Numeric values only.")
            #update the balance
            self.balance = float(deposit + self.balance)
            # and print
            print(f"Your balance is now ${self.balance}")

    def withdrawCash(self):
            # Subtract from the balance.
            self.withdrawal = float(input("How much would you like to withdraw?\n"))
            # Try/except block to prevent letters from being entered
            try:
                self.withdrawal = float(self.withdrawal)
            except ValueError:
                print("Invalid input. Numeric values only.")
        
            # update the balance
            if self.withdrawal >= self.balance:
                self.balance = self.balance - self.withdrawal
            else:
                print("You don't have enough money in your account.")
                print("Operation cancelled...")
            # and print
            print(f"Your balance is now {self.balance}")

    def viewBalance(self):
            # Display the account balance for the user.
            print(f"Your account has a balance of {self.balance}.")

class CheckingAccount(BankAccount):
    def __init__ (self, accountNumber, balance, fees, minimumBalance):
        # Must initiate the parent class features
        super().__init__(accountNumber, balance)
        
        self.fees = float(fees)
        self.minimumBalance = float(minimumBalance)
    # define the fees behavior
    def getFees(self):
        if self.balance < self.minimumBalance:
            print(f"Your account is below the minimum balance. Please make a deposit to avoid fees of ${self.fees}")
        return self.fees

    def getMinimumBalance(self):
        return self.minimumBalance
        
    

class SavingsAccount(BankAccount):
    def __init__ (self, accountNumber, balance, interestRate, minimumBalance):
        # Must initiate the parent class.
        super().__init__(accountNumber, balance)

        self.interestRate = float(interestRate)
        self.minimumBalance = float(minimumBalance)

#The fun part!
def main():
    print("Thank you for choosing Shegstad Bank! \n Please select your banking action:\n")
    #Start a while loop to keep the user in the program until they quit.
    keepBanking = True
    while keepBanking == True:
        #create a menu of choices
        print("********************************")
        action = input(" V to view balance. \n W to withdraw funds. \n D to deposit funds. \n Quit to exit application.\n")
        print("********************************")
        # If the user choose to view...
        if action.lower() == "v":
            # They choose which account
            chooseAccount = input(" C for checking. \n S for savings\n")
            #If they choose checking...
            if chooseAccount.lower() == "c":
                myCheckingAccount.viewBalance()
                #Checking has a minimum balance so we must check if a notification is needed.
                if myCheckingAccount.balance < myCheckingAccount.minimumBalance:
                    print(f"Your balance is below the required minimum. Please make a deposit to avoid fees of ${myCheckingAccount.fees}!")
                # and if they choose savings...
            elif chooseAccount.lower() == "s":
                mySavingsAccount.viewBalance()
            else:
                # chooose a valid letter, please
                print("******************************")
                print("Please choose a valid response")
                print("******************************")
                continue
        #if the choose to withdraw...
        elif action.lower() == "w":
            #checking or savings?
            chooseAccount = input(" C for checking. \n S for savings\n")
            if chooseAccount.lower() == "c":
                myCheckingAccount.withdrawCash()
                #gotta watch out for that minimum balance!
                if myCheckingAccount.balance < myCheckingAccount.minimumBalance:
                    print(f"Your balance is below the required minimum. Please make a deposit to avoid fees of ${myCheckingAccount.fees}!")
            elif chooseAccount.lower() == "s":
                mySavingsAccount.withdrawCash()
            else:
                print("******************************")
                print("Please choose a valid response")
                print("******************************")
                continue
        #if they choose to deposit...
        elif action.lower() == "d":
            chooseAccount = input(" C for checking. \n S for savings\n")
            if chooseAccount.lower() == "c":
                myCheckingAccount.depositCash()
            elif chooseAccount.lower() == "s":
                mySavingsAccount.depositCash()
            else:
                print("******************************")
                print("Please choose a valid response")
                print("******************************")
        elif action.lower() == "quit":
            keepBanking = False
            print("************************************")
            print("Thank you for banking with us today!")
            print("************************************")
            break
        else:
            print("I'm sorry, please choose a valid response from the list below...\n\n")
            continue


#Create two instances of my BankAccount classes
myCheckingAccount = CheckingAccount("0001", 200, 5, 50)
mySavingsAccount = SavingsAccount("0002",  25, 0.02, 50)


main()