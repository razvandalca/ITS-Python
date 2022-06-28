# Retrieve from the user using the input() method 5 numbers and print the average
# counter = 0
# sum_total = 0
#
# while counter < 5:
#     user_number = float(input())
#     sum_total += user_number
#     counter +=1
#
# print(sum_total)

# counter = 0 < 5 => True
# user_number = 20
# sum_total  =20
# counter =1


# counter =1 < 5 => True
# user_number =10
# sum_total =30
# counter =2

# counter =2 < 5 => True
# user_number = 10
# sum_total  =40
# counter =3

# counter =3 < 5 => True
# user_number = 10
# sum_total  =50
# counter =4

# counter =4 < 5 => True
# user_number = 10
# sum_total  =60
# counter =5


# counter =5 < 5 => False
# printam sum_total

# print(f"Average {sum_total/5}")


# Pop all elements from the list fruitsList = ["Mango","Apple","Orange","Guava"] using a while loop


# fruitsList = ["Mango","Apple","Orange","Guava"]


# x = 0
#
# while x < len(fruitsList):
#     pop_fruti = fruitsList.pop()
#     print(pop_fruti)
#     print(fruitsList)
#
#
# while len(fruitsList) > 0 :


# x = 0  -> 0<4 =>True
# pop_fruti = "Guava"
# "Guava"
# ["Mango","Apple","Orange"]

#  x =0 - > 0<3 => True
# pop_fruti = "Guava"
# "Orange"
# ["Mango","Apple"]

#  x =0 - > 0<2 => True
# pop_fruti = "Apple"
# ["Mango"]

#  x =0 - > 0<2 => True
# pop_fruti = "Apple"
# ["Mango"]

#  x =0 - > 0<1 => True
# pop_fruti = "Mango"
# []


#  x =0 - > 0<0 => False


# Printing the items in a tuple using while loop

# fruitsList = ["Mango","Apple","Orange","Guava"]
#
#
# fruitsTuple = tuple(fruitsList)
#
# i = 0
# while i < len(fruitsTuple):
#     print(fruitsTuple[i])
#     i+=1


# Write a program that will tell if a dictionary is empty or not

# dictionary = {"a":22}
#
# if len(dictionary) == 0:
#     print("GOL")
# else:
#     print("Nu e gol!")


# Write a program that will compute the factorial of a number imputed by the user (using while loops)

# user_no = int(input())
#
# i = 1
# result = 1
#
# while i <= user_no:
#     result *= i
#     i += 1
#
# print(result)


# user_no = 5
#  i = 1 -> 1<=5 =>True
# result = 1*1 =>1
#  i = 2
#  i = 2 -> 2<=5 =>True
# result = 1*2 =>2
#  i = 3
#  i = 3 -> 3<=5 =>True
# result = 2*3 =>6
#  i = 4
#  i = 4 -> 4<=5 =>True
# result = 6*4 =>24
#  i = 5
#  i = 5 -> 5<=5 =>True
# result = 24*5 => 120
#  i = 6
#  i = 6 -> 6<=5 =>False
# print result => 120


# user_no = int(input())
#
# result = 1
#
# while user_no > 0:
#     result *= user_no
#     user_no -=1
#
# print(result)

# The user will input 5 numbers (one at a time)  print the min and the max values


# min_num = max_num = float(input("Introduceti primul nr: "))
#
# i = 1
# while i < 5:
#     number = float(input(f"Intrducteti nr {i + 1}: "))
#     if number < min_num:
#         min_num = number
#     elif number > max_num:
#         max_num = number
#     i += 1
#
# print(f"Max {max_num}")
# print(f"MIN {min_num}")


# Finding the sum of numbers in a list using while loop


# my_list = [1,5,2,3,6,7,4]
#
# sum_numere = 0
# i = 0
# while i < len(my_list):
#     sum_numere = sum_numere + my_list[i]
#     i +=1
#
# print(sum_numere)


# Number guessing game, we want to create a game where the user needs to guess the number the computer is thinking of.

# import random
#
# start_no = 1
# end_no = 10
# chosen_number = random.randint(start_no, end_no)
#
# print(f'Ghiceste un numar intre {start_no} si {end_no}')
# state_continue = True
# my_number = 0
# while my_number != chosen_number:
#
#     my_number = int(input())
#     if my_number > chosen_number:
#         print("Go lower!")
#     elif my_number < chosen_number:
#         print("Go higher !")
#     else:
#         print("You guessed it!")


#  Add guess limit


# import random
#
# start_no = 1
# end_no = 10
# chosen_number = random.randint(start_no, end_no)
# incercari = 3
# counter = 0
#
# print(f'Ghiceste un numar intre {start_no} si {end_no}')
# print(f"Ai {incercari} incercari !")
# while counter < incercari:
#
#     my_number = int(input())
#     if my_number > chosen_number:
#         print("Go lower!")
#     elif my_number < chosen_number:
#         print("Go higher !")
#     else:
#         print("You guessed it!")
#         break
#
#     counter += 1
#     if counter == incercari:
#         print("Ai pierdut!")
#
#
# print(f"The correct answer {chosen_number}")



