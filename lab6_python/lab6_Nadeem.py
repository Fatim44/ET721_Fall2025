"""

Fatima Nadeem
Sep 17,2025
Lab 6: objects and classes

"""

print ("\n----- Example 1: create a class -----")
class Circle(object):
    def _init_(self,radius,color):
        self.radius = radius
        self.color = color 

    #method
    def add_radius(self,r):
        self.radius += r 
        return self.radius * self.height
    #method to calculate the perimeter 
    def perimeter(self):
        return 2 * self.width + 2 * self.height
    
class Rectangle(object):
    def __init__(self, height, width, color):
        self.height = height
        self.width = width

#creating an instance of the class, which is an object
circle1 = Circle(4, "red")
circle2=  Circle(10, "green")

rectangle1 = Rectangle(2,5,"magenta")
rectangle2 = Rectangle(7,3,"blue")

#acessing information in an object
print(f"The color of circle2 = {circle2.color}")
print(f"The width of rectangle1 = {rectangle1.width}")

#updating data in an object
#change circle1 color from 'red' to 'yellow' 
print(f"The color of circle1 before the update = {circle1.color}")
circle1.color = "yelllow"
print(f"The color of circle1 after the update = {circle1.color}")

#accessing a method 
print(f"Radius of circle2 = {circle2.radius}")
#update the radius by adding 5 
circle2.add_radius(5)
print(f"Radius f circle2 after method add_radius = {circle2.radius}")

#accessing methods in Rectangle 
print(f"The area of the rectangle with width {rectangle1.width} and height {rectangle1.height}")
print(f"The perimeter of rectangle2 = {rectangle2.perimeter()}") 

print("\n----- EXERCISE ------")
class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. Current balance: ${self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew ${amount}. Current balance: ${self.balance}")
        else:
            print(f"Insufficient funds. Withdrawal of ${amount} cannot be made.")

useraccount = BankAccount(123456789, "Student's Name")

useraccount.withdraw(700)
useraccount.deposit(1000)
useraccount.withdraw(500)

print(f"Final balance: ${useraccount.balance}")