# fruitsList = ["Mango","Apple","Orange","Guava"]
#
#
# # x = 0
# #
# # while x < len(fruitsList):
# #     pop_fruti = fruitsList.pop()
# #     print(pop_fruti)
# #     print(fruitsList)
#
#
# print(bool(fruitsList))
# print(fruitsList)
# while fruitsList:
#     fruitsList.pop()
#
# print(bool(fruitsList))
# print(fruitsList)


# my_dict = {"name": "Razvan"}
#
# if my_dict:
#     print("ARE ELEMENTE")

# if not my_dict:
#     print("NU ARE ELEMENTE ")


# Write a program that tells the user if a list is not empty
# my_list = []
#
# if my_list:
#     print("ARE ELEMENTE")
# else:
#     print("NU ARE")

# Given two lists, l1 and l2, write a program to create a third list l3 by picking an odd-index element from the list l1 and even index elements from the list l2.

# l1 = [3, 6, 9, 12, 15, 18, 21]
# l2 = [4, 8, 12, 16, 20, 24, 28]
#
# l3 = []
# if len(l1) == len(l2):
#     for index in range(0, len(l1)):
#         if index % 2 == 0:
#             l3.append(l2[index])
#         else:
#             l3.append(l1[index])
# else:
#     for index in range(0, len(l1)):
#         if index % 2 == 1:
#             #  Aici index este impar
#             l3.append(l1[index])
#
#     for index in range(0, len(l2)):
#         if index % 2 == 0:
#             #  Aici index este par
#             l3.append(l2[index])
#
# print(l3)


# Write a quiz game application.
# Questions
# Each question has 3 answers from which only one is correct
# Minimum 5 questions
# Each correct answer values 1 point
# Show final score
# Bonus: Make the quiz ‘multi-player’

# FORMAT OF QUESTION POSIBIL NU NEAPARAT
# example_question = {
#     "question": "What does Hulk do ?",
#     "answer1": "SMASH!",
#     "answer2": "SCREAM!",
#     "answer3": "BAKE!",
# }
#
# example_question1 = {
#     "question": "What does Hulk do ?",
#     "answer": ["SMASH", "SCREAM", "BAKE"],
#     "correct_answer": "SMASH"
# }
#
# exemple_for_me_razvan = {
#     "question": "What does Hulk do ?",
#     "answers": [ {
#             "correct" : True,
#             "anwser_data": "Smash !"
#         }]
#     }

