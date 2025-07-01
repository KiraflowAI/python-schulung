#pandas ist ein Modul, welches uns den Umgang mit Daten vereinfacht. Dabei arbeitet man oft ähnlich wie bei Excel in einer Tabellenstruktur, wobei Pandas hierbei viel mehr Möglichkeiten bietet und durch eine entsprechend große Bibliothek den von uns am Ende zu schreibenden Code minimiert.


#Um Pandas zu installieren, führe in der Konsole (am besten in deiner venv) den folgenden Befehl aus:

#pip install pandas


#Dadurch wird das Modul pandas installiert und kann nun in deinen Dateien importiert werden.





#PANDAS IMPORTIEREN
#In der Regel werden bei der Bearbeitung von Daten eine Vielzahl an Funktionen und Methoden aus pandas benutzt, weshalb meistens das gesamte Modul importiert wird:


#import pandas


#Jetzt hätten wir allerdings das relativ nervige Problem, dass wir vor jedem Objekt ein pandas. schreiben müssten, allerdings gibt es hierfür eine einfache Lösung:

# Wir geben dem Modul einfach ein Kürzel! Standardmäßig wird hier pandas mit pd abgekürzt.

# Der import-Befehl sieht im Anschluss folgendermaßen aus:


#import pandas as pd




#Daten können in verschiedenen Formaten vorliegen. Gängig sind hier bspw. csv-Dateien. Für viele Formate bietet Pandas eine Methode zum einlesen an:


import pandas as pd

# Beispiel: Einlesen einer csv-Datei

df = pd.read_csv("bookstore.csv")

display(df)