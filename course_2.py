# my_string = 'Test "\'string'
# print(my_string)
#
# my_string_two = "Test '\"string 2"
# print(my_string_two)
#
# my_string_three = "Test \\n string 3"
# print(my_string_three)
# my_string_four = 'I\'m alive'
# print(my_string_four)
#
# big_text = '''Pentru ca
#  o sa
#  putem face
# asta'''
# print(big_text)
#
# big_text_two = """Si aici
# merge bine pe
# mai multe
# randuri
# """
# print(big_text_two)
#
# """
# Urmatorul cod este special.
# """


# a = 'ACASA'
# print(a)
# print(a[3])
# print(a[0])
# print(len(a))
# print(a[3:4])

numere = "0123456789"

# print(numere[0:9:3])

# print(numere[:5]) # daca start_index nu e specificat by default e 0
# print(numere[5:]) # daca stop_index nu e specificat by default e len(numere)-1

# print(numere[len(numere)-2:])
# print(numere[-2::])
# print(numere[len(numere)-1:-4:-1])
# print(numere[::-1])

# quantity = 20
# fruit = "Mere"
# price = 50
#
# text = "Vreau {} bucati de {}  la pretul de {} RON"
# print(text.format(quantity, fruit, price))
#
# text_2 = "La pretul de {2} RON, vreau sa cumpar {0} {1}"
# print(text_2.format(quantity, fruit, price))
#
# text_3 =f"Vreau {quantity} bucati de {fruit} la pretul de {price} RON"
# print(text_3)


# text = " ana are mere"
# text_modificat = text.strip()
# print(text)
# print(text_modificat)
# print(text)

# text = "razvan are mere"
# print(text.upper())


# Exercitiul 1
# text = "Hello World"
#
# print(text[0])
# print(text[2:5])
# print(text[::-1])

# Exercitiul 2

# varsta = 28
# nume = "Razvan"
#
# my_string =f"Numele meu este {nume} am {varsta} ani"
# print(my_string)
#
# my_string2="Numele meu este {} am {} ani"
# print(my_string2.format(nume, varsta))
#
# my_string3="Numele meu este {1} am {0} ani"
# print(my_string3.format(varsta, nume))

# text = "HeHllo World"
# print(text.replace('H','J'))


# x = 5
# y = -5
#
# print(x, y)
#
#
# x = 2.5
# y = 2,5
#
# print(type(x))
# print(type(y))
#
# x = 0.01e2
# print(x)


# x = 3j
# print(type(x))


# print(3>5)
# print(10>5)
# print(10==10)


# print("Care esete numele tau ?")
# input_value = input()
# print(type(input_value))
# print(f"Salut {input_value}!")


# x = int(float(input("X:")))
# y = float(input("Y:"))
#
# total = x+y
#
# print(f"Total {total}")


# x = float("avc")
# print(type(x))
# print(x)

nume = input("Nume: ")
prenume = input("Prenume: ")
greutate = float(input("Greutate: "))
inaltime = int(input("Inaltime: "))
oras = input("Oras: ")
observatii = input("Observatii: ")
print(f"""
Fisa medicala
Nume: {nume}
Prenume: {prenume}
Greutate: {greutate} kg
Inaltime: {inaltime} cm
Oras:{oras.capitalize()}
Observatii: {observatii} 
""")
