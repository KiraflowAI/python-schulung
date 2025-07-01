fragezeichen = ['Justus'] # Liste wird erstellt.
fragezeichen.append('Peter') # Neues Element wird mit `append` hinzugefügt.
fragezeichen.append('Bob')
print(fragezeichen)

# Zu einer Liste können neue Elemente mit der Methode append hinzugefügt werden. 

einkaufskorb = []
print(einkaufskorb.extend(['Apfel', 'Birne'])) #extend kann man verwenden, um innerhalb der Ausgabe die leere Liste zu erweitern
print(einkaufskorb)

einkaufskorb_2 = []
print(einkaufskorb_2)

einkaufskorb_2.append('Kirschen') #Bei Erweiterung der leeren Liste [], mit .append müssen die einzelnen indexstellen definiert werden
einkaufskorb_2.append('Erdbeeren')
einkaufskorb_2.append('Brombeeren')

print(einkaufskorb_2)

einkaufskorb_3 = []
print(f'Im Einkaufskorb befinden sich {len(einkaufskorb_3)} Produkte') # mit  der Funktion {len}, wird die Länge/Anzahl innerhalb der Liste ausgegeben

einkaufskorb_3.append('Kakao')
einkaufskorb_3.append('Mandelmilch')
einkaufskorb_3.append('Guarana')

print(f'Im Einkaufskorb befinden sich {len(einkaufskorb_3)} Produkte') # mit  der Funktion {len}, wird die Länge/Anzahl innerhalb der Liste ausgegeben
# print muss man nach der Erweiterung der Liste, wieder neu schreiben & ausführen



