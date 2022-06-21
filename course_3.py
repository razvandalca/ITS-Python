# # x = 10
# # y = 20
# #
# # total = x + y
# # print(total)
# # total2 = x - y
# # print(total2)
# # total3 = x * y
# # print(total3)
# # total4 = y / x
# # print(total4)
# #
# # # total5 = x / 0
# # # print(total5)
# #
# # x = 7
# # y = 3
# # print(x)
# # print(y)
# # total6 = x%y
# # print(total6)
# #
# # x = 11
# # y = 2
# # print(x/y)
# # print(x//y)
# #
# # x = 2
# # y = 5
# # print(x**y)
#
# # x = "Mere"
# # y = "Pere"
# # total = x +y
# # print(total)
# #
# # x = 5
# # y = "10"
# # total2 = y*x
# # print(total2)
# # total3 = y*-1
# # print(total3)
#
# # x=5
# # print(x)
# # x = x + 3
# # x += 3
# # print(x)
# # x = 10
# # y = 20
# # print(x < 30 and y >= 20)
# # print(x <= 10 or y > 20)
# # print(not(x > 5 and y > 15))
#
#
# # text = "azvan, salut!"
# # print("R" not in text)
#
# # total = 3 + 5 * 2 + (3 *2)
# # print(total)
#
#
# # my_list = ["mar","banana", "kiwi"]
# #
# # print(type(my_list))
#
#
# # my_list = list(("mar", "banana", "kiwi"))
# # print(*my_list)
#
#
# # my_list = ["mar", "banana", "kiwi"]
# # print("kiwi" in my_list)
#
#
# # my_list2 = ["mar", True, 2.5]
# # my_list2[0] = True
# #
# # print(my_list2[:2])
#
#
# # my_list = [1,2,3,4,5,6,7,8,9,10]
# # print(my_list[9])
# # my_list[1:3] = ["a", "b", "c", "d", "e"]
# # print(my_list)
# # print(my_list[9])
#
#
# # my_list = [1,2,3]
# # my_list.append(4)
# # print(my_list)
# #
# #
# # my_list.insert(1, "Salut")
# # print(my_list)
# #
#
# my_list = [1,3,3]
# my_list2 = [4,5,6]
# b = my_list.extend(my_list2)
# a = my_list.count(3)
# print(b)


# my_list = [1,2,3,4,5,6,7,8]
#
#
# print(my_list)
# a = my_list.pop(5)
#
# print(a)
# print(my_list)
# my_list.clear()
# print(my_list)


# a = [1,2,3]
# b = list(a)
# print(a)
# print(b)
# a.append(4)
# print(a)
# print(b)


fruits = ['apple', 'bannana', 'cherry ']
print(fruits[2])
fruits[1] = "kiwi"
print(fruits)
fruits[1:2] = ['mar', 'cireasa']
print(fruits)

masini = ['volvo', 'dacia', 'aro']
fruits.extend(masini)
print(fruits)

# fruits.remove('aro')
# print(fruits)
# a = fruits.pop(4)
# print(a)
print(fruits.remove('aro'))
print(fruits.pop(4))