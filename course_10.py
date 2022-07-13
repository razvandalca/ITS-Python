# Create a list with elements from 0 to 100 using list comprehension

# my_list = [number for number in range(0,101)]
# print(my_list)

# Given the list  lst1=[1,2,3,4,5] create an identical list from the first list using list comprehension.

# lst1=[1,2,3,4,5]
# my_list = [i for i in lst1]
# print(my_list)


# Given a list lst1=[2, 4, 6, 8, 10, 12, 14], using list comprehension, construct a new  list from the squares of each element in the list lst1.

# lst1=[2, 4, 6, 8, 10, 12, 14]
# new_list = [x**2 for x in lst1]
# print(new_list)

# Given a list of numbers original_list = [2,3.75,.04,59.354,6,7.7777,8,9], create a new list without float numbers using list comprehension

# list1 = [2,3.75,0.04,59.354,6,7.7777,8,9]

# no_float_list = [int(i) for i in list1]
# no_float_list = [i for i in list1 if i == int(i)]
# print(no_float_list)

# Create a function to reverse a string.

# def string_rev(string_to_reverse):
#     return string_to_reverse[::-1]
#
#
#
# reversed_string = string_rev("Salut sunt Razvan")
# print(reversed_string)


# Create a function that accepts a string and calculate the number of upper case letters.

# def uppercase_letters(string_to_verify):
#     counter = 0
#     for letter in string_to_verify:
#         if letter.isupper():
#             counter += 1
#
#     return counter


# uppecarse_letters_no = uppercase_letters("Salut Razvan")
# print(uppecarse_letters_no)


# Create a function that squares up a list of numbers and returns the new list with the numbers squared

# def square_my_list(lst):
#     return [number**2 for number in lst]
#
# print(square_my_list([1,2,3]))


# Create a function that removes all vowels from a string given as argument and returns the new string.

# def vowels_remove(text_to_remove):
#     vowels_letters = ['a', 'e', 'i', 'o', 'u']
#     result = [letter for letter in text_to_remove if letter.lower() not in vowels_letters]
#     return ''.join(result)
#
# print(vowels_remove("Ana are mere"))

# Incearca sa rescrii quiz game-ul folosind functii (unde este posibil).


# score = 10
# def function_one():
#     global score
#     score +=20
#
# print(function_one())
# print(score)


# def function_one():
#     def function_add():
#         print("TEST")
#
#     function_add()
#     function_add()
#     function_add()
#
# function_one()


# def test_function(command_one, *args):
#     print(type(args))
#     print(args)
#     print(command_one)
#
#
# test_function("Razvan","Test","Hello")


# def talk_to_robot(robot_name, command):
#     print(f'Apelare comanda {command} pentru robot {robot_name}')
#
#
# def talk_to_robot_V2(robot_name, *commands):
#     for command in commands:
#         print(f'Apelare comanda {command} pentru robot {robot_name}')
#

# talk_to_robot("R2D2","Mergi Inainte")
# talk_to_robot("R2D2","Mergi Derapta")
# talk_to_robot("R2D2","Mergi Stanga")
#
# talk_to_robot_V2("R2D2","Mergi Inainte","Mergi Derapta", "Mergi Stanga")

# def talk_to_robot(robot_name, command):
#     print(f'Apelare comanda {command} pentru robot {robot_name}')
#
# talk_to_robot("R2D2","Mergi Inainte")
# talk_to_robot("Mergi Inainte", "R2D2")
#
# talk_to_robot(command="Mergi Inainte", robot_name="R2D2")


# def shopping_list(**kwargs):
#     print(type(kwargs))
#     print(kwargs)
#
#
# shopping_list(bannana=20,apple=10,cherry=25)


# def factorial(number):
#     if number == 0:
#         return 1
#     return number * factorial(number-1)
#
# print(factorial(3))


# try:
#     a = 1 + "2"
# except (KeyError, TypeError) as variable:
#     print("TESTS")
#     raise
# except SyntaxError as variable:
#     print("E SyntaxError error ")
#
# print("Am ajuns la linia 151")



# def my_function(a,b):
#     result = 0
#     try:
#         result = a/b
#     except ZeroDivisionError as error:
#         print(f"Could not devide elements {error}")
#     except TypeError as error:
#         print(f"Could not devide elements {error}")
#     else:
#         print(result)
#
#
# my_function(2,2)


# file  = open("test.txt", "a")
# file.write("SALUT25")
# file.close()

# with open("/Users/razvandalca/Desktop/Work/test.txt", "a") as file:
#     file.write("Salut\n")


# file  = open("test.txt", "r")
#
# # print(file.readlines())
# for line in file:
#     print(line)


# import os
#
# os.remove('test.txt')