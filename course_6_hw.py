# Write a program that finds and prints the largest number from a list of lists

#
# my_list = [2,[-12, -33, -55], 3, 4, [-2, -2, -19], [-32, -2, -1], 30]
#
# if type(my_list[0]) == int:
#     # my_list = [2,[-12, -33, -55], 3, 4, [-2, -2, -19], [-32, -2, -1], 30]
#     bigest_no = my_list[0]
# elif type(my_list[0]) == list:
#     # my_list = [[-12, -33, -55], 3, 4, [-2, -2, -19], [-32, -2, -1], 30]
#     bigest_no = my_list[0][0]
#
# for i in my_list:
#     print(i)
#     if type(i) == int:
#         if i > bigest_no:
#             bigest_no = i
#     else:
#         for j in i:
#             print(j)
#             if j > bigest_no:
#                 bigest_no = j
#
# print(f"BIGEST NO : {bigest_no}")


# Version 2

# my_list = [[-12, -33, 55],[-2, -2, -19], [-32, -2, -1]]
#
#
# big_no = my_list[0][0]
#
# results = []
# for i in  my_list:
#     # [-12, -33, 55]
#     max_from_i = max(i)
#     results.append(max_from_i)
#     # if max_from_i > big_no:
#     #     big_no = max_from_i
#
# print(max(results))


# Write a program that will compute the factorial of a number imputed by the user (using for loops)

#
# num = int(input("enter a no: "))
# fact = 1
#
# if num < 0:
#     print("Only positive no!")
# elif num == 0:
#     print("Fact of 0 is 1")
# else:
#     for i in range(1, num + 1):
#         fact = fact * i
#     print(f"The factorial of {num} is {fact} ")


# Finding the sum of numbers in a list using for loop

# my_list = [1,2,3,4,5,6,7,8,9]
#
# sum = 0
#
# for i in my_list:
#     sum +=i
#
# print(sum)


my_list = [[1, 2], [3, 4, 5, 6], [7, 8, 9]]

sum_total = 0
# for i in my_list:
#     for j in i:
#         sum += j
#
# print(sum)

#
# for i in my_list:
#
#     sum_total += sum(i)
# print(sum_total)


# import  random
#
# chosen = random.randint(1,14)
# print(chosen)

# Get all values from the dictionary and add them to a list but don’t add duplicate (use for loops and do it without for loops)

# data = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
#
# values = data.values()
# result = []
# for i in values:
#     # if i not in result:
#     #     result.append(i)
#     if i in result:
#         continue
#     else:
#         result.append(i)
#
# print(result)


# result_set = set(values)
# result_list = list(result_set)
# print(result_list)


# result = list(set(data.values()))
# print(result)


