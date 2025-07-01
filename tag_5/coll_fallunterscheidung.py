#a) Gegeben sei die folgende Liste. Erstellen Sie mit Hilfe von List Comprehension eine Kopie dieser Liste, bei der sollen jedoch Wörter, die mit "E" beginnen durch drei Sterne "***" ersetzt werden.

["Eins", "Zwei", "Drei", "Elefant", "Apfel", "Esel"]

liste = ["Eins", "Zwei", "Drei", "Elefant", "Apfel", "Esel"]
neue_liste = ['***' if item [0] == 'w' else item for item in liste]
print(neue_liste)

## Ausgabe: ["***", "Zwei", "Drei", "***", "Apfel", "***"]

#b) Gegeben sei die folgende Liste. Erstellen Sie mit Hilfe einer List Comprehension eine Kopie dieser Liste, bei der jede Zahl, die größer als 20 ist, durch "groß" ersetzt wird, ansonsten durch "klein".

[5, 20, 35, 10, 25]

liste_zahl = [5, 20, 35, 10, 25]
neue_liste_zahl = ['groß' if zahl > 20 else 'klein' for zahl in liste_zahl]
print(neue_liste_zahl)

# Ausgabe: ["klein", "klein", "groß", "klein", "groß"]


#c.) Gegeben sei die folgende Liste. Erstellen sie mit hilfe von list comp eine kopie dieser liste bei der
# jede Zahl größer als 30 durch "heiß" ersetzt wird,
# jede Zahl größer als 12 und kleiner als 30 durch "mild" ersetzt wird und
# jede Zahl unter 12 durch "kühl" ersetzt wird.


numbers = [10, 15, 30, 45, -5, 25]

neue_liste_numbers = ['Heiß' if num > 30 else 'mild' if num > 12 else 'kühl' for num in numbers]

print(neue_liste_numbers)

#["kühl", "mild", "mild", "heiß", "kühl", "mild"]