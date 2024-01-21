# #Lesson 03: Data Structures
# #----List
# #my_integer_list = []  # empty integer list
# #my_integer_list2 = [1, 2, 4, 9, 15] # Integer list
#
# string_list = ["good", "day", "good", "we", "are", "learning"]
#
# joint_various_list = ["hi", 1, 5, "code", "academy"]
#
# #my_integer_list2.append(25) #.append means ADD more new value or items at the END of list
#
# #print(my_integer_list2)   #output [1, 2, 4, 9, 15, 25]
#
# #my_integer_list2.insert(2, 3) #add new element in the list. you can used index to select where to the position, in this case we ADD under second index
#
# #print(my_integer_list2) #output- [1, 2, 3, 4, 9, 15, 25]
#
# #my_integer_list2.remove(9)
#
# #print(my_integer_list2)
#
# #my_integer_list2.pop()  # pop used for removing element in the list and it will removed last element is nothing specify
#
# #print(my_integer_list2)  # output [1, 2, 3, 4, 15]
#
# #my_integer_list2.pop(2)  #2 is index using by pop to removed item
#
# #print(my_integer_list2)  #output [1, 2, 4, 15]
#
# #removed_item = my_integer_list2.pop(2)
#
# #print(my_integer_list2)  #output- [1, 2, 15]
#
# #print(removed_item) #output- 4
#
# # my_integer_list2 = [1, 2, 4, 2, 2, 2, 2, 9, 15]
#
# #count the element of list 2 in the list bellow
# #print(my_integer_list2.count(2))  #output- 5
#
# #count the element of string good bellow
# string_list = ["good", "day", "good", "we", "are", "learning"]
#
# #print(string_list.count("good")) #output- 2
#
# #Add string + list or various together
# #new_list = string_list + my_integer_list2
#
# #print(new_list) #output- ['good', 'day', 'good', 'we', 'are', 'learning', 1, 2, 4, 2, 2, 2, 2, 9, 15]
#
# #OR another way by using EXTEND
#
# #my_integer_list2.extend(joint_various_list)
#
# #print(my_integer_list2) #output- [1, 2, 4, 2, 2, 2, 2, 9, 15, 'hi', 1, 5, 'code', 'academy']
#
# #my_integer_list2.append(string_list)
#
# #print(my_integer_list2) #output- ['good', 'day', 'good', 'we', 'are', 'learning']]
#
# #print(my_integer_list2[4]) #output- 2 base on the index
#
# #print(my_integer_list2[9])  #output- hi base on index 9
#
# #print(my_integer_list2[13][2]) #output- a
#
# #LEN function used to know now many element in the list
# # list_length = len(my_integer_list2)
#
# #print(list_length) #output- 14
#
# #print(len(joint_various_list))  #output- 5
#
# #print(len(string_list)) # output- 6
#
# #MAX AND MIN Function cannot combine both lists and string
# # my_integer_list3 = [1, 2, 4, 9, 15, 2, 2, 2, 2,]
# # print(max(my_integer_list3))  # output 15
# #
# # print(min(my_integer_list3))  # output 1
# #
# # print(min(string_list)) # output are /bcoz of first alfarbert a
# #
# # print(max(string_list)) # output- we /Bcoz of max alfabert w
#
# #SORT- Function
# # my_integer_list3.sort()
#
# #print(my_integer_list3)  #output- [1, 2, 2, 2, 2, 2, 4, 9, 15]
#
# #print(sorted(string_list)) #['are', 'day', 'good', 'good', 'learning', 'we']
#
# #INDEXES continue on my_integer_list3
# # my_integer_list3[2] = 5
#
# # print(my_integer_list3) #output-[1, 2, 5, 2, 2, 2, 4, 9, 15] /changing index base 2 into 5
# #
# # print(my_integer_list3[:5]) #output- [1, 2, 5, 2, 2]
# #
# # print(my_integer_list3[5:])  #output- [2, 4, 9, 15]
#
# #print(my_integer_list3[::2])  #output-[1, 5, 2, 4, 15]/not correct/ should gave two interval
#
# #print(my_integer_list3[::-1])  #output-[15, 9, 4, 2, 2, 2, 5, 2, 1]/ not correct/ should reverse the list
#
# #METHOD .append AND FUNCTION len
# # Iterating over elements within the list
#
# list = [1, 5, 9, 7, 5, 3, 2, 4, 8, 6, 12, 65, 78]
#
# list2 = [1, 2, 3, 4]
#
# # for item in list:
#   # print(item)
#  #          print(item + 100)
#  # print(item * item)
# for item in list2:
#    list.insert(3, item)
#
# print(list)  #output from index 3 under 7- [1, 5, 9, 4, 3, 2, 1, 7, 5, 3, 2, 4, 8, 6, 12, 65, 78]
#
# print(100 in list)  #output- false
# print(5 in list)
#
# #integer and string can ADD together you need to convert integer to string first
# #Example
# print(str(item) + " EUR ") #OUTPUT-4 EUR
#
# #TUPLE, using this sign parentheses and comma (,) simplify list that cannot change
# #tuple is good when you know that you do not want to change or constant your data and
# # it is good bcoz it doesnt Add diff Methods during when using it
# my_tuple = (1, 2, 3, 9, 7, 8)
#
# my_tuple[3] = 5
# print(my_tuple)  #output it bring error bcoz tuple cannot change value

# Exercises EX1
# Write a python program that sums up all items in the list
# (all items are integers or floats in list, create a list yourself).
# my_list = [1, 13, 4, 9, 1]

# list_sum = 0
# for item in my_list:
#     list_sum = list_sum + item
#     print(list_sum)
# Note we can use Debugger to check our result or output

# EX2
# Write a python program that multiplies all items in the
# list (all items are integers or floats in list, create a list yourself).
# my_list = [1, 2, 5, 2, 3]
#
# list_product = 1
# for item in my_list:
#     list_product =  list_product * item
#     print(list_product)

#EX3
#Write a python program that gets maximum value from the list
# (all items are integers or floats in list, create a list yourself)

# list1 = [10, 30, 2.5, 60]
#
# max_value = list1[0]
# for item in list1:
#    if item > max_value:
#     max_value = item
#
#     print(max_value)

#EX4
#Write a python program that concatenates all strings
# in the list (all items are strings, create a list yourself).
# string_list = ["kaunas", "lagos", "vilnius", "berlin", "london"]
#
# concatanate_str = ""
# for item in string_list:
#     concatanate_str += item
#
#     print(concatanate_str)
#
# #EX5
# #Create two lists and add them together,
# # make sure it works the way you want it to
#
# my_list = [1, 13, 4, 9, 1]
# string_list = ['good', 'rich', 'beautiful', 'healthy', 'smart']
#
# item1 = 0
# for item2 in string_list[::-1]:
#     my_list.insert(item1, item2)
#     item1 += 2
#     print(my_list)

# EX 6
#Write a python program that asks user to
# enter 3 integers and find the highest value entered.
#
# number_one = int(input("Enter number 1: "))
# number_two = int(input("Enter number 2: "))
# number_three = int(input("Enter number 3: "))
#
# my_tuple = (number_one, number_two, number_three)
# high = my_tuple[1]
# for item in my_tuple:
#     if item > high:
#         high = item
#
#         print(high)

#OR another way to solve the Ex6

# input_times = int(input("Enter how many number: "))
# number = [float(input("Enter your number: ")) for item in range(input_times)]
# max_num = number[0]
# for item in number:
#     if item > max_num:
#         max_num = item
#
#         print(max_num)

#EX 10
#Write a Python program to find the list of words that are longer than n
# from a given list of words.

# given_list = [ 'good', 'rich', 'beautiful', 'healthy', 'smart']
# new_list = []
#
# n = int(input('Enter the length: '))
# for item in given_list:
#     if len(item) > n:
#         new_list.append(item)
#
# print(new_list)

#EX 11
#Write a Python function that takes two lists and
# returns True if they have at least one common member.
#
# list_1 = ['car', 'truck', 'bike']
# list_2 = ['apartment', 'bike', 'condo', 'flat']
# for item in list_1:
#  if item in list_2:
#
#     print('yes it exist',)


















