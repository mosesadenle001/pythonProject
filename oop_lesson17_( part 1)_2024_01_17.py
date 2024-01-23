# class Account:
#
#     def __init__(self, amount=0):
#         self.amount = amount
#
#     def receive_money(self, amount):
#         self.amount +=amount
#
#
#     def withdraw(self, amount):
#         if self.amount >= amount:
#             self.amount -= amount
#             print(f"withdraw {amount}, {self.amount}")
#         else:
#             print("not enough money")
#
#
# account1 = Account()
#
# account2 = Account(2000)
#
# account1.withdraw(10)
#
# account1.receive_money(5000)
#
# account1.withdraw(10)
#
# '''>>>>>>>>>>>>>>>>>>>>>>'''
# class Animal:
# def __init__(self, gender):
# self.gender = gender
#
#  def set_gender(self, gender):
# if (gender != "male") and (gender != "female"):
# raise WrongGender("it has to be either male or female")
# else:
# self.gender = gender
#
# my_dog = Animal("male")
#
# print(my_dog.gender)
#
# my_dog.set_gender("female")


'''EX1 Create a Calculator class with main functionality: add, divide, multiply, subtract , etc..
Initiate class and show up some calculations.'''

#
# # Define object class
# class Calculator:
#     def __init__(self, num1: float, num2: float):
#         self.num1 = num1
#         self.num2 = num2
#
#     def add(self):
#         return self.num1 + self.num2
#
#     def subtract(self):
#         return self.num1 - self.num2
#
#     def divide(self):
#         return self.num1 / self.num2
#
#     def multiply(self):
#         return self.num1 * self.num2
#
#
# # Get user input
# a = float(input("Number1: "))
# b = float(input("Number2: "))
#
# acalc = Calculator(a, b)
#
# print(acalc.add())
# print(acalc.subtract())
# print(acalc.divide())
# print(acalc.multiply())
#
# '''EX2 Create the instance attributes fullname and email in the Employee class.
# Given a person's first and last names:
# Form the fullname by simply joining the first and last name together, separated by a space.
# Form the email by joining the first and last name together with a . in between, and
# follow it with @company.com at the end. Make sure the entire email is in lowercase.'''
#
#
# class Employee:
#  def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#  def fullname(self):
#     self.fullname = f'{self.first_name} {self.last_name}'
#     return self.fullname
#
#  def email(self):
#     self.email f'{self.first_name}.{self.last_name}@company.com'.lower()
#     return self.email
#     employee_info = Employee(first_name='John', last_name='Doe')
#     print(employee_info.fullname())
#     print(employee_info.email())

'''EX3 Create a Book class that has two attributes:
title
author
and two methods:
A method named .get_title() that returns: "Title: " + the instance title.
A method named .get_author() that returns: "Author: " + the instance author.
and instantiate this class by creating 3 new books:
Pride and Prejudice - Jane Austen (PP)
Hamlet - William Shakespeare (H)
War and Peace - Leo Tolstoy (WP)
The name of the new instances should be PP, H, and WP, respectively. For instance, if I instantiated the following book using this Book class:
Harry Potter - J.K. Rowling (HP)
I would get the following attributes and methods:'''












'''EX4 A country can be said as being big if it is:
Big in terms of population.
Big in terms of area.
Add to the Country class so that it contains the attribute is_big. 
Set it to True if either criteria are met:
Population is greater than 20 million.
Area is larger than 3 million square km.
Also, create a method which compares a country's population density to another country object. 
Return a string in the following format:
{country} has a {smaller / larger} population density than {other_country}'''
class Country:
    def __init__(self, country_name, population, area):
        self.population = population
        self.area = area
        self.country_name = country_name
        def is_big(self):
            if self.population >= 20000000 and self.area >= 3000000:
                return True
            else:
                return False
        def country_density(self):
                self.density = self.population / self.area
                return self.density
        def compare(self, other_country):
            if self.country_density() > other_country.country_density():
                return f"{self.country_name} has a LARGER population density than {other_country.country_name}"
            elif self.country_density() < other_country.country_density():
                return f"{self.country_name} has a SMALLER population density than {other_country.country_name}"
            else:
                return f"{self.country_name} has an EQUAL population density than {other_country.country_name}"
Lithuania = Country("Lithuania", 2800000, 65300)
Latvia = Country("Latvia", 1884000, 64589)
print(Lithuania.is_big())
print(Lithuania.compare(Latvia))

'''OR'''
class Country:
    def __init__(self, country_name, population, area):
        self.population = population
        self.area = area
        self.country_name = country_name
        if self.population >= 20000000 and self.area >= 3000000:
            self.is_big = True
        else:
            self.is_big = False
    def country_density(self):
                self.density = self.population / self.area
                return self.density
    def compare(self, other_country):
        if self.country_density() > other_country.country_density():
           return f"{self.country_name} has a LARGER population density than {other_country.country_name}"
        elif self.country_density() < other_country.country_density():
             return f"{self.country_name} has a SMALLER population density than {other_country.country_name}"
        else:
            return f"{self.country_name} has an EQUAL population density than {other_country.country_name}"
Lithuania = Country("Lithuania", 2800000, 65300)
Latvia = Country("Latvia", 1884000, 64589)
print(Lithuania.is_big)
print(Lithuania.compare(Latvia))






