#Dictionaries sind ein Datentyp in Python, mit dem wir Schlüssel-Wert-Paar beschreiben können. S
#Sie ermöglichen uns, Werte mithilfe von Schlüsseln zu speichern und abzurufen, ähnlich wie ein echtes Wörterbuch 
# es erlaubt, die Bedeutung eines Wortes zu finden. Wir erinnern uns an Listen oder Tupels, bei denen wir auf die Elemente durch ihre Position in der Sammlung, a
# lso deren Index, auf die Elemente zugreifen können.

#Das Dictionary wird mit geschweiften Klammern {...} erstellt. Schlüssel und Werte werden über ein Doppelpunkt : voneinander getrennt und die verschiedenen Schlüssel-Wert-Paare über Komma ,.


# Eigenschaften von Dictionaries
# Schlüssel und Werte: Jeder Eintrag in einem Dictionary besteht aus einem Schlüssel und einem zugehörigen Wert.

# Einzigartige Schlüssel: Jeder Schlüssel in einem Dictionary muss einzigartig sein. Sollen mehrere Elemente in einem Schlüssel gespeichert werden, kann man natürlich auch eine Liste für diesen Schlüssel speichern.

# Veränderbar: Dictionaries sind veränderbar, was bedeutet, dass Einträge hinzugefügt, entfernt oder geändert werden können.

# Ungeordnet: Die Elemente in einem Dictionary sind nicht in einer bestimmten Reihenfolge gespeichert. Man greift auf die Elemente über deren Schlüssel zu.

# Dynamisch: Die Größe eines Dictionaries kann sich während der Laufzeit des Programms ändern.

mein_dict = {"Name": "Max", "Alter": 25, "Stadt": "Berlin"} # (1)
print(mein_dict)


# #Operationen mit Dictionaries
# Erstellen und Initialisieren eines Dictionaries
# Es gibt verschiedene Varianten zur Erstellung von Dictionaries:

a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict([('two', 2), ('one', 1), ('three', 3)])
d = dict({'three': 3, 'one': 1, 'two': 2})
e = dict({'one': 1, 'three': 3}, two=2)

print(a == b == c == d == e)


#Zugriff auf Werte
#Der Zugriff auf die Werte erfolgt über den entsprechenden Schlüssel in eckigen Klammern. Das sieht ähnlich aus wie bei Listen, nur dass wir keinen Index verwenden, sondern den entsprechenden Schlüssel.

mein_dict = {"Name": "Max", "Alter": 25, "Stadt": "Berlin"}
print(mein_dict["Name"])


#Eine weitere Möglichkeit auf die Values eines Dictionaries zuzugreifen besteht in der Methode get(). Das besondere: Wenn der Key nicht existiert, wird None zurückgegeben. Das ist in if-Bedingungen nützlich, bei denen ich Code nur durchführen möchte, wenn der Schlüssel auch tatsächlich existiert. Denn bool(None) ist immer False.

my_dict = dict(one=1, two=2, three=3)

v1 = my_dict.get("one")

if v1:
    print(f"Found value: {v1}")
else:
    print("No Value found")

v2 = my_dict.get("four")

if v2:
    print(f"Found value: {v2}")
else:
    print("No Value found")

