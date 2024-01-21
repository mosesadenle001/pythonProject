#Lesson 04: Dictionary Data Structures continue
#my_dictionary = {"Name": "Karina", "Surname": "Klinkeviciute", "Age": 44}
#
# print(my_dictionary["Name"])
#
# print(my_dictionary["Surname"])
#
# print(my_dictionary["Age"])

#change value in dictionary
#my_dictionary = {"Name": "Karina", "Surname": "Klinkeviciute", "Age": 44}
#
# my_dictionary['Name'] = 'Asta'
#
# print(my_dictionary["Name"])
#
# my_dictionary['Surname'] = 'Kalaseviciute'
#
# print(my_dictionary['Surname'])

# my_dictionary['Name', 'Surname', 'Age'] = 'Monika', 'Kalaseviciute', '26'
#
# print(my_dictionary['Name', 'Surname', 'Age']) #output ('Monika', 'Kalaseviciute', '26')

#Droping or delete Keys from dictionary by USING "del"

#del my_dictionary["Surname"]

#print(my_dictionary)

#add surname back
#my_dictionary["Surname"] = "Smith"

#print(my_dictionary)

# my_dictionary["City"] = "Kaunas"
#
# print(my_dictionary)
#KEY cannot be a list[1, 2],bcoz list can change, but can be value in a dictionary, also dictionary like {"a": "b"}: cannont be a KEY
# however, it can be tuples(1, 2) immutable or unchange, integers, strings, Booleans value True or false and float 1.0
#KEY Can also be Empty string "": but only Once
#All keys has to be unique we cannot has same word as a key in our value

##nested dictionary
# #More complex, nested structures dictionary inside another dictionary
# from pprint import pprint   #from pprint is a module and import pprint is a function using instead of print
# my_dictionary = {
# 	"name": "Albert",
# 	"surname": "Einstein",
# 	"occupation": {
# 		"role": "Professor",
# 		"workplace": "University of Berlin"
# 	},
#         "languages": ["German", "Latin", "Italian", "English", "French"]}

# print(my_dictionary["occupation"])  #output {'role': 'Professor', 'workplace': 'University of Berlin'}
# print(my_dictionary["occupation"]["role"])  # output Professor
##print(languages)  #output ['German', 'Latin', 'Italian', 'English', 'French']


#anguage = my_dictionary["languages"][2]  #2 is indexes from the languages

#print(language)  #output Italian

#Acess KEY and VALUE Seperately
# dictionary = {"a": 10, "b": 20, "c": 30}
# dictionary2 = {"e": 100, "f": 200}




# print(dictionary.items()) #output dict_items([('a', 10), ('b', 20), ('c', 30)]) as tuples
# print(list(dictionary.items()))  #output [('a', 10), ('b', 20), ('c', 30)]
# print(dictionary.keys())  # output dict_keys(['a', 'b', 'c'])
# print(dictionary.values())  # output dict_values([10, 20, 30])

#Pop item in dictionary

#value = dictionary.pop("b")
#
# print(value)   #output dict_values 20
#
# print(dictionary)  #output {'a': 10, 'c': 30}

#UPDATE to joined dictionary together

# print(dictionary)  #output {'a': 10, 'b': 20, 'c': 30}
# print(dictionary2) #output {'e': 100, 'f': 200}
# dictionary.update(dictionary2)
#
# print(dictionary) #output {'a': 10, 'b': 20, 'c': 30, 'e': 100, 'f': 200}

#print(len(my_dictionary["occupation"]))  #output 2
#print(len(dictionary)) #output 3

#nested dictionary
#
# dictionary = {"a": 10, "b": 20, "c": 30}
# #updating dictionary inside of another dictionary
# my_dictionary["occupation"].update(dictionary)

#you can automatically import pprint by pressing Alt and enter on keyboard
#pprint(my_dictionary)  # OUTPUT using pprint he update by adding dictionary into occupation
# #{'languages': ['German', 'Latin', 'Italian', 'English', 'French'],
 # 'name': 'Albert',
 # 'occupation': {'a': 10,
 #                'b': 20,
 #                'c': 30,
 #                'role': 'Professor',
 #                'workplace': 'University of Berlin'},
 # 'surname': 'Einstein'}

#Two dictionary with same and different KEY
# dictionary = {"a": 10, "b": 20, "c": 30}
# dictionary2 = {"e": 100, "f": 200}
#
# dictionary.update(dictionary2)

#print(dictionary) # output without same KEY {'a': 10, 'b': 20, 'c': 30, 'e': 100, 'f': 200}

#dictionary = {"a": 10, "b": 20, "c": 30}
#dictionary2 = {"b": 100, "f": 200}

#dictionary.update(dictionary2)
#print(dictionary)  #output {'a': 10, 'b': 100, 'c': 30, 'f': 200}

#update from Tuple to dictionary

#dictionary.update([("g", 45), ("h", 56)])

#print(dictionary)  #output {'a': 10, 'b': 20, 'c': 30, 'g': 45, 'h': 56}
#dictionary.update(i=78, j=89) #output {'a': 10, 'b': 20, 'c': 30, 'g': 45, 'h': 56, 'i': 78, 'j': 89}

#print(dictionary)

#LOOP  in dictionary
# dictionary = {"a": 10, "b": 20, "c": 30}
# dictionary2 = {"b": 100, "f": 200}
# dictionary.update(dictionary2)
#
# dictionary.update([("g", 45), ("h", 56)])
# dictionary.update(a=78, b=89)

#for item in dictionary:

#print(item) #output he print only KEYS
# a
# b
# c
# g
# h
# i
# j

#for key in dictionary:
	#print(key) #output he print only KEYS
# a
# b
# c
# g
# h
# i
# j

#OR ANOTHER WAY TO GET OUR KEY
#for key in dictionary.keys():
	#print(key)  #output same above

#for both KEY and VALUE
#for key, value in dictionary.items():
	#print(key, value) #output
# a 78
# b 89
# c 30
# f 200
# g 45
# h 56

#for value in dictionary.values():
    #print(value)  #output
# # 78
# 89
# 30
# 200
# 45
# 56

#Create an empty list or empty dictionary
#my_list = []
#OR
#my_list = list()

#my_dict = {}
#OR
# my_list = dict[]
#
# #ALSO
# my_list = [1, 2, 3]
# #OR
# my_list = list()
#
# my_dict = {"a": 1, "b": 2}
# #OR
# my_dict = dict()

#Converting or combine two lists into a dictionary
#zip function joined list and value together in a list of tuple
#dist function indicate that we are using dictionary

# keys = ["Alberts", "Tom", "Stephen"]
# values = [1, 4, 5]
# new_dictionary = dict(zip(keys, values))

#print(new_dictionary) #output {'Alberts': 1, 'Tom': 4, 'Stephen': 5}


#SET Item repeat ONLY Once
# Set items are unchangeable, but you can remove items and add new items.

# my_set = {2, 5, 8}
#
# print(my_set)  #output {8, 2, 5}
#
# my_set = {2, 5, 8, 5, 2}
#
# # print(my_set) #output {8, 2, 5}
#
# #creat a set from the list below
# my_list = [23, 56, 89, 12, 45, 78, 12, 78, 56]
#
# my_set = set(my_list)
#
# print(my_set) #output {12, 45, 78, 23, 56, 89} it remove duplicate item
#
# my_set.add(100)
#
# print(my_set) #output {100, 12, 45, 78, 23, 56, 89}
#
# my_set.remove(45)
#
# print(my_set)  #output {100, 12, 78, 23, 56, 89}
#
# value = my_set.pop()
#
# print(value) #output 100 pop the first value as we did not specify

#EX 1 Write python program that asks user to enter name,
# # surname, age. Put these values into a dictionary and print it.
# # ent_name = input("Enter your name: ")
# ent_surname = input("Enter your surname: ")
# ent_age = int(input("Enter your age: "))
#
# my_dict = {"name": input("Enter your name:"), "surname": ent_surname, "age": ent_age}
#
# print(my_dict)  #output
# # Enter your surname: Adenle
# # Enter your age: 35
# # Enter your name:Akin
# # {'name': 'Akin', 'surname': 'Adenle', 'age': 35}

#EX2 Try creating nested dict structure which would use all data types and structures you already know.
# my_dictionary = {
# 	"name": "Albert",
# 	"surname": "Einstein",
# 	"occupation": {
# 		"role": "Professor",
# 		"workplace": "University of Berlin"
# 	},
#         "languages": ["German", "Latin", "Italian", "English", "French"]}

# print(my_dictionary["occupation"])  #output {'role': 'Professor', 'workplace': 'University of Berlin'}
# print(my_dictionary["occupation"]["role"])  # output Professor
##print(languages)  #output ['German', 'Latin', 'Italian', 'English', 'French']

#EX3 Create a program, that would take sentences from the input
# and create a dictionary where they keys represents letters
# and values the frequency those letters appeared in those sentence.
# The program must demand that user should enter 3 or more sentences.

# sentence_length = 4
# sentemces = []
# for item in range (4):   #check every each sensense
#  sentence = input('Enter you sentence').lower()
# sentemces.append(sentence)
#
# #print(sent)
# character_counts = {}
# for sentence in sentemces: #each every character in the sentenses
#     for character in sentence:          #character is the KEY
#         character_counts[character] = character_counts.get(character, 0)+1

#print(character_counts)
# .get is used to get the later and count the latter if it is an existing letter if not existing it return 0

#OR ANOTHER WAY
# sentence_length = 4
# sentemces = []
# for item in range (4):   #check every each sensense
#  sentence = input('Enter you sentence').lower()
# sentemces.append(sentence)
# print(sentense)
#
# character_counts = {}
# for sentence in sentemces: #each every character in the sentenses
#     for character in sentence:          #character is the KEY
#         #character_counts[character] = character_counts.get(character, 0)+1  #OR character_counts[character] += 1
#       if character in character_counts.keys():
# #or if character in character_counts, # means that check if existing
#     character_counts[character] += 1
#     #quike way to add 1 to the empty character_counts
#
# else:    #means if the charecter does not exit then we create it one
#  character_counts[character] = 1
#
#  print(character_counts)

#EX 4
# Create a dictionary of student names and their grades: Store student names as keys and their
# grades as values in a dictionary.
# Calculate the average grade of all students:
#
# Use sum() and len() functions to calculate the total and number of grades, respectively, and then divide the total by the number to get the average.
# Remove students with grades below 80 from the dictionary:
#
# Create a set of student names with grades below 80.
# Check if a specific student exists in the dictionary:
#
# Input a student name from the user.
# Use the in operator to check if the student name exists in the dictionary.
# Print a message indicating whether the student name is found or not.

# #student = {"name": "grade"}
# number_of_student = int(input("Enter the number of student:"))
# student = {}
# for student in range(number_of_student):
#     student_name = input("Enter the student name: ")
#     student_grade = int(input("Enter their grades"))
#     student[student_name] = student_grade
#
#     print(student)
#
#     grade_of_student = sum(student.values())/len(student.values())
#
#     print(f"Grade of student is {grade_of_student}")
#
# new_student = {}
# for name, grade in student.items():
#     if grade >= 80:
#         new_student[name] = grade
#
#         print(student)

#EX4 ANOTHER WAY

# my_students_dict = {"Tomas": 85, "Tadas": 87, "Lukas": 78, "Imanuelis": 100,
# "Silvija": 99, "Simas": 59, "Laimonas": 49}
# my_values = list(my_students_dict.values())
# my_lenght = (len(my_values)) #len reikia imti is verciu, o ne is pradinio saraso, kvaily tu, gerai, kad supratai
# my_sum = sum(my_values)
# print(my_lenght)
# print (my_sum)
# x = my_sum/my_lenght
# print(x)
#
# new_students_dict = {}
# new_students_set = set()
# for student, grade in my_students_dict.items():
#     if grade < 80:
# new_students_set.add(student)
# else:
# new_students_dict[student] = grade
#
#     print(new_students_dict)
#     print(new_students_set)
#     name = input("Enter please a name ")
#     if name in new_students_dict:
#         print("students grade is above 80")
# else:
#         print ("none")





