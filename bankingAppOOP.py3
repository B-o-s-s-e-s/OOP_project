# Banking Systems using OOP

# Parent Class: User
# 1. Holds detials about an User
# 2. Has a function to show user detials
class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def show_user_details(self):
        print("Personal Detials")
        print(" ")
        print("Name", self.name)
        print("Age", self.age)
        print("Gender", self.gender)

# johan = User("Pika", 21, "Male")
# johan.show_user_details()

#Child Class: Bank
#1. Store details about the account balance
#2. Store details about the amount
#3. Allows for deposit, withdraw, view_balance
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name,age, gender)
        self.balance = 0

    def deposit(self,amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("New balnce: $", self.balance)
        

    def withdraw(self, amount):
        if amount > self.balance:
            print("Failed. You do not have that much money on your account")
        else:
            self.balance = self.balance - amount
            print("After withdraw, $:",self.balance)
    
    def view_balance(self):
        self.show_user_details()
        print("check total price, $:",self.balance)

#testing
johan = Bank("john", 21, "F")
johan.deposit(100)
johan.deposit(100)
johan.deposit(100)
johan.deposit(1200)
johan.withdraw(30)
johan.withdraw(70)
johan.withdraw(110)
johan.withdraw(1300)
johan.view_balance()
