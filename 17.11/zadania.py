# zadanie 1.5
# x = int(input("Proszę podać liczbę:"))
# result = x / 2 + 4
# assert result == 14

# zadanie 2.1
# first_name = input("Wprowadź swoje imię: ")
# last_name = input("Wprowadź swoje nazwisko: ")
# print(f"Cześć {last_name} {first_name}")

# zadanie 2.2 (to musi być po kropce, a jak jest w nazwie przecinek to wtedy przecinek)
# file_name = input("Proszę podać nazwę pliku:")
# print(file_name.split('.')[1])

# zadanie 2.3
# dd = input('Podaj dzień: ')
# mm = input('Podaj miesiąc: ')
# yyyy = input('Podaj rok: ')
# print(f'{dd}/{mm}/{yyyy}')

# zadanie 2.4
# lc1 = int(input("podaj liczbe całkowitą:"))
# lc2 = int(input("podaj liczbe całkowitą:"))
# r = lc1 + lc2
# print(f"suma {lc1} oraz {lc2} to {r}") 

# zadanie 2.5
# x = int(input("podaj liczbę całkowitą:"))
# y = int(input("podaj liczbę całkowitą:"))
# z = float(input("podaj liczbę zmiennoprzecinkową:"))
# a = float(input("podaj liczbę zmiennoprzecinkową:"))

# wynik1 = x + z
# wynik2 = y - a

# print(f"Wynik operacji 1: {wynik1}")
# print(type(wynik1))
# print(f"Wynik operacji 2: {wynik2}")
# print(type(wynik2))

# suma = wynik1 + wynik2

# print(f"Suma to: {suma}")
# print(type(suma))

# # zadanie 2.6
# a = int(input("podaj liczbe:"))
# b = int(input("podaj pierwiastek:"))

# print(f'Wynik to {a**(1/b)}')

# zadanie 2.7 (zdrobilam dobrze!!)
# słowo1 = str(input("podaj słowo:"))
# słowo2 = str(input("podaj słowo:"))

# print(f'{słowo1} {słowo2}')
# print(słowo1, słowo2, sep=", ")
# print(słowo1, end=" ")
# print(słowo2)

# zadanie 2.8
# a = float(input("podaj długość bok1:"))
# b = float(input("podaj długość bok2:"))
# c = float(input("podaj długość bok3:"))

# p = (a + b + c)/2
# pole = (p * (p - a) * (p - b) * (p - c)) ** 0.5
# print(f'Pole trójkąta wynosi: {pole:.2f}')

# zadanie 2.9 (1 kilometr to 0,621371192 mili)
# km = float(input("podaj odległość w km:"))
# mile = 0.621371192 * km
# print(f'{km:.2f} kilometra to {mile:.2f} mili')

# zadanie 2.10 ((°C x 9/5) + 32 =°F)
# cel = float(input("Podaj temperaturę w Celsjuszach: "))
# fahr = (cel * 9 / 5) + 32
# print(f"{cel:.1f} stopni celsjusza to {fahr:.1f} stopni Fahrenheita")

# zadania inny plik: Kolekcje, sterowanie przepływem programu

# zadanie 1.1
# my_list = []

# my_list.append("Python")
# my_list.append("is ok")
# my_list.append("sometimes")

# my_list.remove("sometimes")
# my_list[1] = "is neat"

# assert my_list == ["Python", "is neat"]

# zadanie 1.2
# original = ["I", "am", "learning", "hacking", "in"]
# modified = original.copy()
# modified.append("Python")
# modified[3] = "lists"

# assert original == ["I", "am", "learning", "hacking", "in"]
# assert modified == ["I", "am", "learning", "lists", "in", "Python"]

# zadanie 1.3
# list1 = [6, 12, 5]
# list2 = [6.2, 0, 14, 1]
# list3 = [0.9]

# combo = list1 + list2 + list3
# my_list = sorted(combo, reverse=True)

# assert my_list == [14, 12, 6.2, 6, 5, 1, 0.9, 0]

#zadanie 1.2.1
# first_name = "John"
# last_name = "Doe"
# favorite_hobby = "Python"
# sports_hobby = "gym"
# age = 82

# my_dict = {"name": f"{first_name} {last_name}", 
# "age": age, 
# "hobbies": [favorite_hobby,sports_hobby]}
# # print(my_dict)

# assert my_dict == {"name": "John Doe", "age": 82, "hobbies": ["Python", "gym"]}

# # zadanie 1.2.2
# dict1 = dict(key1="This is not that hard", key2="Python is still cool")
# dict2 = {"key1": 123, "special_key": "secret"}
# # Można również zainicjalizować słownik przez wykorzystanie listy krotek
# dict3 = dict([("key2", 456), ("keyX", "X")])
# # Twoja implementacja
# my_dict = {**dict1, **dict2, **dict3}

# special_value = my_dict.pop('special_key')

# # Sprawdźmy czy otrzymaliśmy poprawny wynik
# assert my_dict == {"key1": 123, "key2": 456, "keyX": "X"}
# assert special_value == "secret"
# # Sprawdźmy czy słowniki początkowe nie zostały zmienione
# assert dict1 == {"key1": "This is not that hard", "key2": "Python is still cool"}
# assert dict2 == {"key1": 123, "special_key": "secret"}
# assert dict3 == {"key2": 456, "keyX": "X"}

# zadanie 1.3.1

# name = "John Doe"
# if len(name) > 20:
#     print(f'Name "{name}" is more than 20 chars long')
#     length_description = "long"
# elif len(name) > 15:
#     print(f'Name "{name}" is more than 15 chars long')
#     length_description = "semi long"
# elif len(name) > 10:
#     print(f'Name "{name}" is more than 10 chars long')
#     length_description = "semi long"
# elif len(name) in range(8, 11):
#     print(f'Name "{name}" is 8, 9 or 10 chars long')
#     length_description = "semi short"
# else:
#     print(f'Name "{name}" is a short name')
#     length_description = "short"
# # Sprawdźmy czy otrzymaliśmy poprawny wynik
# assert length_description == "semi short"

# zadanie 1.3.2
# words = ["PYTHON", "JOHN", "chEEse", "hAm", "DOE", "123"]
# upper_case_words = []
# for word in words:
#     if word.isupper():
#         upper_case_words.append(word)
# # Sprawdźmy czy otrzymaliśmy poprawny wynik
# assert upper_case_words == ["PYTHON", "JOHN", "DOE"]

# # zadanie 1.3.3
# magic_dict = dict(val1=44, val2="secret value", val3=55.0, val4=1)
# # Twoja implementacja
# sum_of_values = 0
# for key in magic_dict.keys():
#     if isinstance(magic_dict[key],(int, float)):
#         sum_of_values += magic_dict[key]
# # Sprawdźmy czy otrzymaliśmy poprawny wynik
# assert sum_of_values == 100
# # albo: sum_of_values = sum(value for value in magic_dict.values() if isinstance(value, (int, float)))


# # zadanie 1.3.4
# numbers = [1, 3, 4, 6, 81, 80, 100, 95]
# # Twoja implementacja
# my_list = []
# for number in numbers:
#     if number % 5 == 0 and number % 2 == 1:
#         my_list.append("five odd")
#     elif number % 5 == 0 and number % 2 == 0:
#         my_list.append("five even")
#     elif number % 2 == 1:
#         my_list.append("odd")
#     elif number % 2 == 0:
#         my_list.append("even")

# # Sprawdźmy czy otrzymaliśmy poprawny wynik
# assert my_list == [
#     "odd",
#     "odd",
#     "even",
#     "even",
#     "odd",
#     "five even",
#     "five even",
#     "five odd",
# ]


# zadanie 2.1

# # System oceniania
# 90-100, 5.0
# 75-89, 4.5
# 65-74, 4.0
# 60-64, 3.5
# 50-59, 3.0
# 0-49, 2.0

# points = float(input("Podaj liczbę punktów (0-100): "))

# # System oceniania
# if 80 <= points <= 100:
#     grade = 5.0
# elif 75 <= points < 80:
#     grade = 4.5
# elif 65 <= points < 75:
#     grade = 4.0
# elif 60 <= points < 65:
#     grade = 3.5
# elif 50 <= points < 60:
#     grade = 3.0
# else:
#     grade = 2.0

# # Sprawdzenie, czy student zaliczył
# if grade >= 3.0:
#     result = "Student zaliczył zadanie"
# else:
#     result = "Student nie zaliczył zadania"

# # Wyświetlenie wyniku
# print(f"Liczba punktów: {points}")
# # print(f"Uzyskana ocena: {grade}")
# # print(result)

# # drugie rozwiązanie
# score = {
#     (90, 100): 5.0,
#     (75, 89): 4.5,
#     (65, 74): 4.0,
#     (60, 64): 3.5,
#     (50, 59): 3.0,
#     (0, 49): 2.0
# }

# punkty = int(input("Podaj liczbę punktów: "))

# ocena = None
# for przedzial, ocena_wynik in score.items():
#     if przedzial[0] <= punkty <= przedzial[1]:
#         ocena = ocena_wynik
#         break

# print(f"Liczba punktów: {punkty}")
# if ocena >= 3.0:
#     print(f"Uzyskana ocena: {ocena}")
#     print("Student zaliczył zadanie")
# else:
#     print(f"Uzyskana ocena: {ocena}")
#     print("Student nie zaliczył zadania")

# zadanie 2.2

# month = input("Wprowadź miesiąc: ")
# seasons = {
#     ('1', '2', '3', 'styczeń', 'luty', 'marzec'): "zima",
#     ('4', '5', '6', 'kwiecień', 'maj', 'czerwiec'): "wiosna",
#     ('7', '8', '9', 'lipiec', 'sierpień', 'wrzesień'): "lato",
#     ('10', '11', '12', 'październik', 'listopad', 'grudzień'): "jesień",
# }
# # season = None
# # for key, value in seasons.items():
# #     if month in key:
# #         season = value
# #         break

# season = [value for key, value in seasons.items() if month in key][0]

# print(f'Pora roku dla miesiąca {month}: {season}')

# zadanie 2.3

# lista = ['tekst', 1, 1.5, True, [0]]
# print(len(lista))
# print(lista[0])
# print(lista[len(lista)//2])
# print(lista[-1])
# print(lista)
# lista.insert(0, "Pierwszy")
# lista.append("Ostatni")
# print(lista)

# # zadanie 2.4
# lista = [x for x in range(1,11)]
# print(lista)
 
# lista.sort(reverse = True)
# print(lista)
 
# nowa_lista = lista[:5]
# print(nowa_lista)
 
# nowa_lista.remove(nowa_lista[len(nowa_lista)//2])
# print(nowa_lista)
 
# nowa_lista.sort()
# print(nowa_lista)
 
# element = 8
 
# if element in lista:
#     print(f'W pierwszej liście występuje element {element}')
# else:
#     print(f"nie istnieje")

# # if element in nowa_lista:
# #     print(f'W nowej liście występuje element {element}')
# # else:
# #     print(f"Nie istnieje")
# # del lista
# # del nowa_lista

# # # zadanie 2.5
# # liczba1 = float(input("Wpisz liczbę: "))
# # liczba2 = float(input("Wpisz liczbę: "))
# # operacja = input("Podaj operację (+, -, *, /): ")

# # if operacja == "+":
# #     wynik = liczba1 + liczba2
# #     print(f"Wynik dodawania: {liczba1} + {liczba2} = {wynik}")

# # elif operacja == "-":
# #     wynik = liczba1 - liczba2
# #     print(f"Wynik odejmowania: {liczba1} - {liczba2} = {wynik}")

# # elif operacja == "*":
# #     wynik = liczba1 * liczba2
# #     print(f"Wynik mnożenia: {liczba1} * {liczba2} = {wynik}")

# # elif operacja == "/":
# #     wynik = liczba1 / liczba2
# #     print(f'Wynik dzielenia: {liczba1} / {liczba2} = {wynik}')

# # else:
# #     wynik = "nieznany operator"

# # działanie = f"{liczba1} {operacja} {liczba2}"

# # print(f"działanie: {działanie}")
# # print(f"wynik: {wynik}")

# # zadanie 2.6
# wejście = input("Podaj działanie (np. 2 + 4): ")
# skladniki = wejście.split()  # Dzieli tekst na listę elementów
# liczba1 = float(skladniki[0])  # Pierwsza liczba
# operacja = skladniki[1]  # Operator (+, -, *, /)
# liczba2 = float(skladniki[2])  # Druga liczba

# if operacja == "+":
#     wynik = liczba1 + liczba2
#     print(f"Wynik dodawania: {liczba1} + {liczba2} = {wynik}")

# elif operacja == "-":
#     wynik = liczba1 - liczba2
#     print(f"Wynik odejmowania: {liczba1} - {liczba2} = {wynik}")

# elif operacja == "*":
#     wynik = liczba1 * liczba2
#     print(f"Wynik mnożenia: {liczba1} * {liczba2} = {wynik}")

# elif operacja == "/":
#     wynik = liczba1 / liczba2
#     print(f'Wynik dzielenia: {liczba1} / {liczba2} = {wynik}')

# else:
#     wynik = "nieznany operator"

# działanie = f"{liczba1} {operacja} {liczba2}"

# print(f"działanie: {działanie}")
# print(f"wynik: {wynik}")

# ######lub 
# z= input("Podaj pełne działanie: ")

# lis=z.split()
 
# x=float(lis[0])

# y=float(lis[2])

# k=lis[1]
 
 
# dzialania = {

#     "+": x + y,

#     "*": x*y,

#     "-": x - y,

#     "/": x/y,

# }
 
# wynik = [value for key, value in dzialania.items() if k in key][0]

# print(f"Działanie {z}")

# print(f"Wynik {wynik}")
 

#zadanie 2.7
# lista = [-4, -3, -2, -1, 0, 3, 6, 9, 12]
# print([value for value in lista if value > 0])

# zadanie 2.8
# wynik = [(i, 1, i, i**2, i**3) for i in range(11)]
# print(wynik)

# zadanie 2.9
# lista = [22, 19, 24, 25, 26, 24, 25, 24]
# zbior = set(lista)
# print(len(lista),len(zbior))
# print(lista if len(lista) > len(zbior) else zbior)

# zadanie 2.10
# x = int(input('Podaj liczbę: '))

# for y in range(1, 11):
#   print(f'{x} * {y} = {x * y}')

# # zadanie 2.11
# suma_parzyste = sum(i for i in range(101) if i % 2 == 0)
# suma_nieparzyste = sum(i for i in range(101) if i % 2 == 1)

# print(f'Suma liczb parzystych: {suma_parzyste}')
# print(f'Suma liczb nieparzystych: {suma_nieparzyste}')

# # zadanie 2.12
# tekst = """Uczę się Pythona, aby móc tworzyć aplikacje. Dużą zaletą Pythona jest to że jest bardzo 
# zbliżony do języka angielskiego. Posiada prostą składnię, ale czasami potrafi być skomplikowany 
# przez wysoki poziom abstrakcji. Jednak dobrze jest się nauczyć Pythona, aby dalej rozwijać się 
# w stronę programowania."""

# zdania = tekst.split('. ')

# for zdanie in zdania:
#     print(zdanie)
#     slowa = zdanie.split(' ')
#     print(f'Liczba unikalnych słów: {len(set(slowa))}')
#     print(f'Liczba słów: {len(slowa)}')

# # zadanie 2.13
# X = [
#     [12,9,3],
#     [4,5,6],
#     [7,8,3]
# ]
# Y = [
#     [9,8,1],
#     [6,7,3],
#     [4,5,9]
# ]

# result = []
# for i in range(len(X)):
#     row = []
#     for j in range(len(X[i])):
#         row.append(X[i][j] + Y[i][j])
#     result.append(row)

# assert result == [[21, 17, 4], [10, 12, 9], [11, 13, 12]]

# zadanie 2.14
X = [[12,9],
[7 ,3],
[5 ,6]]

result = [[0, 0, 0],
[0, 0, 0]]

for i in range(len(result)):
    for j in range(len(result[i])):
        ####print(i,j)
        result[i][j] = X[j][i]

assert result == [[12, 7, 5], [9, 3, 6]]