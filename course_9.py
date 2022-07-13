# fruits = ['banana', 'apple', 'cherry','kiwi']
#
# new_list = []
#
# for fruit in fruits:
#     if 'a' in fruit:
#         new_list.append(fruit)
#
# print(new_list)
# new_list2 = [fruit for fruit in fruits if 'a' in fruit]
# print(new_list2)

# newlist = [expression for item in iterable if condition == True]

# Create a new list with elements from 0 to 10

# no_list = []
#
# for number in range(0,11):
#     if number < 6:
#         if number % 2 ==0:
#             no_list.append("Par")
#         else:
#             no_list.append("Impar")
#
# # newlist = [x if x != "banana" else "orange" for x in fruits if "a" in x]
# no_list2 = ["PAR" if number%2==0 else "IMPAR" for number in range(0,11) if number < 6]
# print(no_list)
# print(no_list2)


# Exercises


# Creeaza o lista in care sa ai toate numerele de la 0 - 1000

# my_list = [x for x in range(0, 1001)]
# print(my_list)

# Creeaza o noua lista in care sa avem numerele divizibile cu 8

# my_list = [number for number in range(0, 1001) if number%8 ==0]
# print(my_list)


# Creeaza o noua lista in care apar doar numerele care contin 6
# my_list = [x for x in range(0,1001) if '6' in str(x)]
# print(my_list)


# Pornind de la lista fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# Creeaza o noua lista in care avem fructele cu litere mari

#
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# new_list = [fruit.upper() for fruit in fruits]
# print(new_list)


my_list = [0, 22, 41, 63, 82, 101, 122, 143, 167, 181]


# Creeaza o noua lista folosind for in care sa adaugam doar elementele pare

# my_new_list = []

# for i in my_list:
#     if i %2 ==0:
#         my_new_list.append(i)
#
# print(my_new_list)

# Creaza o noua lista folosind list comprehension in care sa fie doar elementele pare

# my_other_new_list = [i for i in my_list if i%2==0]
# print(my_other_new_list)


# Creeaza o lista folosind for loops in care daca elementul este par adaugam “Even” altfel daca elementul este impar adaugam “Odd”

# my_new_list =[]
#
# for element in my_list:
#     if element%2 ==0:
#         my_new_list.append("Even")
#     else:
#         my_new_list.append("Odd")
#
# print(my_list)
# print(my_new_list)

# Creeaza o lista folosind list comprehension  in care daca elementul este par adaugam “Even” altfel daca elementul este impar adaugam “Odd”

# # newlist = [x if x != "banana" else "orange" for x in fruits if "a" in x]
# my_other_new_list = ["Even" if element%2==0 else "Odd" for element in my_list]
# print(my_other_new_list)

# a = "test"
# def my_function(nume="Gigi"):
#     rezultat = "salutare"+nume
#     return rezultat
#
#
# result = my_function("razvan")
# result2 = my_function("Bogdan")
# result3 = my_function()
# print(result)
# print(result2)
# print(result3)

# def add_function(x, y):
#     return x+y
#
# def inumultire(x,y):
#     result = x*y
#     return result
#
# # result1 = add_function(3,5)
# # result2 = add_function(35,5)
#
# print(inumultire(add_function(3,5), add_function(35,5)))
#
# def is_string_present(string_to_look, string_for_looking):
#     return string_for_looking in string_to_look
#
# first_string = "Ana are mere"
# second_string = "mere"
#
# if is_string_present(first_string, second_string):
#     print('Am gasit')
# else:
#     print('Nu am gasit')


# Scrie o functie care sa returneze daca elementul primit este par

# def parity_function(number_to_verify):
#     return number_to_verify % 2 == 0
#
#
# print(parity_function(2))
# print(parity_function(21))
# print(parity_function(2112))



# Scrie o functie care sa iti returneze o lista cu toate elementele pare pana la limita primita ca si argument
# newlist = [item for item in iterable if condition == True]

# def create_even_list(min_number, max_number):
#     return [item for item in range(min_number,max_number+1) if item%2 ==0]
#
# #
# # print(create_even_list(10,20))
#
#
# # Scrie o functie care sa calculeze suma unei liste de numere primite ca si argument
#
# def sum_list(a_list):
#     result_sum = 0
#     for number in a_list:
#         result_sum += number
#     return result_sum
#
# even_list = create_even_list(0,10)
# our_sum = sum_list(even_list)
# print(our_sum)
