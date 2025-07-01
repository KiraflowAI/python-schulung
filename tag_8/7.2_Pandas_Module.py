#Es gibt einige Gründe warum Python eine eher einfache Programmiersprache ist.
#Ein Grund hierfür ist, dass Python eine große Ansammlung an vorgefertigten Code in sogenannten Modulen zur Verfügung stellt. Dieser kann sowohl einzelne Variablen, als auch Funktionen und Klassen enthalten.


#Module werden durch den import Befehl importiert. Ein bereits in Python implementiertes Modul ist bspw. math, welches viele mathematische Konstanten und Funktionen enthält.


import math

# pi
print(math.pi)

# Abrunden
print(math.floor(3.7))

from math import pi, floor

# pi
print(pi)

# Abrunden
print(floor(3.7))

from math import pi, floor

# pi
print(pi)

# Abrunden
print(floor(3.7))

#Auf diese Weise sind pi und floor direkt importiert und auch als die selben Variablen und Funktionen gespeichert worden.

# Alle anderen Konstanten, Funktionen, etc aus math wurden hierbei nicht importiert.