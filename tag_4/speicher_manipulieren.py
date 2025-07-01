#Schreibe ein Programm, das in einer Liste die Zahlen von 0 bis 8 gespeichert hat. Ziel dieses Programms ist es nun die gespeicherten Zahlen durch Nutzereingaben zu manipulieren.
#Das Programm fragt dann den Nutzer nach einer Zahl zwischen 0 und 8. Es speichert diese Eingabe in der Variable namens pos.
#Das Programm fragt den Nutzer dann nach dem zu speichernden Text. Dieser Text wird nun in der Liste an der Postion pos gespeichert und der bisherige Wert wird überschrieben.
#Erweitere das Programm so, dass der Nutzer immer wieder abgefragt wird.
#Die Konsolenausgabe sollte dann wie folgt aussehen:

# Tipps ohne Code:

# Lege dir zunächst eine Variable speicher an mit den Zahlen von 0 bis 8 (siehe Übungsaufgabe Listen definieren mit Zahlen).
# Um eine Schleife dauerhaft für immer zu durchlaufen, kann als Bedingung True genutzt werden.
# Nutzerabfragen können mit der input Funktion eingeholt werden.
# Nutzereingaben liefern immer nur Strings zurück. Wenn sie als Integer gebraucht werden, nutze int(input(...)).
# Die Postion, die manipuliert werden muss, steht in pos.

# speicher = ...
# while ...:
#     print(f"Bisheriger Speicher: { speicher }")
#     pos = ...
#     eingabe = ...
#     speicher[...] = ...
#     print()

speicher = [0, 1, 2, 3, 4, 5, 6, 7, 8]
while True:
    print(f'Bisheriger Speicher: {speicher}')
    pos =  int(input('An welcher Stelle (0-8) soll gespeichert werden?'))
    eingabe = input('Was soll gespeichert werden?')
    speicher [pos] = eingabe
    print()

    
