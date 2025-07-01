# #Bei dem folgenden Code soll der Flächeninhalt eines Kreises berechnet werden. Der Radius des Kreises hat in diesem Beispiel eine Länge von 2. Die Fläche eines Kreises lässt sich allgemein mit 
# A = π⋅r 2
# A=π⋅r 2
# berechnen.
# Es hat sich beim importieren von dem Modul math ein Fehler eingeschlichen. Führe zunächst den nachfolgenden Code aus und schaue dir die Fehlermeldung an. Korrigiere den Code soweit, dass dieser wie oben beschrieben funktioniert.



                        # from math import pi

                        # radius = 2
                        # circle_area = math.pi * radius**2
                        # print(circle_area)


# Diese Fehlermeldung sagt uns, dass Python momentan math nicht kennt. Wenn wir uns den Import von math in der erste Zeile des Codes anschauen, stellen wir fest, dass nicht math importiert wurde, sondern lediglich die Konstante pi aus math. Dieser Fehler lässt sich auf zwei Weisen lösen:

# Variante 1:

# Wir importieren das gesamte Modul math:


import math

radius = 2
circle_area = math.pi * radius**2
print(circle_area)


# Variante 2:
# Da direkt pi aus math direkt importiert wird, können wir pi statt math.pi schreiben:

from math import pi

radius = 2
circle_area = pi * radius**2
print(circle_area)
