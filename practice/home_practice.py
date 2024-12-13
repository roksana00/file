# list_a = list(range(0, 10, 2))
# list_b = ['a', 'b', 'c']
# for a, b in zip(list_a, list_b):
#     print(f'{a} - {b}')

# my_list = [0, 1, 2, 3, 4, 5]
# for i in range(len(my_list)):
#     print(my_list [i])


# lista = [1, 2, 8, 5, 0, 3, 4, 5, 6, 7, 7, 8]
# element = lista.pop()
# print(element)

# element = lista.pop(4)
# print(element)
# print(lista)

# index = lista.index(5)
# print(index)

# lista.reverse()
# print(lista)

# slownik = {'słowo1': 'ananas', 
#            'słowo2': 'lekarz'}
# print(slownik['słowo1'])

# # print(slownik.keys())
# # print(slownik.values())
# # print(slownik.items())
# # print(slownik.get ('słowo1'))
# # print(slownik.get ('klucz1'))
# # print(slownik.pop ('słowo1'))
# # print(slownik.popitem ())
# slownik.update ({'słowo3': 'pilot'})
# print(slownik)
# slownik.clear()
# print(slownik)

# zbior = {2, 5, 6, 8, 10}

# # zbior.add(9)
# # print(zbior)

# # zbior.remove(6)
# # print(zbior)

# # zbior.discard(0)
# # print(zbior)

# element = zbior.pop()
# print(element)
# print(zbior)

# zbior.clear()
# print(zbior)


# zbior1 = {1, 2, 3, 4, 5}
# zbior2 = {5, 3, 8, 10, 11}

# wynik_union = zbior1.union(zbior2)
# print(wynik_union)

# wynik_in = zbior1.intersection(zbior2)
# print(wynik_in)

# wynik_diff = zbior1.difference(zbior2)
# print(wynik_diff)

# wynik_diff = zbior2.difference(zbior1)
# print(wynik_diff)

# symdiff = zbior1.symmetric_difference(zbior2)
# print(symdiff)



# text = ['Python', 'jest', 'nice']
# sentence = ', '.join(text)
# print(sentence)

# text = 'papa dobranoc'
# print(text.upper())
# print(text.lower())

# def dodaj(a, b):
#     return a + b
# print(dodaj(2, 3))

# def powitanie():
#     print("witaj, świecie")
# powitanie()

# lambda arguments: expression
# add = lambda x, y: x + y
# result = add(10, 9)
# print(result)

# data = [
#     {'name': 'alice', 'age': 30},
#     {'name': 'aggy', 'age': 1},
#     {'name': 'bob', 'age': 6}
# ]

# oldest = max(data,key=lambda x: x['age'])
# print(oldest['name'])


# youngest = min(data, key = lambda x: x['age'])
# print(youngest['name'])

# data = [
#     ('toyota', 'golf', 2006, 15000),
#     ('honda', 'civic', 2004, 10000),
#     ('a', 'y', 2001, 2039483)
# ]

# # most_expensive = max(data, key = lambda x: x[3])
# # print(most_expensive)

# sort_price = sorted(data, key = lambda x: x[3])
# print(sort_price)

# try:
#     result = 10 / 0
# except ZeroDivisionError as e:
#     print('Wyjątek:', e)

# try:
#     result = 10 / 2
# except ZeroDivisionError as e:
#     print('wyjątek:', e)
# else:
#     print("wynik:", result)

# def calculate_age(age):
#     if age < 0:
#         raise ValueError ("wiek nie może być ujemny")
    
#     return age
# try:
#     result = calculate_age(-5)
# except ValueError as e:
#     print("wyjątek:", e)

# name = 'alice'
# age = 30

# print('name:', name, 'age:', age)

# Pole = 25.12
# print(f' Pole wynosi: {Pole: .3f}')

# print('a', 'b', 'c', sep=', ')
# print("hello", end=' ')
# print('world')

# a = 45.01

# change = bool(a)
# print(change)

# i = 1
# while i <= 5:
#     print(i)
#     i += 1

# lista = [10, 20, 30, 40, 50]
# zakres = lista[1:4]
# print(zakres)

# my_list = ['jabłko', 'banan', 'kiwi']
# for index, value in enumerate(my_list):
#     print(f'{index}, {value}')

# list_a = (range(0, 10, 2))
# list_b = ['a', 'b', 'c', 'd']
# for a, b in zip(list_a, list_b):
#     print(f'{a} - {b}')

# lista = [1, 2, 3, 4, 5]
# element = lista.pop(3)
# print(element)

# ----

my_list = []
my_list.append("python")
my_list.append("is ok")
my_list.append("sometimes")

my_list.remove("sometimes")

my_list[1] = "is neat"

assert my_list == ["python", "is neat"]



