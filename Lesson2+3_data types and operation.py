# # String type operation
#
# letter = "a"
#
# letter2 = "b"
#
# name = "Karina"
#
# company = "Code Academy"
#
# sentence = "I really enjoy learning python"
#
# age = "55 years"
#
# age2 = "9 months"
#
# print(company)
#
# name_company = name + company
#
# print(name_company)
#
# #result/output KarinaCode Academy
#
# letter = "a"
#
# letter2 = "b"
#
# name = "Karina"
#
# company = "Code Academy"
#
# sentence = "I really enjoy learning python"
#
# age = "55 years"
#
# age2 = "9 months"
#
# print(company)
#
# name_company = name + " " + company
# # if you add empty string to complete the sentence
# # output Karina Code Academy
# print(name_company)
#
# letter = "a"
#
# letter2 = "b"
#
# name = "Karina"

#company = "Code Academy"

# sentence = "I really enjoy learning python"
#
# age = "55 years"
#
# age2 = "9 months"
#
# print(company)
#
# name_company = name + " works at " + company
#
# print(name_company)
#
# # f stands for formating string " "
# # we add variable in curly braces: {}
# # f - string is the most common method of formating
# name_company2 = f"{name} works at {company} "
#
#
# print(name_company2)
#
# greeting = "Hello, my name is"
# name = "Tom"
#
# greeting_name = greeting + " " + name
# print(greeting_name)
#
# greeting = "Hello, my name is "
#
# name = "Aleksas"
#
# like = "i live in kaunas, i love to play football"
#
# completed_greeting = f"{greeting} {name} {like}"
# print(completed_greeting)
#
# name_company2 = f"{name} works at {company} "

# name_company3 = "{} works at {}".format(name, company)
#
# print(name_company3)

#output Aleksas works at Code Academy
# name = "Aleksas"
# company = "Code Academy"
#
# name_company3 = "{0} works at {1}".format(name, company)
#
# print(name_company3)

#output Aleksas works at Code Academy

#name = "Aleksas"
#company = "Code Academy"

#name_company3 = "{1} works at {0}".format(name, company)

#print(name_company3)

#output Code Academy works at Aleksas

########String indexes starting from 0
# String slicing
#company = "Code Academy"

#@print(company [-4])
#output d

#print(company[5:12])
#output Academy

#print(company[5:10])
#output Acade

#company = "Code Academy is great"

#print(company[5:])
#output Academy is great

#print(company[:4])
#output Code

#print(company[5:12:2])
#output- Aaey #print every 2rd letter
#print(company[5:12:3])
#output- Ady #print every 3rd letter

#print(company[::-1])
#output taerg si ymedacA edoC #read id backward

#print(f"{company[2:5]} {company[12:20]}")
#output  de   is grea   #add two slices with one print

#print(company[5])    #output- A #4th character from the beginning
#print(company[-5])   #output- g #4th chanacter from the end

##ords = company.split()

#print(words)  #output- ['Code', 'Academy', 'is', 'great']

#print(company.upper()) #output- CODE ACADEMY IS GREAT

#print(company.casefold())  #output- code academy is great

#print(company.replace("Code", "Coding")) #output- Coding Academy is great

#print(company.replace("C", "K")) #Output- Kode Academy is great

#print(company.replace("d", "D")) #Output- CoDe AcaDemy is great

#print(company.replace("a", "A", 2)) #output- Code AcAdemy is greAt

#print(company.replace("e", "E",2).replace("d", "D"))  #OUTPUT-CoDE AcaDEmy is great

#string adding each sentense together

# sentence = 'he siad "your dog is nice"'
#
# sentence2 = "let's eat"
#
#sentence3 = 'let\'s eat'
#
# sentence4 = 'he siad "let\'s eat"'

#print(len(sentence3))  #len is used to calculate the lenth number of character in a sentence

#
# print(sentence)
# print(sentence2)
# print(sentence3)
#print(sentence4)   #output he siad "your dog is nice"
# let's eat
#let's eat
#he siad "let's eat"

#\ backslid is a continuasion of the same line

#CONVERSION OF TYPES STRING
#text = "100"     #text as a numner

# number = int(text)  #int= interger which convert text to number
#
# print(number)   #output- 100
#
# print(number * 2)  #output- 200
#
# print(text * 3) # output- 100100100

#number = float(text)

#print(number * 3) # output- 300.0 float with bullet . decimal point

# text = "hello" CANNOT BE CONVERTED

# number = 45
#
# text = str(number)
#
# print(text * 3) # output 454545
#
# number_float = float(number)
# print(f"floating point number: {number_float}") #output floating point number: 45.0

#basically we cannot convert string to interger or float E.G "Hello" to number

#VARIATIONS NAME CONERSION

#USER INPUT

#name = input()
#
# print(name) #output Nothing you need to enter something in the outout section
#
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# # print(name)
# # print(age)

# CONVERT STRING TO NUMBER USING INT

# number1 = (input("Enter first number: "))
# number2 = (input("Enter second number: "))
#
# number3 = number1 * number2

#print(number3) #TypeError: can't multiply sequence by non-int of type 'str'
#
# number1 = int(input("Enter first number: "))
# number2 = int(input("Enter second number: "))
#
# number3 = number1 * number2

#print(number3) #output  10 and 30 bring 300

#Excercises lesson2

# question 1
# Create a program that allows user to enter his/her name and age
# Calculate the year user was born
# Print the answer to the terminal



#question 4
# Create program that allows user to enter text
#Convert that text to Leet speak 1337
#Print outcome

# text = input("enter text: ")
# text_leet = text.replace("d", "l)")
#
# print(text_leet) # output- laba l)iena
#
# text_leet = text_leet.replace("a", "@")
#
# print(text_leet) # output- l@b@ l)ien@
#
# text_leet = text_leet.replace("e", "3")
#
# print(text_leet) #output- l@b@ l)i3n@
#
# #also another way to do it is call Chain which allow us to combine all value together
# print(text.replace("d", "l)").replace("a", "@").replace("e", "3"))


#5. Write a Python program to get a single string from two given strings,
# separated by a space and swap the first two characters of each string.
#Sample String : 'abc', 'xyz'
#Expected Result : 'xyc abz'
#
# text1 = "abc"
# text2 = "xyz"
#
# text1a = text2[:2] + text1[2:]
# text2a = text1[:2] + text2[2:]
#
# print(text1a + " " + text2a)  #output- xyc abz








# #company = "Code Academy is great"
#
# company = company.replace("a", "4")
# company = company.replace("b", "8")
# company = company.replace("c", "<")
# company = company.replace("d", "l")
#
# #print(company)  # output Cole A<4lemy is gre4t
#
# #print(leet)






















































