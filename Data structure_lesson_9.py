#Square all numbers 5-15 and put them in a tuple
#Tuple comprehension

#squares = tuple(s[i ** 2 for i in range(5, 16)]):

#EX 1
#Find all of the numbers from 1-1000 that are divisible by 6.
# numbers = []
# ([for number in range(1,1001) if number ** 6])
#    numbers.append(number)
print(numbers)


# using List comprehension
# numbers = [number for number in range(1, 1001) if number / 6]
# print(numbers)

#EX2 Find all number from 1-1000 that have 9 in them.

#Nine = [number for number in range(0,1000) if '9' in str(number)]
#print(Nine)

#EX3 Given string:
# text = 'In this lecture we will review some additional functionalities of python built-in data structures.'
# calculate how many words have letter e in it.

text = ('In this lecture we will review some additional functionalities of python built-in data structures.')




















#EX4 Given the same string as in previous exercise:
# calculate count of words that have more than 5 characters
#text = ('In this lecture we will review some additional functionalities of python built-in data structures.')

#words = [letter for letter in text.split() if len(letter) > 5]

#print(len(words))


#EX5 Given the same string calculate the occurrence of each letter in the string.
# (HINT: store everything in dictionary)

text = ('In this lecture we will review some additional functionalities of python built-in data structures.')

occurrence = set(text)

dict_store = {letter: text.count(letter) for letter in occurrence}

print(dict_store)


#EX6 Write a program that checks if given number is a perfect square.
#perfect square are number that can 16, 9, 25, 100, 4
import math

# Creating A List
Numbers = [4, 16, 17, 11, 36, 82,
           81, 49, 110, 120, 100]

# Printing the original array
#print("The original List is : ", Numbers)

# Using List comprehension to find perfect squares
perfect_squares = [i for i in Numbers if (
        math.sqrt(i) == math.floor(math.sqrt(i)))]

# Printing the perfect squares
print("The perfect squares are: ", perfect_squares)

































