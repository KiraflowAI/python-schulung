# #Aufgabe 1:

# Im Folgenden wird die Klasse Apple erstellt und einige Instanzen dieser erzeugt. Schaue dir den Code an und versuch vorauszusagen was dieser ausgeben wird.

# PYTHON

class Apple():
    pass

apple_1 = Apple()
apple_2 = Apple()
apple_3 = apple_2

print(type(apple_1))
print(apple_1 == apple_2)
print(apple_3 == apple_2)



# self und __init__ braucht man nur, wenn du der Klasse eigene Eigenschaften (Attribute) oder Funktionen (Methoden) geben willst.

# Aufgabe 1:

# Die Ausgabe von type(apple_1) ist der Datentyp. Dadurch, dass apple_1 eine Instanz der Klasse Apple ist, bekommen wir auch genau das als Ausgabe. __main__ ist bei uns mit ausgegeben worden, da die Klasse Apple in unserem aktuellen Code definiert und nicht importiert wurde.
# Die Ausgabe von apple_1 == apple_2 ist False, da dies zwei unterschiedliche Referenzen auf die Instanzen der Klasse Apple sind.
# Die Ausgabe von apple_3 == apple_2 ist True, da apple_3 der selben Referenz von apple_2 zugewiesen wurde und somit auf die selbe Instanz zeigen.




# Aufgabe 2:
# Die Klasse Cherry muss wieder mit dem Ausdruck pass erstellt werden. Die Anschließenden Instanzen werden als Referenzen zugewiesen. Deren Benennung ist hierbei beliebig.

# Klasse: Cherry
class Cherry():
  pass

# 2 Instanzen
cherry_1 = Cherry()
cherry_2 = Cherry()
