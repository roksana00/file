# WSB_Numpy_Matplotlib.pdf

# 1. Stwórz wektor (np.array) składający się z pięciu dowolnych wartości liczbowych. Wyświetl utworzony wektor.
# Następnie, zmień liczbę na drugiej pozycji (nie pod indeksem 2, tylko na drugiej pozycji) na -1, a liczbę
# znajdującą się na pozycji czwartej powiększ dwa razy.

# import numpy as np

# # a = np.array([1, 2, 3, 4, 5])
# # print('Oryginalna lisat:', a)

# # a[1]= -1
# # a[3] *= 2

# # print('Zmodyfikowana lista:', a)

# # 2. Stwórz macierz dwuwymiarową o wymiarach 3 na 4 (3 wiersze, 4 kolumny) składającą się z losowych wartości za pomocą polecenia np.random.randint. Przedział wartości może być dowolny. Następnie, wyświetl
# # wygenerowaną macierz. 

# b = np.random.randint(0, 100, size=(3, 4))

# print(b)

#         # a) Wyświetl drugi wiersz macierzy (tutaj i dalej to są pozycje, nie indeksy. Chyba że jest powiedziane pod
# # indeksem);

# print(b[1])
# # lub 
# print(b[1, :])

#         b) Wyświetl drugą kolumnę macierzy;

# print(b[:, 1])

#         c)Pomnóż cały pierwszy wiersz razy dwa:

# b[0]*=2
# lub
# b[0, :]*=2

# print(b)

#         d) Wyświetl kwadratową macierz 2x2 składającą się z wycinku macierzy zawierającego pierwsze 2 elementy
# pierwszego i drugiego wiersza.

# c = b[:2, :2]
# print(c)
#                 :2 w pierwszym indeksie oznacza, że wybieramy pierwsze dwa wiersze (pozycje 1 i 2).
#                 :2 w drugim indeksie oznacza, że wybieramy pierwsze dwie kolumny (pozycje 1 i 2).

# 3.  Napisz funkcję simple_plot(a, b), która wyświetli wykres, dwóch podanych wektorów a oraz b. Wektor a będzie
# określony przerywaną linią czerwoną, natomiast wektor b będzie określony ciągłą linią niebieską. Legenda do
# wykresu pojawi się w prawym górnym rogu. Oś x powinna być podpisana x, oś y powinna być podpisana y.
# Dodatkowo należy dodać podpis wykresu oraz siatkę. Siatka powinna być zdefiniowana zieloną linią przerywaną
# z przezroczystością 0.5 i grubością linii 1.15.


import matplotlib.pyplot as plt

# def simple_plot(a, b):
#     plt.plot(a, 'r--', label='Wektor a') # tak, albo jak niżej
#     plt.plot(b, linestyle='-', color='blue', label='Wektor b')

#     plt.title("Wykres dwóch wektorów")
#     plt.xlabel("X")
#     plt.ylabel("Y")

#     plt.legend(loc='upper right')

#     plt.grid(
#         linestyle='--', color='green', alpha=0.5, linewidth=1.15
#     )

#     plt.show()

# a = np.array([1, 3, 5, 7, 9])
# b = np.array([2, 4, 6, 8, 10])

# simple_plot(a, b)

# 4. Napisz funkcje func_plot(vmin, vmax, step), która wykona wykres funkcji f(x) = x
# 2 − x ∗ 4 + 8. Argument
# vmin oznacza wartość początkową wektora x, vmax oznacza wartość końcową wektora x, step oznacza krok
# w wektorze x.

import numpy as np
import matplotlib.pyplot as plt


# def func_plot(vmin, vmax, step):
#     x = np.arange(vmin, vmax + step, step)
    
#     y = x**2 - 4*x + 8
    
#     plt.plot(x, y, label='f(x) = x^2 - 4x + 8')
#     plt.title("Wykres funkcji f(x)")
#     plt.xlabel("x")
#     plt.ylabel("f(x)")
#     plt.legend()
#     plt.grid(True)
#     plt.show()

# func_plot(-10, 10, 0.1)

# 5. Napisz funkcję multi_plot(sizes, labels), która w jednym oknie wyświetli dwa wykresy: wykres kołowy dla
# podanych rozmiarów w wektorze sizes oraz podpisów labels, oraz wykres słupkowy dla podanych rozmiarów
# w wektorze sizes oraz podpisów labels. Jako przykładowe dane można wziąć na przykład liczbę mieszkańców
# 4-5 polskich miast oraz nazwy tych miast.

# import matplotlib.pyplot as plt
# import numpy as np

# sizes = [1790658, 1280395, 794166, 722434, 485110]
# labels = ["Warszawa", "Kraków", "Łódź", "Wrocław", "Poznań"]

# def multi_plot(sizes, labels):
#     if len(sizes) != len(labels):
#         raise ValueError("Liczba elementów w 'sizes' i 'labels' musi być taka sama.")
    

# fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# axes[0].pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
# axes[0].set_title("Wykres Kołowy")

# axes[1].bar(labels, sizes)
# axes[1].set_title("Wykres Słupkowy")
# axes[1].set_xlabel("Miasta")
# axes[1].set_ylabel("Liczba mieszkańców")

# plt.tight_layout()
# plt.show()

# multi_plot(sizes, labels)

# # 6. . Napisz funkcję scatter_plot(), która wyświetli wykres punktowy dwóch zestawów danych (po 100 punktów każdy): współrzędne x i y punktów w pierwszym zestawie ma być wygenerowane za pomocą funkcji
# np.random.rand(), a współrzędne drugiego zestawu danych mają być wygenerowane za pomocą funkcji
# np.random.randn(). Pierwszy zestaw punktów ma być wizualizowany w kolorze niebieskim, a drugi w kolorze zielonym. Punkty drugiego zestawu danych muszą być w postaci gwiazdek (marker). Na wykresie ma
# być pokazana legenda i siatka.


# def scatter_plot():
#     x1 = np.random.rand(100)
#     y1 = np.random.rand(100)
#     x2 = np.random.randn(100)
#     y2 = np.random.randn(100)

#     plt.scatter(x1, y1, color='blue', label='Dataset 1')
#     plt.scatter(x2, y2, color='green', marker='*', label='Dataset 2')

#     plt.xlabel('x')
#     plt.ylabel('y')
#     plt.title('Wykres punktowy dwóch zestawów danych')
#     plt.legend()
#     plt.grid(True)
#     plt.show()

# scatter_plot()

# 7. . Napisz funkcję make_3D(x, y), która wyświetli wykres powierzchni 3D funkcji funkcji f(x, y) = p
# x2 + y2. Oś x powinna być podpisana x, oś y powinna być podpisana y, oś z powinna być podpisana jako z.

# from mpl_toolkits.mplot3d import Axes3D


# def make_3D(x, y):
#     X, Y = np.meshgrid(x, y)
#     Z = np.sqrt(X ** 2 + Y ** 2)

#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')
#     ax.plot_surface(X, Y, Z, cmap='viridis')

#     ax.set_xlabel('x')
#     ax.set_ylabel('y')
#     ax.set_zlabel('z')

#     plt.show()


# # Przykladowe dane
# x = np.linspace(-5, 5, 100)
# y = np.linspace(-5, 5, 100)

# make_3D(x, y)

# //////// # WSB_Pandas.pdf

# 1. Napisz program, który wczyta zbiór danych. Indeks musi być dopasowany względem pierwszej kolumny z
# pliku. Wyświetl 5 pierwszych i ostatnich rekordów z ramki danych.

import pandas as pd
import matplotlib.pyplot as plt

# df = pd.read_csv('C:/users/leuto/data/file/zajęcia_11_01/pokemon_data.csv', index_col=0)
# print(df.head())
# print(df.tail()) # lub df.head(-5)

# 2. Na podstawie dostarczonej ramki danych stwórz dwie nowe ramki danych. Pierwsza ramka danych będzie
# zawierała rekordy, w których kolumna Type 2 ma wartość brakującą. Druga ramka danych nie będzie zawierała
# żadnych wartości brakujących. Następnie wyświetl liczbę rekordów w każdej z tych nowych ramek danych.
# Użyteczne wyrażenia: isnull(), dropna().

# df_type2_missing = df[df['Type 2'].isnull()]
# df_no_missing = df.dropna()
# print(f'Liczba rekordów z brakującą wartością w kolumnie "Type 2": {len(df_type2_missing)}')
# print(f'Liczba rekordów bez brakujących wartości: {len(df_no_missing)}')

# 3. Na podstawie dostarczonej ramki danych posortuj dane według malejących wartości kolumn związanych ze
# statystkami defensywnymi (tj. HP, Defense, Sp. Def) i według rosnących wartości kolumn ze statystykami
# ofensywnymi (tj. Attack, Sp. Atk, Speed). Stwórz kolumny o nazwach Total def. oraz Total off., które
# będą posiadać sumaryczną wartość kolejno kolumn defensywnych i ofensywnych. Utwórz kolumny Rank def.
# oraz Rank off. posiadające ranking wartości z powstałych kolumn według wartości najwyższych. Wyświetl
# Top 5 rekordów według Rank def. oraz Rank off.
# Użyteczne wyrażenia: sort_values(), rank().

# df_sorted = df.sort_values(by=['HP', 'Defense', 'Sp. Def'], ascending=False)
# df_sorted = df_sorted.sort_values(by=['HP', 'Defense', 'Sp. Def'], ascending=True)

# df_sorted['Total def.'] = df_sorted['HP'] + df_sorted['Defense'] + df_sorted['Sp. Def']
# df_sorted['Total off.'] = df_sorted['Attack'] + df_sorted['Sp. Atk'] + df_sorted['Speed']

# df_sorted['Rank def.'] = df_sorted['Total def.'].rank(ascending=False)
# df_sorted['Rank off.'] = df_sorted['Total off.'].rank(ascending=False)

# top_def = df_sorted.sort_values(by='Rank def.').head(5)
# top_off = df_sorted.sort_values(by='Rank off.').head(5)
# print(top_def[['Name', 'Rank def.', 'Total def.']])
# print(top_off[['Name', 'Rank off.', 'Total off.']])

# 4. Na podstawie dostarczonej ramki danych, utwórz filtr, który wybierze rekordy zawierające w kolumnie Name
# ciągi znaków Mega oraz os. Następnie wyświetl liczbę rekordów spełniających ten warunek. Dla każdego z
# tych rekordów stwórz wykres słupkowy przedstawiający statystyki ofensywne i defensywne. Wykres ma być
# stworzony na jednym obiekcie Figure, a słupki nie powinny nachodzić na siebie.
# Użyteczne wyrażenia: contains(), bar().

# fig, ax = plt.subplots(figsize=(10, 6))

# filtered_df = df[df['Name'].str.contains('Mega') & df['Name'].str.contains('os')]
# # Liczba rekordów
# num_records = len(filtered_df)

# # Szerokość słupka
# bar_width = 0.1

# # Tworzenie wykresów dla każdego rekordu
# for i, (_, row) in enumerate(filtered_df.iterrows()):
#     stats = row[['Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']]
#     x = [j + bar_width * i for j in range(len(stats))]
#     ax.bar(x, stats, bar_width, label=row['Name'])

# # Konfiguracja wykresu
# ax.set_title('Statystyki ofensywne i defensywne')
# ax.set_xlabel('Statystyki')
# ax.set_ylabel('Wartość')
# ax.set_xticks([r + bar_width * (num_records - 1) / 2 for r in range(len(stats))])
# ax.set_xticklabels(['Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed'])
# ax.legend()
# plt.show()

# df['Name'].str.contains('Mega')

# 5. Na podstawie dostarczonej ramki danych, utwórz ramkę danych, która będzie zawierała dodatkową kolumnę
# o nazwie Total, zawierającą sumaryczne wartości statystyk. Następnie utwórz kolumnę Pseudo Legendary,
# która będzie przyjmować wartość True, jeśli wartość w kolumnie Total będzie większa niż 500, a w przeciwnym razie będzie przyjmować wartość False. Następnie wykonaj zapytanie grupujące ramkę danych według
# kolumny Generation. Na koniec stwórz wykres ilościowy grup według generacji dla kolumn Legendary oraz
# Pseudo Legendary.
# Użyteczne wyrażenia: groupby().

# df_new = df.copy()
# df_new['Total'] = df[['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']].sum(axis=1)
# df_new['Pseudo Legendary'] = df_new['Total'] > 500
# grouped = df_new.groupby('Generation').agg({'Legendary': 'sum', 'Pseudo Legendary': 'sum'}).reset_index()

# grouped.plot(kind='bar', x='Generation', stacked=True)
# plt.title('Legendary i Pseudo Legendary według generacji')
# plt.ylabel('Liczba')
# plt.show()

# 6. Na podstawie dostarczonej ramki danych, utwórz ramkę danych, która będzie zawierała jedynie wartości
# statystyk dla rekordów. Następnie zapisz powstałą ramkę do pliku z rozszerzeniem csv o nazwie modified.csv.
# Utwórz wykresy zależności między statystkami.
# Użyteczne wyrażenia: to_csv().

# df_stats = df[['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']]
# df_stats.to_csv('modified.csv', index=False)
# pd.plotting.scatter_matrix(df_stats, figsize=(12, 12))
# plt.show()

# 7. Dodaj do istniejącej ramki danych rekordy pochodzące z pliku gen7.csv. Przed połączeniem danych z ramki
# gen7.csv usuń nadmiarowe kolumny. Po połączeniu zapisz dane do pliku o nazwie pokemon_extended.csv.
# Nazwy kolumn zachowaj z ramki podstawowej.
# Użyteczne wyrażenia: drop(), concat(), rename()

# df_gen7 = pd.read_csv('gen7.csv')
# df_gen7 = df_gen7.rename(columns={
#     'name': 'Name', 
#     'type1': 'Type 1', 
#     'type2': 'Type 2', 
#     'sp_attack': 'Sp. Atk', 
#     'sp_defense': 'Sp. Def', 
#     'generation': 'Generation', 
#     'is_legendary': 'Legendary',
#     'hp': 'HP',
#     'attack': 'Attack',
#     'defense': 'Defense',
#     'speed': 'Speed'
# })
# df_gen7 = df_gen7[df.columns]  # Dopasowanie kolumn do oryginalnego pliku
# df_extended = pd.concat([df, df_gen7])
# df_extended.to_csv('pokemon_extended.csv', index=False)

# 8. Dla rozszerzonego zbioru danych (plik pokemon_extended.csv) stwórz wykres kołowy przedstawiający rozkłady typów Pokemonów (Type 1) w poszczególnych generacjach.
# Użyteczne wyrażenia: loc, plot(), groupby().

# pokemon_extended_df = pd.read_csv('pokemon_extended.csv')

# # Grupowanie danych według kolumny Generation i Type 1, a następnie zliczenie ilości wystąpień każdego typu w każdej generacji
# grouped = pokemon_extended_df.groupby(['Generation', 'Type 1']).size().unstack()

# # Utworzenie wykresów kołowych dla rozkładu Type 1 w poszczególnych generacjach
# fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(15, 15))
# for i, (gen, ax) in enumerate(zip(grouped.index, axes.flatten()), 1):
#     grouped.loc[gen].plot(kind='pie', ax=ax, autopct='%1.1f%%', startangle=90)
#     ax.set_title(f'Generation {i}')
#     if i == 8 or i == 9:
#         for spine in ['top', 'right', 'left', 'bottom']:
#            ax.spines[spine].set_visible(False)
# plt.tight_layout()
# plt.show()

# 9. Utwórz ogólny raport statystyczny dla rozszerzonego zbioru danych. Następnie przedstaw te statystyki na
# wykresie pudełkowym, który pozwoli zobaczyć rozkład wartości poszczególnych cech.
# Użyteczne wyrażenia: describe(), boxplot().

# stat_report = df_extended.describe()
# print(stat_report)

# df_extended[['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']].plot(kind='box', figsize=(12, 8))
# plt.title('Rozkład statystyk Pokemonów')
# plt.show()