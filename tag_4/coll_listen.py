# Listen
# Derzeit können wir in einer Variablen genau einen Wert speichern.

# Wir werden nun Möglichkeiten kennenlernen, wie wir in einer Variable eine große Menge von Daten speichern können.

# Die wichtigste Möglichkeit zum Speichern großer Datenmengen in einer Variable sind Listen.

# Eine Liste kann man sich vorstellen wie eine Variable mit mehreren durchnummerierten Schubladen. Die Nummerierung startet mit 0, geht dann weiter zu 1, weiter zu 2 usw.

# Wir können eine Liste definieren, indem wir die zu speichernden Elemente in eckige Klammern ([...]) schreiben.

# Um nun auf die Elemente zuzugreifen, schreiben wir nach dem Variablennamen eckige Klammern, die den Eintrag, welchen wir haben möchten, angeben:


trinkgeld = [70, 60, 15, 15, 0, 100, 0]

print(f'Montag: {trinkgeld[0]}')
print(f'Dienstag: {trinkgeld[1]}')
print(f'Mittwoch: {trinkgeld[2]}')
print(f'Donnerstag: {trinkgeld[3]}')
print(f'Freitag: {trinkgeld[4]}')
print(f'Samstag: {trinkgeld[5]}')
print(f'Sonntag: {trinkgeld[6]}')

#Beachte, dass der erste Eintrag den Index 0 hat, der zweite den Index 1 usw. Wenn die Liste n Elemente hat, 
# dann ist der letzte Index n-1. Wenn eine Liste also 7 Einträge hat, der letzte Index auf den man zugreifen kann die 6.

supremes = ['Diana', 'Mary', 'Florence']
print(supremes)
supremes[2] = 'Cindy' # Hier wird die zweitee Stelle, also Florence (0=Diana, 1=Mary, 2=Florence) mit cindy ausgetauscht, Cindy wird mit supremes [2] , innerhalb der Liste ausgetauscht
print(supremes)

my_var = 5
print(my_var) # Zugriff direkt über den Namen der Variablen
my_var = 6 # Überschreiben der Variablen
print(my_var)

my_list = [5, 8, 5, 1, 0,80]
print(my_list[0]) # Zugriff auf Element über den Index 0
my_list[0] = 10 # Überschreiben des Elements an dem Index
print(my_list) # Konsolenausgabe der gesamten Liste

