# Using sliceing

# l1 = [3, 6, 9, 12, 15, 18, 21]
# l2 = [4, 8, 12, 16, 20, 24, 28]
#
# l3=[]
#
# odd_index = l1[1::2]
# print(odd_index)
# even_index = l2[0::2]
# print(even_index)
#
#
# l3.extend(odd_index)
# l3.extend(even_index)
#
# print(l3)
#


# question_1 = {
#     'question': 'What does the fox say ?',
#     'answers': [
#         {
#             'answer': 'Ta-Ta-Ta!',
#             'option': 'A',
#             'correct': True
#         },
#         {
#             'answer': 'IDK',
#             'option': 'B',
#             'correct': False
#         },
#         {
#             'answer': 'Woof!',
#             'option': 'C',
#             'correct': False
#         },
#     ]
# }
# question_2 = {
#     'question': 'What does the bear say ?',
#     'answers': [
#         {
#             'answer': 'Pow!',
#             'option': 'A',
#             'correct': False
#         },
#         {
#             'answer': 'Moooor',
#             'option': 'B',
#             'correct': True
#         },
#         {
#             'answer': 'Woof!',
#             'option': 'C',
#             'correct': False
#         },
#     ]
# }
#
# question_3 = {
#     'question': 'What does the dog say ?',
#     'answers': [
#         {
#             'answer': 'Miau!',
#             'option': 'A',
#             'correct': False
#         },
#         {
#             'answer': 'Chit!',
#             'option': 'B',
#             'correct': False
#         },
#         {
#             'answer': 'Woof!',
#             'option': 'C',
#             'correct': True
#         },
#     ]
# }
#
# questions = [question_1, question_2, question_3]
# possible_answer = ['A', 'B', 'C']
# player_names = []
#
# players_no = int(input("How many players ? :"))
# i = 0
#
# # Save player names into a list
# while i < players_no:
#     player_name = input(f"Please add player {i} name")
#     player_names.append(player_name)
#     i+=1
#
# # Pentru fiecare jucator dorim sa rulam codul din interior (printat intrebari , raspunsuri ,asteptat raspusn , validat raspuns)
# for player in player_names:
#     print(f'Player {player} turn !')
#     score = 0
#     # Cliclam prin dictionarele de intrebari din lista questions
#     for question_dict_data in questions:
#         # Printam intrebarea
#         print(question_dict_data['question'])
#         # Cliclam prin dictionarele de raspun din lista de answers din cadrul dictionarului  question_dict_data
#         for answer_dict_data in question_dict_data['answers']:
#             # Printam fiecare optiune de raspuns
#             print(f"{answer_dict_data['option']}-{answer_dict_data['answer']}")
#
#         # Cerem input de la user
#         user_input = input("Chose A,B,C:")
#
#         # Daca inputul nu e ok printam not acceptble
#         if user_input not in possible_answer:
#             print("Not Acceptable!")
#             continue
#         # Ciclam prin dictionarele de raspunsuri
#         for answer_dict_data in question_dict_data['answers']:
#             # Verificam daca user inputul este corect sau nu
#             if user_input == answer_dict_data['option'] and answer_dict_data['correct']:
#                 print("Bravo!")
#                 score+=1
#             elif user_input == answer_dict_data['option'] and not answer_dict_data['correct']:
#                 print("Wrong!")
#     print(f'Player {player} - {score} points!')
#
#



# Write a hangman game:
# The words are in a list and one of them is chosen randomly
# User selects a letter , if present in word , the letter reveals itself
# The user has 5 lives, game ends if the user finds all letters of the word or runs out of lives

# import  random

# words = ['casa', 'python', 'masina', 'autobuz']


# Version1
# chosen_word =words[random.randint(0, len(words) -1)]
# print(chosen_word)

# Version2
# chosen_word = random.choice(words)
# lives = 5
# print(chosen_word)
# guess_word = "_" * len(chosen_word)
# print(guess_word)
# user_guessed_letters_correctly = set()
#
# while True:
#     user_input = input("Specify a letter:")
#     if len(user_input) > 1:
#         print("PLease add only one character!")
#         continue
#
#     if user_input in chosen_word:
#         user_guessed_letters_correctly.add(user_input)
#     else:
#         lives = lives-1
#     guess_word = ""
#     for letter in chosen_word:
#         if letter in user_guessed_letters_correctly:
#             guess_word = guess_word+letter
#         else:
#             guess_word = guess_word+"_"
#     print(guess_word)
#     print(f'Lives {lives}')
#     if guess_word == chosen_word:
#         print("Congrats!")
#         break
#     if lives == 0:
#         print("Sorry, try again!")
#         break
#


# Hangman V2 prima si ultima litera la vedere
# words = ['casa', 'python', 'masina', 'autobuz']
#
# chosen_word =words[random.randint(0, len(words) -1)].upper()
#
# print(chosen_word)
#
# hangman_word = chosen_word[0] + "_"*(len(chosen_word)-2) + chosen_word[-1]
#
# hangman_word = list(hangman_word)
#
# for i in range(0, len(chosen_word)):
#     if chosen_word[i] == chosen_word[0] or chosen_word[i] == chosen_word[-1]:
#         hangman_word[i] = chosen_word[i]
#
#
# backup_word = hangman_word
# hangman_word = str()
#
# for i in range(0, len(backup_word)):
#     hangman_word = hangman_word +backup_word[i]
#
#
#
#
# for i in range(0, 5):
#     if i == 4:
#         print("Ultima sansa")
#     else:
#         print(f"Mai ai {5-i}")
#
#     print(hangman_word)
#
#     print("Enter a letter or the word:")
#     user_input = input().upper()
#     if user_input == chosen_word:
#         print("Congrats, this is the word!")
#         print(chosen_word)
#         break
#     else:
#         for j in range(0, len(chosen_word)):
#             if chosen_word[j] == user_input:
#                 hangman_word = list(hangman_word)
#                 hangman_word[j] = user_input
#                 backup_word = hangman_word
#                 hangman_word = str()
#                 for x in range(0, len(backup_word)):
#                     hangman_word = hangman_word +backup_word[x]
#
#     if i < 5 and hangman_word == chosen_word:
#         print("This is the chosen word !")
#         print(chosen_word)
#         break
#     elif i == 4 :
#         print("Ai pierdut!")


