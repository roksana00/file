# PROJEKTOWANIE OBIEKTOWE
# zestaw atrybutów = podejście obiektowe,
# klasa będzie opisywać obiekt
# tworzenie szablonu z atrybutami 

# pies_1_waga = 10
# pies_1_wzrost = 80
# pies_1_wiek = 5

# pies_2_waga = 17
# pies_2_wzrost = 110
# pies_2_wiek = 2

#  ale jest to counterproductive więc można stworzyć szablon

# class Pies: #lepiej zaczynać od dużej litery
#     # pass #nie zawiera nic
#     def __init__(self): #kontener przechowujący klasy
#         self.waga = None
#         self.wzrost = None
#         self.wiek = None 

# ! __init__ = metoda magiczna

# pies1 = Pies() #tworzenie konkretnego obiektu wg szablonu klasy
# print(pies1.waga)
# print(pies1.wzrost)
# print(pies1.wiek)

# pies2 = Pies()
# print(pies2.waga)
# print(pies2.wzrost)
# print(pies2.wiek)
# ---
# class Pies: 
#     def __init__(self, waga, wzrost, wiek):
#         self.waga = waga
#         self.wzrost = wzrost
#         self.wiek = wiek

# #self - potrzebny zawsze, 

# pies1 = Pies(10, 80, 5) #tworzenie konkretnego obiektu wg szablonu klasy
# print('Pies 1')
# print(pies1.waga)
# print(pies1.wzrost)
# print(pies1.wiek)

# pies2 = Pies(17, 90, 4)
# print('Pies 2')
# print(pies2.waga)
# print(pies2.wzrost)
# print(pies2.wiek)

# ---
# class Pies: 
#     ilosc_łap = 4 #zmienna klasowa, taka sama wartość dla każdego obiektu tej klasy
#     dzwiek = 'hau'
#     def __init__(self, waga, wzrost, wiek='5'): #można tak zrobić, jak wiemy, że ta zmienna nie będzie często się zmieniać, ale będzie nadpisana przez inną 
#         self.waga = waga
#         self.wzrost = wzrost
#         self.wiek = wiek
#         self.ilosc_wizyt = 0 # przypisana sztywna wartość, 

# pies1 = Pies(10, 80, 5) #tworzenie konkretnego obiektu wg szablonu klasy
# print('Pies 1')
# print(pies1.waga)
# print(pies1.wzrost)
# print(pies1.wiek)
# print(pies1.ilosc_łap)
# print(pies1.dzwiek)

# pies2 = Pies(17, 90, 4)
# print('Pies 2')
# print(pies2.waga)
# print(pies2.wzrost)
# print(pies2.wiek)
# print(pies2.ilosc_łap)

# ---
# class Pies: 
#     ilosc_łap = 4 #zmienna klasowa, taka sama wartość dla każdego obiektu tej klasy
#     dzwiek = 'hau'
#     def __init__(self, waga, wzrost, wiek='5'): #można tak zrobić, jak wiemy, że ta zmienna nie będzie często się zmieniać, ale będzie nadpisana przez inną 
#         self.waga = waga
#         self.wzrost = wzrost
#         self.wiek = wiek
#         self.ilosc_wizyt = 0 
    
#     def wypisz_informacje(self):
#         print(f'waga: {self.waga}')
#         print(f'wzrost: {self.wzrost}')
#         print(f'wiek: {self.wiek}')
#         print(f'ilosc_łap: {self.ilosc_łap}')

# pies1 = Pies(10, 80, 5) #tworzenie konkretnego obiektu wg szablonu klasy
# print('Pies 1')
# pies1.wypisz_informacje()
# pies1.waga = 12
# print("po zmianie wagi")
# pies1.wypisz_informacje()

# METODY MAGICZNE: zawsze z __x__
# class Pies: 
#     ilosc_łap = 4 #zmienna klasowa, taka sama wartość dla każdego obiektu tej klasy
#     dzwiek = 'hau'
#     def __init__(self, waga, wzrost, wiek='5'): #można tak zrobić, jak wiemy, że ta zmienna nie będzie często się zmieniać, ale będzie nadpisana przez inną 
#         self.waga = waga
#         self.wzrost = wzrost
#         self.wiek = wiek
#         self.ilosc_wizyt = 0 

    # def __del__(self): #destruktor, który uruchamia się kiedy obiekt jest czyszczony
    #     print('obiekt Pies jest zniszczony')
    
    
#     def wypisz_informacje(self):
#         print(f'waga: {self.waga}')
#         print(f'wzrost: {self.wzrost}')
#         print(f'wiek: {self.wiek}')
#         print(f'ilosc_łap: {self.ilosc_łap}')

#     def __add__(self, drugi_pies): # operacja dodawania obiektów
#         return self.waga + drugi_pies.waga
    
#     def __eq__(self, other): # porównanie obiektów
#         return (self.waga == other.waga) and (self.wzrost == other.wzrost) and (self.wiek == other.wiek)
    
# pies1 = Pies(10, 80, 5) #tworzenie konkretnego obiektu wg szablonu klasy
# print('Pies 1')
# pies1.wypisz_informacje()
# pies1.waga = 12
# print("po zmianie wagi")
# pies1.wypisz_informacje()

# pies2 = Pies(17, 90, 4)
# print('Pies 2')
# print(pies2.waga)
# print(pies2.wzrost)
# print(pies2.wiek)
# print(pies2.ilosc_łap)

# pies3 = Pies(12, 80, 5) #tworzenie obiektu wg szablonu klasy Pies

# print(pies1 + pies2)
# print(pies1 == pies3)

# ZADANIA

# zad. 3.1

# class Samochod: 
#     def __init__(self, marka, model, rok_produkcji, predkosc_max): 
#         self.marka = marka
#         self.model = model
#         self.rok_produkcji = rok_produkcji
#         self.predkosc_max = predkosc_max

#     def jedz(self, predkosc, droga):
#         if predkosc > droga.max_predkosc:
#             przekroczenie = predkosc - droga.max_predkosc
#             print(f'samochód marki {self.marka} {self.model} z {self.rok_produkcji} roku jedzie z prędkością {predkosc} km/h. Przekraczasz maksymalną prędkość o {przekroczenie} km/h na drodze rodzaju {droga.rodzaj}!')
#         else:
#             print(f'Samochód marki {self.marka} {self.model} jedzie z prędkością {predkosc} km/h na drodze {droga.rodzaj}')

#     def __del__(self):
#         print('obiekt Samochod jest zniszczony')
    
# class Droga:
#     def __init__(self, rodzaj, max_predkosc):
#         self.rodzaj = rodzaj
#         self.max_predkosc = max_predkosc

# samochod = Samochod("Ferrari", "250 GTO", 2019, 200)
# droga = Droga("Autostrada", 140)
# samochod.jedz(110, droga)

#  zad 3.2

# class KontoBankowe:
#     def __init__(self, numer_konta, imię_właś, nazwisko_właś, saldo):
#         self.numer_konta = numer_konta
#         self.imię_właś = imię_właś
#         self.nazwisko_właś = nazwisko_właś
#         self.saldo = saldo

#     def __del__(self):
#         print(f'Konto o {self.numer_konta} należące do {self.imię_właś} {self.nazwisko_właś} zostało usunięte')

#     def wpłata(self, kwota):
#         self.saldo += kwota
#         print(f'Wpłata na konto o numerze {self.numer_konta} została wykonana. Aktualne saldo: {self.saldo}')
        
#     def wypłata(self, kwota):
#         if self.saldo >= kwota:
#             self.saldo -= kwota
#             print(f'Wpłata na konto o numerze {self.numer_konta} została wykonana. Aktualne saldo: {self.saldo}')
#         else:
#             print(f"Nie można wypłacić {kwota}. Saldo: {self.saldo} jest za niskie.")

# moje_konto = KontoBankowe("123456789", "Jan", "Kowalski", 1000.0)
# moje_konto.wpłata(500.0)
# moje_konto.wypłata(1500.0)

#  zad 3.3

# class EnergiaOdnawialna:
#     def __init__(self, nazwa, moc, lokacja):
#         self.nazwa = nazwa
#         self.moc = moc
#         self.lokacja = lokacja

#     def get_info(self):
#         print(f"Źródło: {self.nazwa}, Moc: {self.moc} MW, Lokalizacja: {self.lokacja}")

#     def __add__(self, other):
#         nowa_nazwa = f'{self.nazwa}, {other.nazwa}'
#         nowa_moc = self.moc + other.moc
#         nowa_lokacja = self.lokacja + other.lokacja
#         return EnergiaOdnawialna(nowa_nazwa, nowa_moc, nowa_lokacja)
    
#     def __str__(self):
#         return f"Źródło: {self.nazwa}, Moc: {self.moc} MW"

#     def __eq__(self, other):
#         return self.nazwa == other.nazwa and self.moc == other.moc and self.lokacja == other.lokacja

# elektrownia_wiatrowa = EnergiaOdnawialna("Wiatr", 70, "Niemcy")
# elektrownia_sloneczna = EnergiaOdnawialna("Slonce", 30, "Polska")

# elektrownia_wiatrowa.get_info()
# elektrownia_sloneczna.get_info()

# elektrowania_hybrydowa = elektrownia_wiatrowa + elektrownia_sloneczna
# elektrowania_hybrydowa.get_info()

# print(elektrownia_wiatrowa)
# print(elektrownia_wiatrowa == elektrownia_sloneczna)

# zad. 3.4

# from math import gcd 

# class Fraction:
#     def __init__(self, licznik, mianownik):
#         if mianownik == 0:
#             raise ZeroDivisionError("Mianownik nie może być równy zero.")
#         self.licznik = licznik
#         self.mianownik = mianownik
#         self.skracaj()

#     def skracaj(self):
#         dzielnik = gcd(self.licznik, self.mianownik)
#         self.licznik //= dzielnik
#         self.mianownik //= dzielnik
#         if self.mianownik < 0:
#             self.licznik *= -1
#             self.mianownik *= -1

#     def __repr__(self):
#         return f'Ułamek({self.licznik}, {self.mianownik})'
    
#     def __str__(self):
#         calosc = self.licznik // self.mianownik
#         reszta = self.licznik % self.mianownik 
#         if reszta == 0:
#             return f'{calosc}'
#         elif calosc == 0:
#             return f'{reszta}/{self.mianownik}'
#         else:
#             return f'{calosc} {reszta}/{self.mianownik}'
    
    
# ulamek1 = Fraction(3, 4)
# print (ulamek1)

# ulamek2 = Fraction (6, 12)
# print (ulamek2)

#     def __add__(self, other):
#         licznik = self.licznik * inny.mianownik + inny.licznik * self.mianownik
#         mianownik = self.mianownik * inny.mianownik 
#         return Fraction(licznik, mianownik)
    
#     def __sub__(self, other):
#         licznik = self.licznik * inny.mianownik - inny.licznik * self.mianownik
#         mianownik = self.mianownik * inny.mianownik
#         return Fraction(licznik, mianownik)
    
#     def __mul__(self, other):
#         licznik = self.licznik * inny.licznik
#         mianownik = self.mianownik * inny.mianownik 
#         return Fraction(licznik, mianownik)   

#     def __truediv__(self, other):
#         if inny.licznik == 0:
#             raise ZeroDivisionError("nie można dzielić przez 0!")
#         licznik = self.licznik * inny.mianownik 
#         mianownik = self.mianownik * inny.licznik
#         return Fraction(licznik, mianownik)

#     def __abs__(self):
#         return Fraction(abs(self.licznik), abs(self.mianownik))

#     def __eq__(self):
    
#     ## to ja robiłam, nieskończone a niżej z zajęć

#     import math
# class Fraction:
#     def __init__(self, a, b):
#         if b == 0:
#             raise ZeroDivisionError('Mianownik nie może być 0')
        
#         # skracanie ułamka
#         f_gcd = math.gcd(a, b)
#         self.a = int(a / f_gcd)
#         self.b = int(b / f_gcd)
#         self.value = self.a / self.b

#     def __repr__(self):
#         return f'Fraction({self.a}, {self.b})'

#     def __str__(self):
#         return f'{self.a // self.b} {self.a % self.b}/{self.b}' if self.value > 1 else  f'{self.a}/{self.b}'

#     # operatory arytmetyczne
#     def __add__(self, other):
#         return Fraction(self.a * other.b + other.a * self.b, self.b * other.b)

#     def __sub__(self, other):
#         return Fraction(self.a * other.b - other.a * self.b, self.b * other.b)
        
#     def __mul__(self, other):
#         return Fraction(self.a * other.a, self.b * other.b)
    
#     def __truediv__(self, other):
#         return Fraction(self.a * other.b, self.b * other.a)

#     def __abs__(self):
#         return Fraction(abs(self.a), abs(self.b))

#     # operatory porównania
#     def __eq__(self, other): # ==
#         return self.a == other.a and self.b == other.b

#     def __neq__(self, other): # !=
#         return self.a != other.a or self.b != other.b

#     def __gt__(self, other): # >
#         return self.value > other.value
    
#     def __ge__(self, other): # >=
#         return self.value >= other.value

#     def __lt__(self, other): # <
#         return self.value < other.value
    
#     def __le__(self, other): # <=
#         return self.value <= other.value

#     # metody rzutowania
#     def __float__(self):
#         return self.value

#     def __int__(self):
#         return int(self.value)
    
#     def __bool__(self):
#         return self.value > 0

#     # zaokrąglanie
#     def __round__(self, round_val=0):
#         return round(float(self.value), round_val)        

# fraction1 = Fraction(3, 6)
# print(repr(fraction1))
# print(str(fraction1))

# fraction2 = Fraction(7, 4)
# print(repr(fraction2))
# print(str(fraction2))

# # operatory arytmetyczne
# print('Działania artymetyczne')
# print(Fraction(1, 4) + Fraction(2, 4))
# print(Fraction(3, 4) - Fraction(2, 4))
# print(Fraction(2, 4) * Fraction(2, 4))
# print(Fraction(1, 4) / Fraction(2, 4))
# print(abs(Fraction(-3, 4)))

# # operatory porównania
# print('Porówanie')
# print(Fraction(1, 4) == Fraction(2, 4))
# print(Fraction(3, 4) != Fraction(2, 4))
# print(Fraction(2, 4) > Fraction(2, 4))
# print(Fraction(1, 4) >= Fraction(2, 4))
# print(Fraction(1, 4) < Fraction(2, 4))
# print(Fraction(1, 4) <= Fraction(2, 4))

# # metody rzutowania
# print('Rzutowanie')
# print(float(Fraction(1, 2)))
# print(int(Fraction(1, 2)))
# print(int(Fraction(3, 2)))
# print(bool(Fraction(1, 2)))
# print(bool(Fraction(0, 2)))
# print(round(Fraction(3, 4), 1))


#--- kolejne zadania 
# projektowanie obiektoqw - intrukcja do lab 2 

# modyfikatory dostępu
# zakresy dostępu public, private + protected (kiedyś indziej)

# self.pole_publiczne = a (będzie dostęp)
# self._pole_chronione = b (będzie widoczne)
# self.__pole_prywatne = b (nie dostaniemy się do tego pola, mechanizm obronny)

# dekorator - powiązany z motyfikatorami dostępu
# getter - pobieranie konkretnej wartości (@property) nawet jeśli jest to pole prywatne
# seter - ustawienie jakiejś wartości (@zmienna.setter)
# delater - dana wartość ma być usunięta (@zmienna.delater)

# Zad 3.1

# class Punkt:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
        
#     def __repr__(self):
#         return f'punkt ({self.x}, {self.y})'

#     def położenie(self, prosta):
#         y_obliczone = prosta.oblicz_y(self.x)
#         return self.y == y_obliczone

# class Prosta:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def oblicz_y(self, x):
#         return self.a * x + self.b
    
#     def __repr__(self):
#         return f'prosta: y: {self.a} + {self.b}'
    

# punkt1 = Punkt(3, 6)
# punkt2 = Punkt(-1, 4)
# prosta = Prosta(2, 1)
# print(punkt1)
# print(punkt2)
# print(prosta)

## tu ja probowalam niżej z zajęć

# class Punkt:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y

#     @property
#     def x(self):
#         return self.__x

#     @property
#     def y(self):
#         return self.__y

#     def nalezy_do(self, prosta):
#         return self.__y == prosta.a * self.__x + prosta.b

# class Prosta:
#     def __init__(self, a, b):
#         self.__a = a
#         self.__b = b

#     @property
#     def a(self):
#         return self.__a

#     @property
#     def b(self):
#         return self.__b

#     def miejsce_zerowe(self):
#         return -self.b / self.a if self.a else 'Nie istnieje' if self.b else 'Nieskończenie wiele'

# p = Punkt(3, 6)
# pr = Prosta(2, 0)
# print(p.nalezy_do(pr))
# print(pr.miejsce_zerowe())

# # zad 3.2

# class Punkt:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# def __repr__(self):
#         return f"Punkt({self.x}, {self.y})"

# class Prostokat:
#     def __init__(self, punkt1, punkt2):
#         self.punkt1 = punkt1
#         self.punkt2 = punkt2
#         self.szerokosc = None
#         self.wysokosc = None
#         self.oblicz_boki()

#     def pole(self):
#         return self.bok1 * self.bok2

#     def obwod(self):
#         return 2 * self.bok1 + 2 * self.bok2
    
#     def rysuj(self):
#         plt.plot(self.a.x, self.a.y, color='blue', marker='.', markersize=16)
#         plt.plot(self.b.x, self.b.y, color='blue', marker='.', markersize=16)
#         plt.plot([self.a.x, self.a.x, self.b.x, self.b.x, self.a.x], [self.a.y, self.b.y, self.b.y, self.a.y, self.a.y], color='blue')
#         plt.xlim([0, 6])
#         plt.ylim([0, 4])
#         plt.grid(axis='both', linestyle='--', color='grey', alpha=0.7)
#         plt.show()

# p1 = Punkt(1, 1)
# p2 = Punkt(2, 3)
# prost = Prostokat(p1, p2)
# print(prost.pole())
# print(prost.obwod())  

# # coś nie wychodzi - sprawdzić później z nagraniem 

# zad 3.3

# from datetime import datetime

# class Note:
#     def __init__(self, author, content):
#         self.author = author
#         self.content = content
#         self.creation_time = datetime.now()

#     def __str__(self):
#         time = self.creation_time.strftime("%H:%M")
#         return f"{self.author}: \"{self.content}\" o godzinie {time}"


# class Notebook:
#     def __init__(self):
#         self.notes = []

#     def add_new(self, author, content):
#         new_note = Note(author, content)  
#         self.notes.append(new_note)

#     def add(self, note):
#         if isinstance(note, Note):
#             self.notes.append(note)
#         else:
#             raise TypeError("Dodawany obiekt musi być instancją klasy Note.")
        
#     def note_count(self):
#         return len(self.notes)

#     def display_all(self):
#         if not self.notes:
#             print("Twój notatnik jest pusty.")
#         else:
#             print("Masz takie notatki:")
#             for i, note in enumerate(self.notes, 1):
#                 print(f"{i}. {note}")


# nb = Notebook()
# nb.add_new("Bartek", "Dokończyć instrukcje")
# nb.display_all()
# n1 = Note("Andrii", "Sprawdzić instrukcje")
# nb.add(n1)
# nb.display_all()
# print(f"Liczba notatek: {nb.note_count()}")


# # zad. 3.4

# class Pracownik:
#     def __init__(self, imie, nazwisko, stanowisko):
#         self.imie = imie
#         self.nazwisko = nazwisko
#         self.stanowisko = stanowisko
        
#         self._id_pracownika = id(imie)

#         self.__pensja = 0

#     def przedstaw_sie(self):
#         print(f'Cześć, nazywam się {self.imie} {self.nazwisko} i pracuje na stanowisku: {self.stanowisko}')

#     def __zmien_pensje(self, nowa_pensja):
#         self.__pensja = nowa_pensja

#     def podwyzka(self, pensja):
#         self.__zmien_pensje(pensja)

#     def get_pensja(self):
#         return self.__pensja

# pracownik1 = Pracownik("Jan", "Kowalski", "Inżynier")
# pracownik1.przedstaw_sie()

# pracownik2 = Pracownik("Anna", "Nowak", "Specjalista ds. marketingu")
# pracownik2.przedstaw_sie()

# print(f"ID pracownika 1: {pracownik1._id_pracownika}")
# print(f"ID pracownika 2: {pracownik2._id_pracownika}")

# pracownik1.podwyzka(1000)
# print(f"Wynagrodzenie pracownika 1: {pracownik1.get_pensja()}")

# ZAJĘCIA 25.01

# METODY STATYCZNE 

# zad 2.

# class StringUtls:
#     @staticmethod
#     def reverse(text):
#         return text[::-1]

# odwrocony_tekst = StringUtls.reverse("Pogoda")
# print(odwrocony_tekst)

# # zad 3.
# class Validator:
#     @staticmethod
#     def is_valid_email(email):
#         import re
#         valid_email = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
#         return bool(valid_email.match(email))

# print(Validator.is_valid_email('abcd'))
# print(Validator.is_valid_email('ab @ cd.pl'))
# print(Validator.is_valid_email('ab@cd.pl'))

# zad 4.
# 1 ver. mniej elastyczna
# class DateUtils:
#     @staticmethod
#     def current_date():
#         import datetime
#         cDate = str(datetime.datetime.now())
#         return cDate[:10]

# print(DateUtils.current_date())

# # 2 ver. bardziej elastyczna

# from datetime import datetime

# class DateUtils:
#     @staticmethod
#     def current_date():
#         return datetime.today().strftime('%Y-%m-%d')

# print(DateUtils.current_date())

# zad 9.
# moje chat
# class TextUtils:
#     @staticmethod
#     def count_words(text: str) -> int:
#         return len(text.split())


#     def capitaliza_first_letter(text: str) -> str:
#         return text.title()


# original_text = "hey world"
# word_count = TextUtils.count_words(original_text)
# capitalized_text = TextUtils.capitaliza_first_letter(original_text)

# print(original_text)
# print(word_count)
# print(capitalized_text)

# # z zajęć

# class TextUtils:
#   @staticmethod
#   def count_words(txt):
#     return len(txt.split())
 
#   @staticmethod
#   def capitalize_first_letter(txt):
#     return txt.title()
 
# print(TextUtils.count_words('Ala ma kota'))
# print(TextUtils.capitalize_first_letter('Ala ma kota'))

# DZIEDZICZENIE 

# zad 1.

# class Person:
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age

#     def get_info(self):
#         return f'Imię: {self._name}, Wiek: {self._age}'

# person = Person("Jan", 30)
# print(person.get_info())

# class Student(Person):
#     def __init__(self, name, age, student_id):
#         super().__init__(name, age)
#         self.__student_id = student_id
    
#     def get_info(self):
#         person_info = super().get_info()
#         return f'{person_info}, Student ID: {self.__student_id}'

# student = Student("Jan", 20, 12344)
# print(student.get_info())

# # zad 2.
# class Flying:
#     def fly(self):
#         print("I can fly!")

# class Swimming:
#     def swim(self):
#         print("I can swim!")

# class Duck(Flying, Swimming):
#     def quack(self):
#         print("quack! quack!")

# duck = Duck()
# duck.fly()
# duck.swim()
# duck.quack()

# POLIMORFIZM 

# ZAD 4.
# class Shape():
#     def area(self):
#         raise NotImplementedError('Subclass must implement abstract method')

# class Circle(Shape):
#     def __init__(self, r):
#         self.__r = r
#     def area(self):
#         return 3.14 * self.__r ** 2

# class Rectangle(Shape):
#     def __init__(self, a, b):
#         self.__a = a
#         self.__b = b

#     def area(self):
#         return self.__a * self.__b

# shapes = [Circle(5), Rectangle(3, 7), Circle(2.5), Rectangle(4, 12), Circle(10)]

# for shape in shapes:
#     print(shape.area())

# zad 5.
# moje chat
# class Payable:
#     def calculate_pay(self):
#         raise NotImplementedError('Subclass must implement abstract method')

# class Employee(Payable):
#     def __init__(self, stała_pensja):
#         self.stała_pensja = stała_pensja
    
#     def calculate_pay(self):
#         return self.stała_pensja

# class Contractor(Payable):
#     def __init__(self, stawka_godzinowa, godziny):
#         self.stawka_godzinowa = stawka_godzinowa
#         self.godziny = godziny
    
#     def calculate_pay(self):
#         return self.stawka_godzinowa * self.godziny
    
# def process_payments(payables):
#     for payable in payables:
#         class_name = payable.__class__.__name__
#         pay = payable.calculate_pay()
#         print(f"Wynagrodzenie {class_name}: {pay} zł")

# payables = [
#         Employee(5000),
#         Contractor(100, 40)
# ]
# process_payments(payables)

# # z zajęć
# class Payable:
 
#     def calculate_pay(self):
#         raise NotImplementedError("Subclass must implement abstract method")
   
# class Employee(Payable):
 
#     def __init__(self, pensja):
#         self.pensja = pensja
 
#     def calculate_pay(self):
#         return self.pensja
   
# class Contractor(Payable):
 
#     def __init__(self, stawka, liczba_godzin):
#         self.stawka = stawka
#         self.liczba_godzin = liczba_godzin
 
#     def calculate_pay(self):
#         return self.stawka * self.liczba_godzin
   
# def process_payments(lista):
#     for i in lista:
#         print(i.calculate_pay())
 
# lista1 = [Employee(8000), Contractor(100, 40), Employee(10000), Contractor(90,50)]
 
# process_payments(lista1)

# zad 6.

# class Book():
#     def __init__(self, author, title):
#         self._author = author
#         self.__title = title
#     def get_info(self):
#         return f'{self._author} - {self.__title}'

# class EBook(Book):
#     def __init__(self, author, title, file_size):
#         super().__init__(author, title)
#         self.__file_size = file_size
#     def get_info(self):
#         return f'{super().get_info()}, Size: {self.__file_size}'

# class PrintedBook(Book):
#     def __init__(self, author, title, page_count):
#         super().__init__(author, title)
#         self.__page_count = page_count
#     def get_info(self):
#         return f'{super().get_info()}, Pages: {self.__page_count}'

# books = [EBook('Autor1', 'Tytul1', 25), PrintedBook('Autor2', 'Tytul2', 300)]

# for book in books:
#     print(book.get_info())

# Programowanie obiektowe Lab3

# zad 2.1

# class Animal:
#     def __init__(self, name, age, species, weight):
#         self.name = name
#         self.age = age
#         self.species = species
#         self.weight = weight

#     @staticmethod
#     def oldest_animal(animals):
#         oldest = animals[0]
#         for animal in animals [1:]:
#             if animal.age > oldest.age:
#                 oldest = animal 
#         return oldest.name, oldest.age
    
#     def is_endangered(self):
#         return self.species.lower() == "tygrys"
    
#     def calculate_bmi(self):
#         wzrost = 1 
#         bmi = self.weight / (wzrost ** 2)
#         return bmi
        
# dog = Animal("hugo", 4, "pies", 20)
# cat = Animal("luna", 6, "kot", 15)
# mouse = Animal("micky", 2, "mysz", 2)
# tiger = Animal('kazu', 10, "tygrys", 100)
# animals = [dog, cat, mouse]

# oldest_name, oldest_age = Animal.oldest_animal(animals)
# print(f'Najstarsze zwierzę to {oldest_name} i jest w wieku {oldest_age} lat')

# print(dog.is_endangered())
# print(tiger.is_endangered())
# print(tiger.calculate_bmi())

# #  z zajęć
# class Animal():
#   def __init__(self, name, age, species, weight):
#     self.name = name
#     self.age = age
#     self.species = species
#     self.weight = weight
 
#   @staticmethod
#   def oldest_animal(animals):
#     oldest = max(animals, key = lambda animal: animal.age)
#     return f'Oldest animal - name: {oldest.name}, age: {oldest.age}'
 
#   def is_endangered(self):
#     return self.species == 'tiger'
 
#   def calculate_bmi(self):
#     height = 1
#     return self.weight / height ** 2
 
# lion = Animal('Simba', 5, 'lion', 200)
# tiger = Animal('Shere Khan', 8, 'tiger', 150)
# elephant = Animal('Dumbo', 3, 'elephant', 400)
# animals = [lion, tiger, elephant]
 
# print(Animal.oldest_animal(animals))
# print(lion.is_endangered())
# print(tiger.is_endangered())
# print(lion.calculate_bmi())
# print(tiger.calculate_bmi())

# zad 2.2

# class Animal():
#     def __init__(self, name, age, species, weight):
#         self.name = name
#         self.age = age
#         self.species = species
#         self.weight = weight
    
#     def __repr__(self):
#         return f'Animal(name={self.name}, age={self.age}, species={self.species}, weight={self.weight})'

#     @staticmethod
#     def oldest_animal(animals):
#         oldest = max(animals, key = lambda animal: animal.age)
#         return f'Oldest animal - name: {oldest.name}, age: {oldest.age}'
 
#     def is_endangered(self):
#         list_of_endangered = {
#             'tiger': True,
#             'lion': True,
#             'elephant': False,
#             'dog': False
#         }

#         if self.species in list(list_of_endangered.keys()):
#             return list_of_endangered[self.species]
        
#         return 'Nie mamy informacji o tym gatunku'

#     def calculate_bmi(self):
#         height = 1
#         return self.weight / height ** 2

# class Farm:
#     def __init__(self, animals = []):
#         self.animals = animals
    
#     def add_animal(self, animal):
#         if not isinstance(animal, Animal):
#             raise ValueError('Podana wartość nie jest typu klasy Animal')

#         self.animals.append(animal)
    
#     def feed_all(self, food):
#         print(f'Feeding all animals on farm with {food}:')
#         for animal in self.animals:
#             print(f'{animal.name} the {animal.species} is being fed.')
#         print('All animals have been fed.')
        
#     @classmethod
#     def create_farm_with_animals(cls, animals):
#         return cls(animals)
    
# farm = Farm()
# cow = Animal("Berta", 5, "cow", 400)
# farm.add_animal(cow)
# chicken1 = Animal("Chirpy", 1, "chicken", 1)
# farm.add_animal(chicken1)
# chicken2 = Animal("Cluck", 2, "chicken", 1.2)
# farm.add_animal(chicken2)
# print(farm.animals)

# farm.feed_all('corn')
# animals = [
#     Animal("Berta", 5, "cow", 400),
#     Animal("Chirpy", 1, "chicken", 1),
#     Animal("Cluck", 2, "chicken", 1.2)
# ]
# farm1 = Farm.create_farm_with_animals(animals)
# print(farm1.animals)

# zad 2.3

# class Student:
#     def __init__(self, first_name, last_name, age, gpa, year):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.gpa = gpa
#         self.year = year

#     def get_full_name(self):
#         return f'{self.first_name} {self.last_name}'

#     def is_on_probation(self):
#         return self.gpa < 2.0
    
#     def get_average_age(students):
#         total_age = sum(student.age for student in students)
#         return total_age / len(students) if students else 0
    
# student1 = Student('Jan', "Kowalski", 20, 2, 3.5)
# student2 = Student("Anna", "Nowak", 22, 3, 2.8)
# student3 = Student("Piotr", "Czerwinski", 19, 1, 2.1)
# student4 = Student("Katarzyna", "Wójcik", 21, 4, 4.0)
# students = [student1, student2, student3, student4]
# average_age = Student.get_average_age(students)

# print(student1.get_full_name())
# print(student1.is_on_probation())
# print(f'Sredni wiek studentów to {average_age}')

# # --- rozwiązanie prowadzącego
# import numpy as np

# class Student:
#     def __init__(self, first_name, last_name, age, year, gpa):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.gpa = gpa
#         self.year = year

#     def get_full_name(self):
#         return f"{self.first_name} {self.last_name} ({self.age} lat, średnia ocen: {self.gpa})"
    
#     def is_on_probation(self):
#         return self.gpa < 3.0
    
#     @staticmethod
#     def get_average_age(students):
#         # return sum([student.age for student in students]) / len(students)
#         return np.mean([student.age for student in students])

#     @staticmethod
#     def get_students_by_year(students):
#         students_by_year = {}
#         for i in range(1, 6):
#             students_by_year[i] = [student for student in students if student.year == i]
    
#         return students_by_year
    
#     @staticmethod
#     def print_students_by_year(students):
#         students_by_year = Student.get_students_by_year(students)
#         for key, value in students_by_year.items():
#             print(f'{key} rok:')
#             for val in value:
#                 if isinstance(val, Student):
#                     print(val.get_full_name())
#                 else:
#                     print('Nie jest to obiekt klasy Student')
    
# s1 = Student("Jan", "Kowalski", 20, 2, 3.5)
# s2 = Student("Anna", "Nowak", 22, 3, 2.8)
# s3 = Student("Piotr", "Czerwinski", 19, 1, 2.1)
# s4 = Student("Katarzyna", "Wójcik", 21, 4, 4.0)
# print(s1.is_on_probation())
# print(s2.is_on_probation())
# students = [s1, s2, s3, s4]
# print(Student.get_average_age(students))

# Student.print_students_by_year(students)

# 26.01.2025

# zad. 2.4

# Zadanie 2.4

# class Athlete:
#     team = None
#     country = None

#     def __init__(self, name, age, height, weight, sport):
#         self.name = name
#         self.age = age
#         self.height = height
#         self.weight = weight
#         self.sport = sport
    
#     def get_bmi(self):
#         return self.weight / (self.height / 100) ** 2
    
#     def get_info(self):
#         return f'Name: {self.name}, Age: {self.age}, Height: {self.height}cm, ' \
#             f'Weight: {self.weight}kg, Sport: {self.sport}, Team {self.team}, Country: {self.country}'
# #         return f'''
# # Name: {self.name}, 
# # Age: {self.age},
# # Height: {self.height}cm, 
# # Weight: {self.weight}kg, 
# # Sport: {self.sport}, 
# # Team {self.team}, 
# # Country: {self.country}
# #         '''

#     @classmethod
#     def set_team(cls, team):
#         cls.team = team

#     @classmethod
#     def set_country(cls, country):
#         cls.country = country
    
# athlete1 = Athlete("Adam Nowak", 25, 175, 75, "football")
# athlete2 = Athlete("Ewa Kowalska", 30, 180, 68, "tennis")

# print(athlete1.get_info())
# print(athlete2.get_info())

# athlete1.set_team("Real Madrid")
# athlete2.set_country("Poland")

# print(athlete1.get_bmi())
# print(athlete1.get_info())
# print(athlete2.get_info())

# athlete2.set_country("Italy")

# print(athlete1.get_info())
# print(athlete2.get_info())

# ---
# Zadania wzorce projektowe
# zad. 1
import abc 

# class Logger():
#     _instance = None
#     __logs = []
 
#     def __new__(cls):
#         if not cls._instance:
#             cls._instance = super(Logger, cls).__new__(cls)
#         return cls._instance
 
#     @classmethod
#     def log(cls, level, message):
#         cls.__logs.append({'level': level, 'message': message})
 
#     @classmethod
#     def get_all_logs(cls):
#         return cls.__logs
 
 
# logger1 = Logger()
# logger1.log('INFO', 'Info message from logger 1')
# logger1.log('ERROR', 'Error message from logger 1')
 
# logger2 = Logger()
# logger2.log('INFO', 'Info message from logger 2')
# logger2.log('WARNING', 'Warning message from logger 2')
 
# print(logger2.get_all_logs())

# zad 2. 
# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return 3.14159 * self.radius ** 2

# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.width * self.height

# class ShapeFactory:
#     @staticmethod
#     def create_shape(shape_type, *args):
#         if shape_type == "circle":
#             return Circle(*args)
#         elif shape_type == "rectangle":
#             return Rectangle(*args)
#         else:
#             raise ValueError("Unknown shape type")

# circle = ShapeFactory.create_shape("circle", 5)
# rectangle = ShapeFactory.create_shape("rectangle", 4, 6)
# print(circle.area())
# print(rectangle.area())

# # z zajęć
# from abc import ABC, abstractmethod
 
# class Product(ABC):
#     @abstractmethod
#     def area(self):
#         pass
 
# class Rectangle(Product):
#     def __init__(self, a, b):
#         super().__init__()
#         self.a = a
#         self.b = b
 
#     def area(self):
#         return self.a * self.b
 
# class Circle(Product):
#     def __init__(self, r):
#         super().__init__()
#         self.r = r
 
#     def area(self):
#         return 3.14 * self.r ** 2
 
# class Creator(ABC):
#     @abstractmethod
#     def create(self):
#         pass
 
# class RectangleCreator(Creator):
#     def create(self, a, b):
#         return Rectangle(a, b)
 
# class CircleCreator(Creator):
#     def create(self, r):
#         return Circle(r)
 
# # Przykład użycia
# rectangle_creator = RectangleCreator()
# circle_creator = CircleCreator()
 
# rectangle = rectangle_creator.create(2, 5)
# circle = circle_creator.create(3)
 
# print(rectangle.area())
# print(circle.area())

# zad. 3

# class TemperatureSensor:
#     def __init__(self):
#         self._observers = []
#         self._temperature = None

#     def add_observer(self, observer):
#         self._observers.append(observer)

#     def remove_observer(self, observer):
#         self._observers.remove(observer)

#     def set_temperature(self, temperature):
#         self._temperature = temperature
#         self._notify_observers()

#     def _notify_observers(self):
#         for observer in self._observers:
#             observer.update(self._temperature)

# class TemperatureDisplay:
#     def update(self, temperature):
#         print(f"Aktualna temperatura: {temperature} stopni.")


# sensor = TemperatureSensor()
# display_1 = TemperatureDisplay()
# display_2 = TemperatureDisplay()
# display_3 = TemperatureDisplay()
# sensor.add_observer(display_1)
# sensor.add_observer(display_2)
# sensor.add_observer(display_3)

# sensor.set_temperature(25)  

# zad. 5 (4 ominięte)

class VendingMachine:
    def __init__(self, initial_state):
        self._state = initial_state

    def set_state(self, state):
        self._state = state

    def request_item(self):
        self._state.request_item()

    def dispense_item(self):
        self._state.dispense_item()

class State:
    def request_item(self):
        pass

    def dispense_item(self):
        pass

class ReadyState(State):
    def request_item(self):
        print("Item selected. Ready to dispense.")

    def dispense_item(self):
        print("Please select an item first.")

class DispenseState(State):
    def request_item(self):
        print("Item already selected. Dispensing now.")

    def dispense_item(self):
        print("Item dispensed. Thank you!")

class OutOfStockState(State):
    def request_item(self):
        print("Sorry, the machine is out of stock.")

    def dispense_item(self):
        print("Out of stock. Please select another item.")

# Przykład użycia
ready_state = ReadyState()
dispense_state = DispenseState()
out_of_stock_state = OutOfStockState()

vending_machine = VendingMachine(ready_state)

vending_machine.request_item()  # Item selected. Ready to dispense.
vending_machine.dispense_item()  # Please select an item first.

vending_machine.set_state


