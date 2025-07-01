#Welche listen werden in jeder Zeile jeweils erzeugt?

print(list(range(10)) )             #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(1, 11)))           #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(range(0, 30, 5)))        # [0, 5, 10, 15, 20, 25]
print(list(range(0, 10, 3)))        # [0, 3, 6, 9]
print(list(range(0, -10, -1)))      # [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
print(list(range(0)))               # []  Keine Elemente heißt leere Liste
print(list(range(1, 0)))            # []   der zweite Paramter ist kleiner alds der erste, daher werden keine Elemente durchlaufen.
