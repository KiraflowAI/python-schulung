# slicing (Ein teilbereich einer liste)

a = [0, 1, 2, 3, 4, 5, 6]
print(a[2:6])                   # der erste index ist einschließlich der zweite ausschließlich

# Hier wird ab der 2. stelle bis zu 6. stelle gesliced , 2,3,4,5

a = [0, 1, 2, 3, 4, 5, 6]
# alles ab der dritten position bis zum ende
print(a[3:]) # zweite stelle wird leer gelassen

a = [0, 1, 2, 3, 4, 5, 6]
print(a[:3]) # alles bis zur dritten position

a = [0, 1, 2, 3, 4, 5, 6]
print(a[:-1]) 

# Rückwarts alles bis zum letzten eintrag
a = [0, 1, 2, 3, 4, 5, 6]
print(a[-3:]) # Hier werde die ersten drei stellen subtrahiert und bis zum letzten punkt gezählt

a = [0, 1, 2, 3, 4, 5, 6] #verwendung eines dritten operators
# von anfang bis ende :  :  :2 vom ersten bis zum letzten eintrag in zweier schritten
print(a[1:4:2])

a = [0, 1, 2, 3, 4, 5, 6]
print(a[::-1]) # Rückwärts durchlauf mit minus -1

a = [0, 1, 2, 3, 4, 5, 6]
print(a[4:1:-1]) # vom vierten bis zum ersten eintrag 

fruechte = ["Apfel", "Banane", "Zitrone", "Birne"]
print(fruechte[0:2]) # gibt ('Apfel', 'Banane') aus

#Slices werden mit 3 Werten angegeben. Dem Startwert, dem nicht-inklusiven Endwert und der Schrittweite:
#Wenn wir also [2:6:2] schreiben, sagen wir, dass wir beim dritten Element starten wollen, dann jedes zweite Element nehmen und bei fünf (Stopwert ist exklusiv) aufhören. Also erhalten wir das dritte und das fünfte Element.

#Übrigens kann man auch bei Strings Slicing betreiben:
print("hallo, wie geht es dir?"[1:3]) 



