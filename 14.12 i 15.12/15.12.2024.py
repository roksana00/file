# with open ('nowy plik.txt', 'w') as f:
#     f.write('ala ma kota\n')
    
# with open('nowy plik.txt', 'r') as f:
#     line = f.readline()
#     print('readline:', line)

# with open ('nowy plik.txt', 'r') as f:
#     s = f.read()
#     print('read:', s)

# #dopisanie na koniec pliku

# with open('nowy plik.txt', 'a') as f:
#     f.write('a jan ma psa\n')
    
# with open('nowy plik.txt', 'r') as f:
#     lines = f.readline()
#     print('readlines:', lines)

# with open('nowy plik.txt', 'r') as f:
#     s = f.read()
#     print('read:', s)

# zad. 3.1.1
# import random
# from collections import Counter

# random_range = [random.randrange(11) for i in range(50)]

# counter = Counter(random_range)

# most_common_numbers = counter.most_common(5)

# print("Lista 50 losowych liczb:", random_range)
# print("5 najczęściej spotykanych liczb:", most_common_numbers)

# # Inny sposób:

# import random
# from collections import Counter

# s = (random.randint(0, 10) for i in range(50))

# c = Counter(s)
# print(c)
# print(c.most_common(5))

# zad 3.1.2

# import itertools

# user_input = input("Podaj napis: ")
# permutations = list(itertools.permutations(user_input, 2))
# combinations = list(itertools.combinations(user_input, 2))
# print("Permutacje:", ["".join(p) for p in permutations])
# print("Kombinacje:", ["".join(c) for c in combinations])

# inny sposób:

# import itertools

# napis = input('Podaj napis: ')

# print('Permutacje:')

# for x, y in itertools.permutations(napis, 2):

# print(f'{x}{y}')

# print('Kombinacje:')

# for x, y in itertools.combinations(napis, 2):

# print(f'{x}{y}')


# zad 3.1.3 (nie wiem jest jakiś błąd, trzeba wrócić)

# def mul(a, b):
#     isinstance(b[0], list)
#     raise ValueError ("argument b ma być wektorem, a nie macierzą.")

#     c = [0] * len(a[0])
#     for i in range(len(a)):
#         for j in range(len(a[i])):
#             c[i] += a[i][j] * b[j]
#     return c 

# a = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# b = [ 6, 4, 2]

# print(mul(a, b))

# zad 3.1.4

with open('C:\Users\leuto\Downloads\pliki\wsb_pliki\points.txt', 'r') as f:
    lines = f.read().splitlines()

points = (line.split() for line in lines)
points = [(float(x), float (y)) for x, y in points]
print(lines)
