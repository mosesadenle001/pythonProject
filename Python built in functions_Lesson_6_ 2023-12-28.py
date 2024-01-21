# #>>>>>print()
# #print(object(s), sep=separator, end=end, file=file, flush=flush)
#
# #object(s) == Any object, and as many as you like. Will be converted to string before printed
# #sep== 'separator' Optional. Specify how to separate the objects, if there is more than one. ****Default is ' '****
# #end== 'end' Optional. Specify what to print at the end. ****Default is '\n'****** (line feed)
# #file == Optional. An object with a write method. Default is ******sys.stdout****
# #flush == Optional. A Boolean, specifying if the output is flushed (True) or buffered (False). Default is ****False****
#
# #object(s) ==
# print("hello world")
# print("hello", "world")
# print(*["hello", "world"])
#
# #sep== 'separator'
# print("hello world", sep=",")
# print("hello", "world", sep=" amazing ")
#
# names_list = ["Albert", "Niels", "Nicole", "Thomas",]
# print(*names_list, sep= " | ")
# # Example with different values separated by a custom separator
# name = "John"
# age = 30
# city = "New York"
# # Using the sep parameter to specify a custom separator
# print(name, age, city, sep=' | ')
#
# #end== 'end'
# # Example using the end parameter
# name = "Alice"
# age = 28
# # Using the end parameter to specify a custom ending string
# print("Name:", name, end=' | ')
# print("Age:", age)      #output Name: Alice | Age: 28
#
# #file
# # Example using the file parameter
# output_file_path = "output.txt"
# name = "Bob"
# age = 35
# # Open a file in write mode and use it as the 'file' parameter in print
# with open(output_file_path, 'w') as file:
#     print("Name:", name, file=file)
#     print("Age:", age, file=file)
# # Verify the content of the file
# with open(output_file_path, 'r') as file:
#     content = file.read()
#     print("Content of", output_file_path, ":\n", content)
#
# #flush
# import time
# # Example using the flush parameter
# for i in range(5):
#     print(f"Countdown: {5 - i}", end='\r', flush=True)
#     time.sleep(1)
# # Adding a newline to separate the countdown from the next output
# print("\nFinished countdown!")
#
# # More Example
# print("Hello, world!")
# # Printing multiple values
# x = 10
# y = 20
# print("The values are:", x, y)
# # Changing separator and end characters
# print("One", "Two", "Three", sep=' | ', end=' !!!\n')
# # Using variables in print
# name = "Alice"
# age = 25
# print("Name:", name, "| Age:", age)
#
# #>>>>type()
# greet = "Hello World"
# print(type(a))
#
# number = 2022
# print(type(number))
#
# my_list = [1, 2, 3]
# print(type(my_list))
# print(type(my_list[0]))
# my_list = [42, "hello", 3.14, True]
# # Print the type of the first element
# print(type(my_list[0]))
#
# #len()
# #len() using a string
# word = "something"
# length = len(word)
# print(f"length of the word {word} is: {length}")
# my_string = "Hello, World!"
# # Using the len() function to get the length of the string
# string_length = len(my_string)
# print(f"The length of the string is: {string_length}")  #output The length of the string is: 13
#
# #len() using a lists
# my_list = [1, 2, 3]
# print(f"length of the list {my_list} is: {len(my_list)}")
# my_list = [1, 2, 3, 4, 5]
# # Using the len() function to get the length of the list
# list_length = len(my_list)
# print(f"The length of the list is: {list_length}")
#
# #round()
# # print(round(1.99999))
#
# # print(round(99.4444))
# #
# # print(round(1.5555555, 2))
#
# # Example using the round() function
# pi = 3.141592653589793
# # Round pi to 2 decimal places
# rounded_pi = round(pi, 2)
# print(f"The rounded value of pi is: {rounded_pi}")   #output The rounded value of pi is: 3.14
#
# # Example rounding to the nearest integer
# number = 4.6
# rounded_number = round(number)
# print(f"The rounded value is: {rounded_number}")  #output The rounded value is: 5
#
# #sorted()
#
# # my_list = [1, 5, 9, 7, 3, 2, 4, 6, 5, 9, 1, 3]
#
# # print(my_list)
# # print(sorted(my_list,reverse=True))
#
#
# # my_dictionary = {1: 2, 3: 1, 2: 4}
# #
# # print(sorted(my_dictionary.items()))
# #
# # print(sorted(my_dictionary,reverse=True))
# #
# # my_string = ["Albert", "Nicole", "Niels", "Thomas", ]
# # print(my_string)
# #
# # print(sorted(my_string,reverse=True))
#
# # print(ord("\n"))
# #
# # # print(chr(10))
# # #
# # # print(chr(8455))
# #
# # print(chr(937))
#
#
# # Example using the sorted() function
# unsorted_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# # Using sorted() to sort the list
# sorted_list = sorted(unsorted_list)
# print("Original list:", unsorted_list)
# print("Sorted list:", sorted_list)   #output Original list: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
#                                     #Sorted list: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
#
# # Example sorting in descending order
# sorted_desc = sorted(unsorted_list, reverse=True)
# print("Original list:", unsorted_list)
# print("Sorted list (descending):", sorted_desc)  #output Original list: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
#                                               #Sorted list (descending): [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1]
#
#
#
#
#
#
# #Exercise 1 Create a list of different types of
# # python objects, and print all the types.
# # my_list_class = [{"age": 39}, "facebook", True, {"name": "Mark Zuckerberg"}, (1, 2, 3), [4.23, 2.78]]
# # print(my_list_class)
#
# # # Exercise 2
# # Print all the items (from previous) separated with "|"
# # car_brand = ["Toyota", "Benz", "BMW", "Audi"]
# # arrange_car = sorted(car_brand)
# #
# # print("arrange car brands classify them with '|': " ": ")
# # print("|".join(arrange_car))
# #
# #EX3
# # Create a list of floats with 3 decimal points, create another
# # # # list with all the values rounded to 2 decimals.
# # float_number = [91.782, 75.839, 83,890, 90.938, 100.000]
# # list_int = []
# #
# # for item in float_number:
# #     list_int.append(round(item, 2))
# #     print(list_int)
#
# # EX4
# # # #4 Create a list with student names and sort them, print the result to the terminal
# # python_student = ["Wike", "John", "Monika", "Alex"]
# # print(sorted(python_student))
#
#
# # # #5 Write a program that allows user to
# # # # write in any float number and then round it.
# # my_new_year = input("Happy new year in advance: ")
#
# # new_year_float = float(my_new_year)
# # number = round(new_year_float)
# # print(f"number: {new_year_float}")
#
# #EX6
# # ## Exercise 1: String Analyzer
# # Write a program that takes a string as input and prints:
# # The length of the string.
# # The type of the string.
# # The string in uppercase.
# # The string in lowercase.
#
# string_analys = input('Enter a string: ')
# print(len(string_analys), type(string_analys), string_analys.upper(), string_analys.lower(), sep='\n')
#
# #EX7
# # List Statistics
# # Create a list of numbers and write a program that prints:
# # The length of the list.
# # The sum of the numbers in the list.
# # The average of the numbers in the list (rounded to two decimal places).
# # The list sorted in ascending order.
#
# list_statis = [78, 89, 903, 839, 1, 79, 90, 872, 70]
# print(len(list_statis))
# print(sum(list_statis))
# average_number = sum((list_statis)) / len((list_statis))
# print(round(average_number, 2))
#
# #EX 8
# # Temperature Converter
# # Write a program that converts a temperature in Fahrenheit to Celsius.
# # Take the temperature as input and use the formula: Celsius = (Fahrenheit - 32) * 5/9.
# # Round the result to two decimal places.
# temperature_fah = int(input('Enter a temperature in Fahrenheit: '))
# temperature_cel = (temperature_fah - 32) * 5/9
# print(f'{temperature_fah}°F to == {round(temperature_cel, 2)}°C')
#
#
# #EX9
# # Word Sorter
# # Write a program that takes a sentence as input
# # and prints the words in the sentence in alphabetical order.
# # You can use the sorted function.
#
# print(sorted(input('Enter word as sentence: ').lower().split()))
#
# #EX10 List Reverser
# # Create a list of items and write a program that prints the list in reverse order.
# # Use the reverse method or slicing.
# my_list = [1, 'Max', True, {'1': 'value', '2': 'value2'}, 2.56, [1, 2, 3]]
# print(my_list[::-1])
#
# #EX 11
# # Type Checker
# # Write a program that takes user input and
# # prints the type of the input (e.g., int, float, str, list).
#
#
# #EX12
# # Area Calculator
# # Write a program that calculates the area of a circle.
# # Take the radius as input and
# # use the formula: Area = π * r^2. You can use the round function to round the result.
# print(round(3.14 * (float(input('Enter a circle radius: ')) ** 2), 2))

