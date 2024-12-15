# with open ('nowy plik.txt', 'w') as f:
#     f.write('ala ma kota\n')
    
with open('nowy plik.txt', 'r') as f:
    line = f.readline()
    print('readline:', line)

with open ('nowy plik.txt', 'r') as f:
    s = f.read()
    print('read:', s)

#dopisanie na koniec pliku

# with open('nowy plik.txt', 'a') as f:
#     f.write('a jan ma psa\n')
    
# with open('nowy plik.txt', 'r') as f:
#     lines = f.readline()
#     print('readlines:', lines)

# with open('nowy plik.txt', 'r') as f:
#     s = f.read()
#     print('read:', s)