#Erstelle mit Hilfe von drei List Comprehensions aus der folgenden Liste drei Teillisten.

#["Hallo", "Johannes", "Tina", "", "33"]


# a) Alle Elemente mit höchstens 4 Zeichen: ["Tina", "", "33"]

# b) Alle Elemente, mit einem "n": ["Johannes", "Tina"]

# c) Alle Elemente, die kein "l" haben: ["Johannes", "Tina", "", "33"]

liste = ['Hallo', 'Johannes', 'Tina', '', '33']

teil_a = [elem for elem in liste if len(elem) <= 4]
teil_b = [elem for elem in liste if 'n' in elem]
teil_c = [elem for elem in liste if not 'l' in elem]

print(teil_a)
print(teil_b)
print(teil_c)