
#  Podstawy programowania Python Kolekcje Przepływ Funkcje

# Zad 1.1.1
# my_list = []

# my_list.append("python")
# my_list.append("is ok")
# my_list.append("sometimes")

# my_list.remove("sometimes")

# my_list[1] = "is neat"

# assert my_list == ["python", "is neat"]

# zad 1.1.2

original = ["I", "am", "learning", "hacking", "in"]

modified = original[:]
modified[3] = "lists"
modified.append("Python")

assert original == ["I", "am", "learning", "hacking", "in"]
assert modified == ["I", "am", "learning", "lists", "in", "Python"]

print(modified)
print(original)