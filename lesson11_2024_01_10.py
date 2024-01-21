# def check_integers(*args):
#     for item in args:      #check
#        if type(item) !=  type(1): #to check if they are integers
#            return False
#
#            return True
#
#
# print(check_integers(1, 2, 3))
#
# print(check_integers("0", "0", 1, 5, 9))
#
# print(check_integers("1", "2"))


# def check_integers(name, *args):
#
#     print(name)
#     for item in args:      #check
#        if type(item) !=  type(1): #to check if they are integers
#            return False
#
#            return True
#
#
# print(check_integers("Petras", 1, 2, 3))
#
# print(check_integers("p", "0", 1, 5, 9))
#
# print(check_integers("jonas", "1", "2"))
#
# print((check_integers(5)))


#
# def are_adults(**kwargs):
#     for name, age in kwargs.items():
#print(key, value)

#     if age < 18:
#       return False
#     return True
#
# print(are_adults(jonas=25, tadas=15, lina=36))
# print(are_adults(petras=19, dovydas=21))
#
# #def integer_division(num_one=10, num_two=2):
#     #return num one //num two
#
# def are_adults(reason, **kwargs):
#     print(reason)
#
#     for name, age in kwargs.items():
# #print(key, value)
#
#     if age < 18:
#       return False
#     return True
#
# print(are_adults("night club", jonas=25, tadas=15, lina=36))
# print(are_adults("sell cigarettes", petras=19, dovydas=21))

#Have all of them in one function
# def my_function(a, b, args, c=10, d=20, **kwargs):
#
#     print(a, b)
#     print(args)
#     print(c, d)
#     print(kwargs)
#
# my_function(1, 2, 3, 4, 5, c=5, d=15, e=20, f=30, g=40)
#
# def multiply(x, y):
#     return x * y
# print(multiply(2, 4))
#
#
# multiply = lambda x, y: x*y
#
# print(multiply(2, 4))

# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# def uppercase(word):
#     return word.upper()
#
#
# print(list(map(lambda word: word.upper(), ['cat', 'dog', 'cow'])))


#EX 1
# Write a function that takes two lists and adds the first
# element in the first list with the first element in the second list,
# the second element in the first list with the second element in the second list, etc, etc.
# Return True if all element combinations add up to the same number. Otherwise, return False.
# Example:
# puzzle_pieces([1, 2, 3, 4], [4, 3, 2, 1]) ➞ True
# # 1 + 4 = 5;  2 + 3 = 5;  3 + 2 = 5;  4 + 1 = 5
# # Both lists sum to [5, 5, 5, 5]
# puzzle_pieces([1, 8, 5, 0, -1, 7], [0, -7, -4, 1, 2, -6]) ➞ True
# puzzle_pieces([1, 2], [-1, -1]) ➞ False
# puzzle_pieces([9, 8, 7], [7, 8, 9, 10]) ➞ False
#Solutions

# list_one = [1, 2, 3, 4, 5, 6, 7, 8, 9, ]
# list_two = [9, 8, 7, 6, 5, 4, 3, 2, 1,]
# list_three = []
# count = 0
# def function3(list1, list2):
#      if len(list1) != len(list2):
#       return False
# for index, item in enumerate(list1):        list_three.append(list1[index] + list2[index])
# for number in list_three:
# if number != list_three[0]:
# return True
# print(function3(list_one, list_two))

#OR
# def sum_elements(list1, list2):
#     sum_list = []
#     for i in range(len(list1)):
#         sum_list.append(list1[i] + list2[i])
#     if len(list1) != len(list2):
#         return False
#     else:
#         return len(set(sum_list)) == 1
# list1 = [1, 2, 3, 1]
# list2 = [4, 3, 2, 2]
# print(sum_elements(list1, list2))
#
# #OR
#
# def sum_elements(list1, list2):
#     sum_list = map(sum, zip(list1, list2))
#     if len(list1) != len(list2):
#         return False
#     else:
#         return len(set(sum_list)) == 1
# list1 = [1, 2, 3, 3]
# list2 = [4, 3, 2, 2]
# print(sum_elements(list1, list2))
#>>>>>>>>>>>>>>>>>>>>>

#EX2 There's a great war between the even and odd numbers.
# Many numbers already lost their lives in this war and it's your task to end this.
#You have to determine which group sums larger: the evens or the odds. The larger group wins.
# Create a function that takes a list of integers, sums the even and odd numbers separately,
# then returns the difference between the sums of the even and odd numbers.
# Example:
# war_of_numbers([2, 8, 7, 5]) ➞ 2
# # 2 + 8 = 10
# # 7 + 5 = 12
# # 12 is larger than 10
# # So we return 12 - 10 = 2
# war_of_numbers([12, 90, 75]) ➞ 27
# war_of_numbers([5, 9, 45, 6, 2, 7, 34, 8, 6, 90, 5, 243]) ➞ 168

# #solution1
# def even_odd_war(user_list):
#     even_sum = sum([i for i in user_list if i % 2 == 0])
#     odd_sum = sum([i for i in user_list if i % 2 != 0])
#     return f'{max(even_sum, odd_sum)} - {min(even_sum, odd_sum)} = {max(even_sum, odd_sum) - min(even_sum, odd_sum)}'
#
# user_list = [5, 9, 45, 6, 2, 7, 34, 8, 6, 90, 5, 243]

# print(even_odd_war(user_list))

#OR

# def even_odd_war(user_list):
#     odd_list = []
#     even_list =[]
#     for item in user_list:
#         if item % 2 == 0:
#             even_list.append(item)
#         else:
#             odd_list.append(item)
#     return sum(even_list) - sum(odd_list)
#
# print(even_odd_war([5, 6, 19, 11, 1111, 15, 1000]))
#
# #OR
#
# number_list = [1, 2, 3, 4, 5, 6]
# def calculate_odd_even(odd_number, even_number):
#     odd_number = 0
#     even_number = 0
#     t1 = tuple()
#     for i in number_list:
#         if i % 2 == 0:
#             even_number = even_number + number_list[i]
#             t1.append(i)
#
#     else:
#             odd_number = odd_number + number_list[i]
#     t1.append(i)
#     return odd_number
#     return even_number
#
# my_tuple = calculate_odd_even("odd_number, even_number")

#EX3You are given an input array of bigrams, and an array of words.
# Write a function that returns True if every single
# bigram from this array can be found at least once in an array of words.

# Example:
#
# can_find(["at", "be", "th", "au"], ["beautiful", "the", "hat"]) ➞ True
# can_find(["ay", "be", "ta", "cu"], ["maybe", "beta", "abet", "course"]) ➞ False
# # "cu" does not exist in any of the words.
# can_find(["th", "fo", "ma", "or"], ["the", "many", "for", "forest"]) ➞ True
# can_find(["oo", "mi", "ki", "la"], ["milk", "chocolate", "cooks"]) ➞ False
#
#Solution
# function canFind(bigrams, words) {
#     let sentense = words.join(" ")
#     return bigrams.length === bigrams.filter(bia => {
#         return sentense.includes(bia)
#     }).length
# }








