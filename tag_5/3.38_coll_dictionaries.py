#Dictionaries (Schlüssel-Wert-Paare):
#Dictionaries sind ein Datentyp in Python, mit dem wir 
# Schlüssel-Wert-Paar beschreiben können. 
# Sie ermöglichen uns, Werte mithilfe von 
# Schlüsseln zu speichern und abzurufen, 
# ähnlich wie ein echtes Wörterbuch es erlaubt, 
# die Bedeutung eines Wortes zu finden. Wir 
# erinnern uns an Listen oder Tupels, bei denen wir auf die Elemente durch ihre Position in der Sammlung, also deren Index, auf die Elemente zugreifen können.


                                # mein_dict = {"Name": "Max", "Alter": 25, "Stadt": "Berlin"} # (1)
                                # print(mein_dict)

#Das Dictionary wird mit geschweiften Klammern {...} erstellt. Schlüssel und Werte werden über ein Doppelpunkt : voneinander getrennt und die verschiedenen Schlüssel-Wert-Paare über Komma ,.


#Eigenschaften von Dictionaries
# Schlüssel und Werte: Jeder Eintrag in einem Dictionary besteht aus einem Schlüssel und einem zugehörigen Wert.

# Einzigartige Schlüssel: Jeder Schlüssel in einem Dictionary muss einzigartig sein. Sollen mehrere Elemente in einem Schlüssel gespeichert werden, kann man natürlich auch eine Liste für diesen Schlüssel speichern.

# Veränderbar: Dictionaries sind veränderbar, was bedeutet, dass Einträge hinzugefügt, entfernt oder geändert werden können.

# Ungeordnet: Die Elemente in einem Dictionary sind nicht in einer bestimmten Reihenfolge gespeichert. Man greift auf die Elemente über deren Schlüssel zu.

# Dynamisch: Die Größe eines Dictionaries kann sich während der Laufzeit des Programms ändern.



# #Operationen mit Dictionaries
# Erstellen und Initialisieren eines Dictionaries
# Es gibt verschiedene Varianten zur Erstellung von Dictionaries:



a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict([('two', 2), ('one', 1), ('three', 3)])
d = dict({'three': 3, 'one': 1, 'two': 2})
e = dict({'one': 1, 'three': 3}, two=2)

print(a == b == c == d == e)

# true


#Zugriff auf Werte
# Der Zugriff auf die Werte erfolgt über den entsprechenden Schlüssel in eckigen Klammern. Das sieht ähnlich aus wie bei Listen, nur dass wir keinen Index verwenden, sondern den entsprechenden Schlüssel.



mein_dict = {"Name": "Max", "Alter": 25, "Stadt": "Berlin"}
print(mein_dict["Name"]) # MAX


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
    print("No Value found") ### Found value: 1 & No value found


#Eine weiterer entscheidender Vorteil bei der Verwendung von get, ist dass keine Fehlermeldung entsteht, wenn versucht wird auf ein Key zuzugreifen, der nicht existiert.



                        # my_dict = dict(one=1, two=2, three=3)

                        # my_dict["four"] # führt zu einem KeyError!




# Hinzufügen und Ändern von Einträgen
# Werte können hinzugefügt werden, in dem wir einem Element, einen Schlüssel hinzufügen und diesem einen Wert zuweisen. Existiert der Schlüssel bereits wird der vorhandene Wert einfach überschrieben.

# Als Schlüssel können dabei nur Objekte genutzt werden, die hashable sind (also z.B. Zahlen, Strings, Tupel)


mein_dict = {"Name": "Max", "Alter": 25, "Stadt": "Berlin"}
# Hinzufügen eines neuen Eintrags
mein_dict["Beruf"] = "Ingenieur"

# Ändern eines vorhandenen Eintrags
mein_dict["Alter"] = 26

print(mein_dict)



#Entfernen von Einträgen
#Das Entfernen von Einträgen sieht leider nicht wie typischer Python-Code aus. Man greift auf das Element, welches man löschen will wie gewohnt zu und löscht das Element mit einem vorangestellten del.


mein_dict = {"Name": "Max", "Alter": 25, "Stadt": "Berlin"}

del mein_dict["Stadt"]

print(mein_dict)


#Durchlaufen eines Dictionaries
#Um die Keys und Values eines Dictionaries zu durchlaufen, muss die Methode items() verwendet werden. Hier erhalten wir dann zwei Werte in unserer for-Schleife auf ein Mal:


mein_dict = {"Name": "Max", "Alter": 25, "Stadt": "Berlin"}

for key, value in mein_dict.items():
    print(key, value)

print("fertig")


# #Out [5]:
# Name Max
# Alter 25
# Stadt Berlin
# fertig


#Vergleich Listen und Dictionary
#Optisch sind sich Listen und Dictionaries in Python sehr ähnlich. Bei beiden erfolgt der Zugriff auf die Elemente über eckige Klammern ([]).


                        # my_list = [5, 8, 5, 1, 0,80]

                        # print(my_list[0]) 

                        # my_list[0] = 10



#DICTIONARY
my_dict = {
    'Hunde': 5,
    'Katzen': 8,
    'Hühner': 5,
    'Hähne': 1,
    'Schweine': 0,
    'Kühe': 80
}

print(my_dict['Hunde']) 

my_dict['Hunde'] = 6