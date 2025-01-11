# WSB_Numpy_Matplotlib.pdf

# 1. Stwórz wektor (np.array) składający się z pięciu dowolnych wartości liczbowych. Wyświetl utworzony wektor.
# Następnie, zmień liczbę na drugiej pozycji (nie pod indeksem 2, tylko na drugiej pozycji) na -1, a liczbę
# znajdującą się na pozycji czwartej powiększ dwa razy.

# import numpy as np

# a = np.array([1, 2, 3, 4, 5])
# print(a)

# a[1]= -1
# a[3] *= 2

# print('Zmodyfikowana lista:', a)

# 2. Stwórz macierz dwuwymiarową o wymiarach 3 na 4 (3 wiersze, 4 kolumny) składającą się z losowych wartości za pomocą polecenia np.random.randint. Przedział wartości może być dowolny. Następnie, wyświetl
# wygenerowaną macierz. 

# b = np.random.randint(0, 100, size=(3, 4))

# print(b)

        # a) Wyświetl drugi wiersz macierzy (tutaj i dalej to są pozycje, nie indeksy. Chyba że jest powiedziane pod
# indeksem);

# print(b[1])

        # b) Wyświetl drugą kolumnę macierzy;

# print(b[:, 1])

        # c)Pomnóż cały pierwszy wiersz razy dwa:

# b[0]*=2
# print(b)

        # d) Wyświetl kwadratową macierz 2x2 składającą się z wycinku macierzy zawierającego pierwsze 2 elementy
# pierwszego i drugiego wiersza.

# c = b[:2, :2]
# print(c)
                # :2 w pierwszym indeksie oznacza, że wybieramy pierwsze dwa wiersze (pozycje 1 i 2).
                # :2 w drugim indeksie oznacza, że wybieramy pierwsze dwie kolumny (pozycje 1 i 2).

# 3.  Napisz funkcję simple_plot(a, b), która wyświetli wykres, dwóch podanych wektorów a oraz b. Wektor a będzie
# określony przerywaną linią czerwoną, natomiast wektor b będzie określony ciągłą linią niebieską. Legenda do
# wykresu pojawi się w prawym górnym rogu. Oś x powinna być podpisana x, oś y powinna być podpisana y.
# Dodatkowo należy dodać podpis wykresu oraz siatkę. Siatka powinna być zdefiniowana zieloną linią przerywaną
# z przezroczystością 0.5 i grubością linii 1.15.


# import matplotlib.pyplot as plt

# def simple_plot(a, b):
#     plt.plot(a, linestyle='--', color='red', label='Wektor a')
#     plt.plot(b, linestyle='-', color='blue', label='Wektor b')

#     plt.title("Wykres dwóch wektorów")
#     plt.xlabel("X")
#     plt.ylabel("Y")

#     plt.legend(loc='upper right')

#     plt.grid(
#         linestyle='--', color='green', alpha=0.5, linewidth=1.15
#     )

#     plt.show()

# 4. Napisz funkcje func_plot(vmin, vmax, step), która wykona wykres funkcji f(x) = x
# 2 − x ∗ 4 + 8. Argument
# vmin oznacza wartość początkową wektora x, vmax oznacza wartość końcową wektora x, step oznacza krok
# w wektorze x.

# import numpy as np
# import matplotlib.pyplot as plt


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

6. 

# 7. . Napisz funkcję make_3D(x, y), która wyświetli wykres powierzchni 3D funkcji funkcji f(x, y) = p
# x2 + y2. Oś x powinna być podpisana x, oś y powinna być podpisana y, oś z powinna być podpisana jako z.

import math
import matplotlib.pyplot as plt
import numpy as np

f(x, y) == math.sqrt(x ** 2 + y ** 2)
