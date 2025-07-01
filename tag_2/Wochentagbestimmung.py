# Eingabe einer Zahl zwischen 1 und 7 durch den Benutzer
zahl = int(input("Bitte geben Sie eine Zahl zwischen 1 und 7 ein: "))

# Überprüfung, ob die eingegebene Zahl im gültigen Bereich liegt
if zahl == 1:
    print("Montag")
elif zahl == 2:
    print("Dienstag")
elif zahl == 3:
    print("Mittwoch")
elif zahl == 4:
    print("Donnerstag")
elif zahl == 5:
    print("Freitag")
elif zahl == 6:
    print("Samstag")
elif zahl == 7:
    print("Sonntag")
else:
    print("Fehler: Die eingegebene Zahl liegt außerhalb des gültigen Bereichs.")
