# KLASSEN
# Ein sehr nützliches Werkzeug, bzw. Bereich der Informatik ist die objektorientierte Programmierung (OOP). 
# Im Gegensatz zu prozeduralem Programmieren, orientiert sich OOP 
# an realen Objekten, die wir als Klassen bezeichnen und als eine Art Blaupause benutzen.
# Stellen wir uns als Beispiel vor wir würden in einem größeren Projekt, welches sich mit Autos 
# beschäftigt, sitzen. Wir wissen, dass jedes Auto verschiedene Eigenschaften, wie Marke, Farbe, Türanzahl,
#  etc. hat. Hier wäre es lohenswert sich eine Klasse Car zu erstellen, die als Attribute genau diese Eigenschaften enthält. 
# Auf diese Weise hätten wir eine Blaupause, die wir für jedes Auto nutzen können.

#VORTEILE VON OOP
# Es gibt viele Gründe warum oft mit OOP gearbeitet wird. Einige hiervon sind bspw. die Modularität und Wiederverwendbarkeit.
# Durch die Unterteilung in Klassen gewinnt der Code mehr an Übersichtlichkeit, was die Wartung und Erweiterung von diesem erleichtert. 
# Genauso lassen sich Klassen über das aktuelle Projekt hinaus benutzen. Statt bereits geschriebenen Code ins eigene Projekt zu kopieren 
# und anzupassen, kann man mithilfe von OOP diesen importieren und ist damit sofort nutzbar. Diese Stärke zeigt sich später noch sehr stark, 
# da es in Python viele sogenannte Module gibt, die solchen bereits geschriebenen Code enthalten und für uns nutzbar sind.


#MINIMALBEISPIEL
#Die einfachste und langweiligste Klasse, die man erstellen kann, ist folgende:



# Hier wird eine Klasse Car erstellt, in der allerdings nichts passiert. pass führt hierbei keinen Code aus, 
# ist aber syntaktisch notwendig. Diese Klasse ist jetzt für uns an der Stelle eine Blaupause mit der wir 
# sogenannte Instanzen erzeugen können, in unserem Beispiel: explizite Autos. Diese Klasse ist jetzt für uns an 
# der Stelle eine Blaupause mit der wir sogenannte Instanzen erzeugen können, in unserem Beispiel: explizite Autos.
# Wichtig ist die Konvention zu erwähnen, dass Klassen allgemein groß geschrieben werden.
# Wir erzeugen im Folgenden drei Instanzen der Klasse Car und schauen uns diese etwas genauer an:

# Erzeugung der Instanzen



class Car():
    pass # kleinstmögliche klasse die existiert, pass macht nichts, pass steht für keinen inhalt - es erwartet eine eingabe

car_1 = Car() # der klasse car() wird die variable car_1 zugewiesen
car_2 = Car() # instanz einer Klasse, car_2 ist ein objekt der klasse car()
car_3 = car_2 # auto 3 wird auto 2 zugewiesen

# Datentyp
print("Datentyp:")
print("Datentyp car_1:  ", type(car_1)) # hier werd der typ ausgebenen, es handelt sich um eine klasse
print("Datentyp car_2:  ", type(car_2))
print("Datentyp car_3:  ", type(car_3))

# Speicheradresse
print("\nSpeicheradresse:")
print("id car_ 1:  ", id(car_1)) # hier wird  mit id - die id nummer ausgegeben also , immer unterschiedlich
print("id car_ 2:  ", id(car_2)) # nur bei 3 und 2 ist das der selbespeicherort
print("id car_ 3:  ", id(car_3)) # 

# Datentyp:
# Datentyp car_1:   <class '__main__.Car'>
# Datentyp car_2:   <class '__main__.Car'>
# Datentyp car_3:   <class '__main__.Car'>

# Speicheradresse:
# id car_ 1:   1803873842864
# id car_ 2:   1803873200816
# id car_ 3:   1803873200816


# Was sehen wir hier?

# zunächst werden drei Instanzen der Klasse car erzeugt. 
# Hier finden wir die selbe Syntax wie bei einer Variablenzuweisung vor.
# Der Datentyp scheint in allen drei Fällen <class '__main__.Car'> zu sein. 
# Hier sehen wir, dass alle drei Variablen Instanzen der Klasse Car sind. Das __main__ sagt uns lediglich, 
# dass die Klasse in unserem aktuellen Code definiert und nicht importiert wurde.
# Die Speicheradresse von car_2 und car_3 sind die selben, da die Zuweisung lediglich eine Referenz zu dem Speicherort 
# der Instanz ist. Damit zeigen car_2 und car_3 auch auf das selbe Objekt, in unserem Fall auf das selbe Auto.
