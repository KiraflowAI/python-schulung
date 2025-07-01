#Schreibe eine Funktion alle_gleich(a, b, c), die drei Parameter annimmt und True zurückgibt, wenn alle gleich sind und False, wenn nicht.

# print(alle_gleich(1, 1, 1)) # True
# print(alle_gleich(3, 1 + 1 + 1, 5 - 2)) # True
# print(alle_gleich(1, 1, 2)) # False
# print(alle_gleich(3, 2, 1)) # False


#Mit a == b können wir prüfen, ob zwei Elemente gleich sind.


# def alle_gleich(a, b, c):
#     return a == b == c



# def alle_gleich(a, b, c):
#     if a == b == c:
#         print("Alle Werte sind gleich.")
#     else:
#         print("Werte sind nicht gleich.")


# print(alle_gleich(1, 1, 1)) # True
# print(alle_gleich(3, 1 + 1 + 1, 5 - 2)) # True
# print(alle_gleich(1, 1, 2)) # False
# print(alle_gleich(3, 2, 1)) # False


def alle_gleich(a, b, c):
    return a == b == c

# --- Eingabe vom Benutzer ---
x = int(input("Gib die erste Zahl ein: "))
y = int(input("Gib die zweite Zahl ein: "))
z = int(input("Gib die dritte Zahl ein: "))

# --- Ergebnis prüfen und ausgeben ---
if alle_gleich(x, y, z):
    print("✅ Alle drei Werte sind gleich.")
else:
    print("❌ Die Werte sind nicht gleich.")
