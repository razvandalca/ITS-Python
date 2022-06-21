# Homework C3
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# my_list[0]= 10
# my_list[9]= 1

# Solutie 1
# x = my_list[0]
# y = my_list[len(my_list)-1]
#
# new_list=my_list[1:len(my_list)-1]
# new_list.append(x)
# new_list.insert(0, y)
# print(new_list)

# Solutie 2
# my_list[0], my_list[-1] = my_list[-1], my_list[0]
# print(my_list)

# Solutie 3
# first_element = my_list.pop(0)
# last_element = my_list.pop()
#
# my_list.append(first_element)
# my_list.insert(0, last_element)

# print(my_list)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# my_list.remove(10)
# print(my_list)

# my_list[2]=my_list[2]**2
# my_list[2] **= 2

# print(22 in my_list)
# print(my_list.count(22) != 0)

# salut_list = ["salut", "sunt ", "Razvan"]
# my_list.extend(salut_list)
# print(my_list)

# a = my_list.pop(10)
# print(a)

# my_list[3:4] = [99,100]
# print(my_list)
# my_list.clear()
# print(my_list)

# my_tuple = (1, 2, True, False,33,55,66)
# a, b, c, *d = my_tuple
# print(a)
# print(b)
# print(c)
# print(d)

# a, b, *c, d, f = my_tuple
# print(a)
# print(b)
# print(c)
# print(d)
# print(f)


# my_tuple =(1,2,3)
# print(my_tuple)
#
# my_list = list(my_tuple)
# my_list[0] = "a"
#
# print(my_list)
# my_tuple = tuple(my_list)
# print(my_tuple)


# my_tuple1 = (1,2,3)
# my_tuple2 = (3,4,5)
# my_tuple3 = my_tuple1+my_tuple2
# print(my_tuple3)

# my_tuple1 = (1,2,3)
# my_tuple2 = my_tuple1*3
# print(my_tuple2)

# Exercitii

# my_tuple = ("a", "b", "c", "d", "e", "f", "g")
#
# # a, b, *c = my_tuple
# a, *b, c = my_tuple
#
#
# print(a)
# print(b)
# print(c)

# my_tuple = ("a", "b", "c", "d", "e", "f", "g")

# Solutia 1
# one_element_tuple = ("h",)
# new_tuple = my_tuple + one_element_tuple
# print(new_tuple)

# Solutia 2
# my_list = list(my_tuple)
# my_list.append("h")
# my_tuple = tuple(my_list)
# print(type(my_tuple))
# print(type(my_list))
# is_in_my_tuple = "a" in my_tuple
# print(is_in_my_tuple)


# my_tuple = (1, 2, True, [15, 20], "test")
# my_list = my_tuple[3]
# value = my_list[1]
# print(my_tuple[3][1])
# print(value)


# Sets

# my_set = {-1, 2, 4}
# # my_set.add(33)
# # print(my_set)
# # my_set.update((44,55,66))
# # print(my_set.discard(3))
#
# print(my_set.pop())


# my_set = {1,2,3,4}
# my_set2 = {3,4,5}

# # print()
# resulting_set = my_set.difference(my_set2)
# print(resulting_set)
# print(my_set)
# my_set.difference_update(my_set2)
# print(my_set)



# print(my_set.intersection(my_set2))

# print(my_set2.issubset(my_set))

# print(my_set.issuperset(my_set2))

# print(my_set.symmetric_difference(my_set2))

# print(my_set.union(my_set2))


# Exercitii

# my_set = {1,2,3,'a','b','c'}
# my_set.update([4,5,6])
#
# print(my_set)

# my_list = ["a", "sa", "rr", "ff", 1]
#
#
# my_set = tuple(my_list)
#
# my_list2 = list(my_set)
#
# print(my_list)
# print(my_set)
# print(my_list2)

# set_one = {'ra', 'raz', 'python',5}
# set_two = {1,2,3, 'ra', 'raz', 'python',6}


# print(set_one.issubset(set_two))

# print(set_one.symmetric_difference(set_two))


#  -- Dictionare
#  -- IF ELSE
# -- LOOPS  -- FOR --WHILE LOOPS
# -- ERROR HANDELEING




