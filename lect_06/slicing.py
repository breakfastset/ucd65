
animals = ["ape", "monkey", "gorilla", "camel", "narwhal", "honey badger", "elephant", "mouse"]
#           0       1        2            3         4            5             6         7
#         -8      -7                                           -3             -2         -1

animals_1 = animals[2:6]    # indexes 2 to 5     list_name[start:end:step]
print(animals_1)

animals_2 = animals[1:6:2]  # indexes 1, 3, 5
print(animals_2)

animals_3 = animals[:5]     # indexes 0 to 4
print(animals_3)

animals_4 = animals[4:]     # indexes 4 to 7
print(animals_4)

animals_5 = animals[:]      # a copy of animals
print(animals_5)

animals_6 = animals[::-1]   # a copy of animals in reverse
print(animals_6)