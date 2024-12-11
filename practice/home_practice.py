list_a = list(range(0, 10, 2))
list_b = ['a', 'b', 'c']
for a, b in zip(list_a, list_b):
    print(f'{a} - {b}')
    