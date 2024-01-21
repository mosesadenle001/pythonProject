# Catching and handling Exceptions
#
# list1 = [12, 5, 3, 4, 56, 12]
#
# list2 = [0, 2, 3, 0, 12, 78]
#
# for index, item in enumerate(list1):
#     try:
#
#         result = list1[index]/list2[index]   # we can also replace list1 as item
#     except ZeroDivisionError:
#         result = "infinity"
#
#         print(result)  #output infinity infinity
#                       #however using "12" string in list2 output showed
#                       # TypeError: unsupported operand type(s) for /: 'int' and 'str'
#
# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# list1 = [12, 5, 3, 4, 56, 12, 58, 45]
#
# list2 = [0, 2, 3, 0, 12, 78]
#
# for index, item in enumerate(list1):
#     try:
#
#         result = item/list2[index]   # we can also replace list1 as item
#     except ZeroDivisionError:
#         result = "infinity"
#
#         print(result)
#
#
# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#
# list1 = [12, 5, 3, 4, 56, 12, 58, 45]
#
# list2 = [0, 2, 3, 0, "12", 78]
#
# for index, item in enumerate(list1):
#     try:
#
#         result = item/list2[index]   # we can also replace list1 as item
#         print(result)
#     except ZeroDivisionError: TypeError, IndexError
#         result = ("something's wrong")
#
#         print(result)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Multiple except clauses
# list1 = [12, 5, 3, 4, 56, 12, 58, 45]
#
# list2 = [0, 2, 3, 0, "12", 78]
#
# for index, item in enumerate(list1):
#     try:
#
#         result = item/list2[index]   # we can also replace list1 as item
#         print(result)
#     except ZeroDivisionError:
#         print("infinity")
#     except TypeError:
#         print("cant divide int bt string")
#     except IndexError:
#         result = ("too many items")
#
#         print(result)

#>>>>>>>>>>>>>>>>>>>>>
# from typing import Union
#
# def my_dummy_int_func(a: Union[str, float]) -> None:
#     try:
#         int_value = int(a)
#         return int_value
#     except ValueError:
#         print('Value of "a cannot be deduced to integer')
#     except TypeError:
#         print('Type of "a" is incompatible; should either be a number or a string')
#
# print(my_dummy_int_func({1, 2}))

#EX1
def key_error(my_dict):
    try:
        print(my_dict[2])
    except KeyError:
        print('No such key')

key_error({"20": "I love coding", "40": "Great"})

#>>>>>>>>>>>>>>>>>>>
#EX2
# In Python, dividing by zero raises a ZeroDivisionError. Your task is to create a function that:
# Takes two numbers as arguments.
# Tries to divide the first number by the second number.
# If the second number is zero, it should catch the ZeroDivisionError and return a custom error message.
# If the division is successful, it should return the result.
# Regardless of whether the division is successful or not, it should print a message saying "Attempted division. If the inputs are not numbers, it raises a TypeError. It catches this TypeError and returns a custom error message.



#Ex3
# Create a mini python program which would take two
# numbers as an input and would return their sum, subtraction, division, multiplication.
# Handle all possible errors that may occur.























