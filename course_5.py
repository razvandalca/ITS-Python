# my_dict = {
#     "name": "Razvan",
#     "age": 28,
#     "city": "Arad"
#
# }
#
# print(my_dict)
#
#
# my_dict_2 = dict((("name","Razvan"), ("age", 28)))
# print(my_dict_2)

#
# my_dict = {
#     "name": "Razvan",
#     "age": 28,
#     "city": "Arad",
#     "house_number" : 28,
#     "my_info": {
#         "cnp":"12313123124124124412"
#     }
# }

# print(my_dict.get("age_to_die"))
# print(my_dict["age_to_die"])
#
# print(28 in my_dict)

# print(my_dict)
# my_keys = my_dict.keys()
# my_values = my_dict.values()
# my_items = my_dict.items()
#
# print(my_keys)
# print(my_values)
# print(my_items)


# my_dict = {
#     "name": "Razvan",
#     "age": 28,
#     "city": "Arad",
#     "house_number" : 28
# }

# my_dict["inaltime"] = 180
# print(my_dict)
#
# new_value = (("culoare_ochi", "Albastru"),)
# my_dict.update(new_value)
# print(my_dict)

# my_dict["house_number"] = 100
# print(my_dict)
# my_dict.update((("age",20), ("name","Toma"), ("city","Bucuresti")))
# print(my_dict)

# print(my_dict.pop("age"))
# print(my_dict)
# print(my_dict.pop("test_key", 0))


# print(my_dict.popitem())
# print(my_dict)
# print(my_dict.popitem())
# mom_dict = {"name": "Monica"}
# mom = "mom"
# family = {
#     "dad": {
#         "name": "Stefan"
#     },
#     mom: mom_dict
# }
# print(family)

#
# my_dict = {
#     "name": "Razvan",
#     "age": 28,
#     "city": "Arad",
#     "house_number" : 28
# }
# print(my_dict.get("test",30))
# print(my_dict)
# print(my_dict.setdefault("test",30))
# print(my_dict)


car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
# print(car["model"])
# print(car.get("color", "red"))

# Solutie 1
# car.setdefault("color", "red")
# print(car)

# Solutie 2

# car["color"] = "red"
# print(car)

# Solutie 3
# car.update((("color", "red"),))
# print(car)


# posible_colors = ["red", "black","grey"]
# car["color"] = posible_colors
# print(car)

# owner = car.setdefault("owner_name", "Raluca")
# print(owner)
# print(car)


#  IF Part

a = 123
b = 12

# if a < b:
#     print("A")
# elif a == b:
#     print("==")
# elif a > 100:
#     print("A MARE")
# elif b >10:
#     print("B")
# else:
#     print("ELSE")
#
# if b >10:
#     print("B")


# if a > b : print("A")

# print("A") if a>b else print("B")


# if a<b :
#     pass
# else:
#     print("A")


# x  =39.9

# if x >=  40:
#     print("X")
#     if x > 50:
#         print("Greater then 50")
#     else:
#         print("Greater then 50 but not greater then 40")
#
# elif x >39.5:
#     if x > 39.7:
#         print("x greater then 39.7")
# else:
#     print("X in the else clause ")


# counter = 0
# while counter < 10:
#     print(counter)
#     if counter == 5:
#         counter += 1
#         continue
#     counter += 1
#     print("Jumbo!")
#
#
#

# i = 1
# j = 1
#
# while i <= 3:
#     print(i, "Outer loop is executed")
#     while j <= 3:
#         print(j, "Inner loop is executed")
#         j += 1
#     i += 1


# i = 0
# while i <5 :
#     print("Salutare")
#     i+=1

my_string = "Hello"

# i = 0
# while i < len(my_string):
#     if my_string[i] == "e" or my_string[i] == "o":
#         print(f"Element exclus {my_string[i]}")
#         i += 1
#         continue
#     print(my_string[i])
#     i += 1


# my_string = "Hello"
#
# i = 0
#
# while i < len(my_string):
#     if my_string[i] == "l":
#         break
#     else:
#         print(my_string[i])
#     i += 1
# listm = [1]
# if listm :
#     print("A")
# else:
#     print("B")