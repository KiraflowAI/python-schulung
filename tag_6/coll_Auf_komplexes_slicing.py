satz = ["Programmieren", "macht", "Spaß!", "Glaubst", "du", "mir?"]

# 1. print(satz[0][0])
# satz[0] -> "Programmieren"; "Programmieren"[0] -> "P"
print(satz[0][0])   # Ausgabe: P

# 2. print(satz[:2][-1])
# satz[:2] -> ["Programmieren", "macht"]; [-1] gibt das letzte Element zurück -> "macht"
print(satz[:2][-1]) # Ausgabe: macht

# 3. print(satz[:2][-1:])
# satz[:2] -> ["Programmieren", "macht"]; [-1:] gibt einen Slice als Liste zurück -> ["macht"]
print(satz[:2][-1:])  # Ausgabe: ['macht']

# 4. print(satz[2][-1:])
# satz[2] -> "Spaß!"; "Spaß!"[-1:] -> "!" (letztes Zeichen als String)
print(satz[2][-1:])   # Ausgabe: !

# 5. print(satz[1:][-1][-1:])
# satz[1:] -> ["macht", "Spaß!", "Glaubst", "du", "mir?"]
# [-1] wählt das letzte Element -> "mir?"
# "mir?"[-1:] -> "?" (als String)
print(satz[1:][-1][-1:])  # Ausgabe: ?

# 6. print(satz[3][2:4])
# satz[3] -> "Glaubst"; "Glaubst"[2:4] -> "au" (Zeichen an Index 2 und 3)
print(satz[3][2:4])   # Ausgabe: au

# 7. print(satz[3:-1][2:4][3])
# satz[3:-1] -> Elemente von Index 3 bis zum vorletzten: ["Glaubst", "du"]
# [2:4] auf dieser Liste: Da die Liste nur 2 Elemente hat, liefert [2:4] eine leere Liste []
# Der Versuch, [3] auf [] anzuwenden, führt zu einem IndexError.
print(satz[3:-1][2:4][3])  # Fehler: IndexError

# 8. print(satz[3][2][0])
# satz[3] -> "Glaubst"; "Glaubst"[2] -> "a"; "a"[0] -> "a"
print(satz[3][2][0])  # Ausgabe: a

# 9. print(satz[3][-2][1][2])
# satz[3] -> "Glaubst"; "Glaubst"[-2] -> "s" (zweiter letzter Buchstabe)
# "s" hat nur einen Buchstaben, daher führt "s"[1] zu einem IndexError.
print(satz[3][-2][1][2])  # Fehler: IndexError

# 10. print(satz[:-2][2:][:2])
# satz[:-2] -> alles außer den letzten beiden Elementen: ["Programmieren", "macht", "Spaß!", "Glaubst"]
# [2:] -> ab Index 2: ["Spaß!", "Glaubst"]
# [:2] -> die ersten 2 Elemente dieser Liste: ["Spaß!", "Glaubst"]
print(satz[:-2][2:][:2])  # Ausgabe: ['Spaß!', 'Glaubst']

# Zusammenfassung:
# Die Zeilen 7 und 9 führen zu einer Fehlermeldung (IndexError).

