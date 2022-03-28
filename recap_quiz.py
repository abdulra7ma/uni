# class Rectangle(object):
#     def __init__(self, a, b) -> None:
#         self.a = a
#         self.b = b
    
#     def area(self):
#         return self.a * self.b
    
#     def perimeter(self):
#         return 2 * (self.a + self.b)
    
#     def display(self):
#         print("Area: ", self.area())
#         print("Perimeter: ", self.perimeter())
        
# a = int(input())
# b = int(input())

# r = Rectangle(a, b)

# r.display()




########################
# BankAccount
########################

class BankAccount:
    def __init__(self, name, acnt_num, balance) -> None:
        self.account_num = acnt_num
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
    
    def withdrawal(self, amount):
        self.balance -= amount

    def display(self):
        print("Account name is: ", self.name)
        print("Account number is: ", self.account_num)
        print("Account balance is: ", self.balance)

n = input()

m, b = map(int, input().split())

acc = BankAccount(n, m, b)

acc.display()

