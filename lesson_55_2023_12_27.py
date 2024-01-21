# # a= 5
# # b  = 10
# #
# # if a > b:
# #     print("bigger")
# # else:
# #     print("not bigger")
# #
#
# #OR
# number1 = int(input("enter number1"))
# number2 = int(input("enter number2"))
#
# # if number1 != number2:
# #
# #     print("not equal")
# # else: print("not equal")
#
# # if number1 > number2:
# #     print("more or equal")
# # else:
# #     print("less")
#
# # if number1 >= number2:
# #     print("more or equal")
# # else:
# #     print("less")
#
# #
# # if number1 == number2:
# #     print("more or equal")
# # else:
# #     print("less")
#
# # if number1 < number2:
# #     print("more or equal")
# # else:
# #     print("less")
#
# # if number1 <= number2:
# #     print("more or equal")
# # else:
#
# #COMPARISON of number/ if we have more that one question to asked we used both if anf elif
#
# # if number1 > number2:
# #     print("more")
# # elif number1 < number2:  #elif used for more than one if
# #     print("less")
# # else: print("equal")
#
# #Example
# # year = int(input("enter year of birth:"))
# #
# # if year >= 2010:
# #     print("generation Alpha")
# # elif year >= 1997:
# #     print("generation Z")
# # elif year >= 1981:
# #     print("Millenial")
# # elif year >= 1965:
# #     print("generation X")
# # elif year >= 1946:
# #     print("Baby Boomer")
# # elif year >= 1928:
# #     print("silent generation")
# # else:
# #     print("some earlier generation")
# # print("number1 is bigger") if number1 > number2 else print("number2 is bigger") if number2 > number1 else print("they are equal")
#
# #Example 2
# a = 200
# b = 300
# c = 100
# if c > b and c > a:
#     print("number c is larger than the other ones")
#
# if c > b or c > a:
#     print("number c is larger then at least on of other numbers")
# else:
#     print("number c is not larger then at least on of other numbers")

# #Example 3
# x = 50
#
# if x > 10:
#     print("x is more than 10")
#
# if x > 20:
#     print("is more than 20")
#
# if x > 30:
#     print("is more than 30")
#     pass              #means- I would write something here
# else:
#     print("x is between 20 and 30")
#
# name = input("tell me your name:")
#
# if name == ("Tom"):
#     print("Hi, Tom")
# else:
#     print("good bye")
#
#     admins = ["Tom", "John", " Gary"]
#
#     if name is admins:
#         print("You have full administrative rights")
#     else: print("You have regular user rights")
#
#     if not name:
#         print("you have to enter a name")

    #item_count = 0



# #Exercise 1 Let user enter name, surname and age. Print if user is allowed to enter an online casino or not. 21 is the age cap.
# print("CASINO ROYALE")
# name = input("Enter name:")
# surname = input("enter surname:")
# Allowed = int(input("How old are you: "))
# admins = ["Kal", "Tom", "Dan"]
# if Allowed < 21:    x
# print("Sorry", name, surname, "you're not allowed inside")
# elif Allowed >= 21 and name in admins:
#     print("Welcome admin")
#
# #2Create a database (list of privileged users), print a specific message with a personal greeting if
# # the user is a privileged and just "Welcome otherwise"
#
# privileged_users = ['Tom', 'Alex', 'Sam', 'Alena']
# user_name = input('Enter your name: ')
# if user_name in privileged_users:
#     print(f'{user_name} welcome here!')
#     else:
#     print(f'Sorry {user_name}, you\'re not in the list but welcome otherwise')
#
#
#
# #EXercise 3 Allow user to enter two numbers, print out which one is higher than the other, or equal.
# Kaunas = 500
# Vilnius = 700
# if vilnius > kaunas:
# print("city kaunas is larger than city vilnis")
# else:
# print("city vilnius is not larger than city kaunas")

# Exercise 4 Write a small calculator application, that allows user to enter two numbers and a symbol,
# do the operation and print the answer.
# number1 = int(input("Enter number 1 "))
# number2 = int(input("Enter number2 "))
# symbol = input("enter symbol: ")
# if symbol  == "+":
#     print(number1 + number2)
# elif symbol == "-":
#     print(number1 - number2)
# elif symbol == "*":
#     print(number1 * number2)
# elif symbol == "/":
#     print(number1 / number2)

#EXercise 5 Create a number guessing game from 1-10.
# Get random integer
# import random
# rint = random.randint(1, 10)
# # Get user input
# user = int(input("Enter a number: "))
# # Check if user guesed the number
# if (user == rint):
#     print(f"{user} is correct answer! ")
# else:
#     print("Wrong guess! ")
#
# # OR EX5. Solution with while loop
# import random
#
# rint = random.randint(1, 10)
#
# # Infinite loop until user enters correct answer
# while True:
#     # Get user input
#     user = int(input('Guess a number between 1 and 10: '))
#     # Validate a number
#     if (user > 10 or user < 1):
#         print("Please enter a number between 1 and 10! ")
#     # Check for correct answer and break
#     # Otherwise print try again
#     elif (user == rint):
#         print(f"Congrats! {user} is a correct answer!")
#         break
#     else:
#         print("Try again!")

#EXercise 6 Write a simple Rock, Paper, Scissors game where
# the user can input their choice, and the computer
# generates a random choice. Determine the winner
# based on the rules: rock beats scissors,
# scissors beats paper, paper beats rock.
# import random
# comp_choice = random.choice(['R', 'S', 'P'])
# user_choice = input('Make a choice from R, P or S: ')
# print(f'Computer choice - {comp_choice}')if user_choice == comp_choice:
#     print('Draw')
#     elif (user_choice == 'R' and comp_choice == 'S') or (user_choice == 'P' and comp_choice == 'R') or (user_choice == 'S' and comp_choice == 'P'):
#     print('User wins!')
#     else:
#     print('Computer wins!')

#EXercise 7 Write a program that checks whether a given year is a leap year.
# A leap year is either divisible by 4 but not by 100 unless it is divisible by 400.
input_year = int(input("input a year "))
if input_year % 4 == 0:
if input_year % 100 != 0:
print("leap year")
else:
if input_year % 400 == 0:
print ("leap year")
else:
print("not a leap year")
else:
print("not a leap year")

# #OR
#
# import calendar
# year = int(input('Year: '))
# print(calendar.isleap(year))

# #OR
# while True:
# input_year = int(input("Enter a year (enter 0 to exit): "))
# if input_year == 0: break
# # Exit the loop if the user enters 0
# if input_year % 4 == 0:
# if input_year % 100 != 0:
# print("Leap year")
# else:
# if input_year % 400 == 0:
# print("Leap year")
# else:
# print("Not a leap year")
# else:
# print("Not a leap year")

































