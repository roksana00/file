# def f(liczba1=3, liczba2=2, operator="+", *args, **kwargs):

# 
# wynik = "Nieznany operator"
#     if operator == '+':
# wynik = liczba1 + liczba2
#     elif operator == '-':
# wynik = liczba1 - liczba2
#     elif operator == '*':
# wynik = liczba1 * liczba2
#     elif operator == '/':
# wynik = liczba1 / liczba2

#     return wynik, args, kwargs

# print(f(1))
# print(f(99, 2, '-'))
# print(f(9.102, 4.2312, '*'))
# print(f('99', '2'))
# print(f())
# print(f(operator='*'))
# print(f(operator='/', liczba1=5, liczba2=10))
# print(f(10, operator='/'))
# print(f(9.102, 4.2312, '*', 0, 1, 2, 3))
# print(f(9.102, 4.2312, '*', 0, 1, 2, 3, liczba3=10))
# print(f(9.102, 4.2312, '*', 0, 1, 2, 3, [1, 2, 3], liczba3=10))
 
# wynik = f()
# print(wynik[0])

# zad 3.1.1

# def f(x):
#     return x**2 + 4*x - 3

# print(f(2))
# print(f(-1))

# zad 3.1.2

# def f(a, b = 2):
#     return a + b

# print(f(1))
# print(f(1, b = 2))
# print(f(1, 2))
# print(f(a = 1))
# print(f(a = 1, b = 2))
# print(f(b = 2, a = 1))

# zad 3.1.3

# def modyfikuj_liste(lista):
#     kopia_listy = lista.copy()

#     nowa_lista = []    
#     # dlugosc = len(kopia_listy)
#     # v1
#     # for i in range(dlugosc):
#     #     if kopia_listy[i] % 3 == 0:
#     #         kopia_listy.pop(i)
#     #         dlugosc -= 1
#     #         i -= 1
#     for i in range(len(kopia_listy)):
#         if kopia_listy[i] % 3 != 0:
#             nowa_lista.append(kopia_listy[i])
           
#     # v2
#     # kopia_listy = [i for i in kopia_listy if i % 3 != 0]
 
#     kopia_listy = nowa_lista
#     lista_wynikowa = []
#     for i in range(len(kopia_listy)):
#         if kopia_listy[i] % 2 == 0:
#             lista_wynikowa.append(-1)
#         lista_wynikowa.append(kopia_listy[i])
#         # else:
#         #     lista_wynikowa.append(kopia_listy[i])
 
#     kopia_listy = lista_wynikowa
 
#     return kopia_listy
 
# moja_lista = [2, 3, 1, 5, 6, 3, 2, 4]
# print(modyfikuj_liste(moja_lista))

# - druga wersja

# def modyfikuj_liste(lista):
#     kopia_listy = lista.copy()
 
#     dlugosc = len(lista)
#     i = 0
#     while i < dlugosc:
#         if kopia_listy[i] % 3 == 0:
#             kopia_listy.pop(i)
#             dlugosc -= 1
#         else:
#             i += 1
 
#     i = 0    
#     while i < dlugosc:
#         if kopia_listy[i] % 2 == 0:
#             kopia_listy.insert(i, -1)
#             dlugosc += 1
#             i += 2
#         else:
#             i += 1
 
#     return kopia_listy


# zad 3.1.4

# import random

# def f(n = 10, a = 0, b = 10):
#     random_list = [random.randrange(a, b) for i in range(n)]
#     return random_list

# print(f())

# zad 3.1.5

# import random

# def losuj(n = 10, a = 0, b = 10):
#     return [random.randrange(a, b) for i in range(n)]

# def f(n):
#     lista = losuj(n)
#     print(lista)
#     print(max(lista))
#     print(lista.index(min(lista)))
#     print(sum(lista))
#     print(lista.count(5))
#     print(set(lista))
    
# f(10)

# zad. 3.1.6
# a = [1, 2, 3]
# b = ['x', 'y']

# def iloczyn_kartezjanski(a, b):
#     result = []
#     for item1 in a:
#         for item2 in b:
#             result.append((item1, item2))
#     return result

# result = iloczyn_kartezjanski(a, b)
# print(result)

# lub :

# def iloczyn_kartezjanski(a, b):
#     return [(i,j) for i in a for j in b]
 
# lista1 = [1, 2, 3]
# lista2 = ['a', 'b']
# print(iloczyn_kartezjanski(lista1, lista2))


# zad. 3.1.7

# a = [x ** 2 for x in range(11)]
# b = [x ** 2 for x in range(21) if x ** 2 % 2 != 0]
# c = [x ** 2 if x % 2 == 0 else x ** 3 for x in range(11)]
 
# print(a)
# print(b)
# print(c)

# zad 3.1.8

# import random

# def suma(n = 20, a = -100, b = 100):
#     return sum(num for num in [random.randrange(a, b) for i in range(n)] if num > 0)

# print("Suma:", suma())

# # lub:

# lista = [random.randrange(-100, 100) for i in range(20)]
 
# print(sum([x for x in lista if x > 0]))

# zad. 3.1.9
# import random

# def f(a):
#     if isinstance(a, (int, float)):
#         return a * 2
#     elif isinstance(a, list):
#         return [x * 2 for x in a]
# print(funkcja(5))
    # lub:
# def funkcja(a):
#     return a*2 if isinstance(a,int) or isinstance(a,float) else [i * 2 for i in a]

# print(funkcja(5))

# zad. 3.1.10

# s = "Ala ma kota"

# def f(s):
#     return[ord(x) for x in s]

# print(f(s))

# zad. 3.1.11

# napis1 = "ala ma kota"
# napis2 = "apple"
    
# def f(napis1, napis2):
#     zbior1 = set(napis1)
#     zbior2 = set(napis2)
#     return print(f'{zbior1.union(zbior2)}\n{zbior1.intersection(zbior2)}\n{zbior1.difference(zbior2)}')
    
# f(napis1, napis2)


# zad. 3.1.12

# def przetlumacz(napis):

#         slownik = {
#         'banana': 'banan',
#         'cherry': 'wiśnia',
#         'apple': 'jabłko',
#         'pear': 'grusza',
#         'watermelon': 'arbuz'}
    
#         lista_slow = napis.split(' ')
#         return ' '.join([slownik[slowo] if slowo in slownik.keys() else f'[{slowo}]' for slowo in lista_slow])

# napis = 'apple banana lemon orange pear'
# print(przetlumacz(napis))

# zad. 3.2.1

# def f(x):
#     return x ** 3 - 3 * (x ** 2) + 8 * x - 2

# print(f(2))
# print(f(-1))

# zad. 3.2.2

# def f(a, b = 0):
#     return -b / a if a else 'Brak rozwiązań' if b else 'Nieskończenie wiele rozwiazań'

# print(f(1, 2))
# print(f(1, b = 2))
# print(f(a = 1, b = 2))
# print(f(b = 2, a = 1))

# zad. 3.2.3

# def modyfikuj_liste(lista):
#     kopia_listy = lista.copy()
 
#     dlugosc = len(lista)
#     i = 0
#     while i < dlugosc:
#         if kopia_listy[i] % 4 == 0:
#             kopia_listy.pop(i)
#             dlugosc -= 1
#         else:
#             i += 1
 
#     i = 0    
#     while i < dlugosc:
#         if kopia_listy[i] % 2 != 0:
#             kopia_listy.insert(i, -1)
#             dlugosc += 1
#             i += 2
#         else:
#             i += 1
 
#     return kopia_listy

# moja_lista = [2, 3, 1, 5, 8, 3, 2, 4]
# print(modyfikuj_liste(moja_lista))

# zad 3.2.4 (to samo co poprzednie)

# import random

# def f(n = 10, a = 0, b = 10):
#     random_list = [random.randrange(a, b) for i in range(n)]
#     return random_list

# print(f())

# zad 3.2.5

# import random

# def losuj(n = 10, a = 0, b = 10):
#     return [random.randrange(a, b) for i in range(n)]

# def f(n):
#     lista = losuj(n)
#     print(lista)
#     print(min(lista))
#     print(lista.index(max(lista)))
#     print(sum(lista))
#     print(sorted(lista))
#     print(lista.count(3))
#     print(set(lista))
    
# f(10)


# # zad. 3.2.6.

# napis = "ABCD"

# def lista_kombinacji(napis):
#     kombinacje = []
#     for i in range(len(napis)):
#         for j in range(i + 1, len(napis)):
#             kombinacje.append(napis[i] + napis[j])
#     return kombinacje      

# wynik = lista_kombinacji(napis)
# print(wynik)

# lub z użyciem enumerate: 

# def funkcja(napis):
#     kombinacje = []
#     for idx1, i in enumerate(napis):
#         for idx2, j in enumerate(napis):
#         #    if i != j:
#            if idx1 != idx2:
#             # kombinacja = i+j
#             if j+i not in kombinacje:
#                kombinacje.append(i+j)
 
#     return kombinacje
 
 

#  zad. 3.2.7

# a = [x ** 3 for x in range(11)]
# b = [x ** 3 for x in range(11) if x ** 3 % 3 == 0]
# c = [x ** 3 if x % 3 == 0 else x ** 2 for x in range(11)]

# print(a)
# print(b)
# print(c)

#  zad. 3.2.8

# import random

# lista = [random.randrange(-10, 10) for i in range(20)]

# print(lista)

# print(sum([x ** 2 for x in lista if x < 0]))

# # # lub:
# import random

# def suma_listy(n = 20, t = 0):
#     lista = [random.randrange(-10, 11) for i in range(n)]
#     print(lista)
#     return sum([x ** 2 for x in lista if x < t])

# print(suma_listy())

# zad. 3.2.9

# import random

# def f(a):
#     if isinstance(a, (int, float)):
#         return a ** 2
#     elif isinstance(a, list):
#         return [x ** 2 for x in a]
# print(f([2, 6]))

#     # lub:

# def f(a):
#     return a ** 2 if isinstance(a,int) or isinstance(a,float) else [i ** 2 for i in a]

# print(f(10))

#  zad. 3.2.10

# a = [122, 108, 107, 118, 103, 107, 102, 111, 104, 115]
 
# def zamien(a):
#     return ''.join([chr(x) for x in a])
 
# print(zamien(a))

#  zad. 3.2.11

# lista1 = [1, 2, 1, 3, 4]
# lista2 = [2, 5, 5, 2]
 
# def f(lista1, lista2):
#     zbior1 = set(lista1)
#     zbior2 = set(lista2)
#     print(f'{zbior1.union(zbior2)}\n{zbior1.intersection(zbior2)}\n{zbior1.difference(zbior2)}')
 
# f(lista1, lista2)

#  zad 3.2.12

# slownik = {
#     'banana': 'banan',
#     'cherry': 'wiśnia',
#     'apple': 'jabłko',
#     'pear': 'gruszka',
#     'watermelon': 'arbuz'
#     }
 
# slowo = ' '
# while slowo != '':
#     slowo = input('Podaj słowo: ')
#     if slowo in slownik.keys():
#         print(slownik[slowo])
#     else:
#         if slowo == '':
#             break
#         else:
#             pytanie = input('Słowo jest nieznane. Czy chcesz je dodać? [tak/nie]: ')
#             if pytanie == 'tak':
#                 tlumaczenie = input('Wpisz tłumaczenie tego słowa: ')
#                 slownik.update({slowo: tlumaczenie})
#                 print(f'Słowo {slowo} zostało dodane do słownika.')
#             elif pytanie == 'nie':
#                 print(f'Słowo {slowo} nie zostanie dodane.')
#             else:
#                 break

# funkcje zadania.pdf

# zad. 7

# def grupuj_wedlug_typow(*args):
 
#     slownik = {}
 
#     for i in args:
#         typ = str(type(i)).split("'")[1]
#         if typ not in slownik.keys():
#             slownik[typ] = []
       
#         slownik[typ].append(i)
 
#     return slownik
 
# wynik = grupuj_wedlug_typow(1, 'tekst', [1,2], {"klucz": "wartosc"}, {1, 2, 3}, 3.14)

# print(wynik)
