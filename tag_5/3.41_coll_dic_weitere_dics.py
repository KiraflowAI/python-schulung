# Dictionaries haben noch weitere nützliche Methoden. Vervollständige bitte die Tabelle und gebe zu jede der Methoden ein Beispiel.

# Funktion	            Beschreibung
# my_dict[key]	        Greif auf den Wert mit dem Key key zu. Existiert dieser nicht wird er beim Schreiben erstellt. Beim Lesen gibt es einen Fehler
# get(key, default=None)	Gibt den Wert für den angegebenen Schlüssel zurück. Gibt default zurück, wenn der Schlüssel nicht existiert.
# keys()	
# values()	
# items()	
# update(dict2)	
# pop(key)	
# clear()	
# copy()	




                        # Funktion	                  Beschreibung
                        # my_dict[key]	            Greift auf den Wert mit dem Key key zu. Existiert dieser nicht, gibt es beim Lesen einen Fehler. Beim Schreiben wird er erstellt.
                        # get(key, default=None)  	Gibt den Wert für den angegebenen Schlüssel zurück. Gibt default, falls nicht vorhanden.
                        # keys()	                    Gibt eine Ansicht aller Schlüssel im Dictionary zurück.
                        # values()	                Gibt eine Ansicht aller Werte im Dictionary zurück.
                        # items()                 	Gibt eine Ansicht aller Schlüssel-Wert-Paare zurück.
                        # update(dict2)	            Fügt die Schlüssel-Wert-Paare aus dict2 in das Dictionary ein oder überschreibt vorhandene Werte.
                        # pop(key)	                Entfernt den Schlüssel key und gibt dessen Wert zurück. Gibt einen Fehler, falls key nicht existiert.
                        # clear()                 	Entfernt alle Elemente aus dem Dictionary.
                        # copy()                   	Erstellt eine flache Kopie des Dictionaries.




# Beispiel-Dictionary
my_dict = {"name": "Alice", "alter": 25, "stadt": "Berlin"}

# `my_dict[key]`
# Zugriff auf den Wert mit dem Schlüssel "name"
print(my_dict["name"])  # Ausgabe: Alice
# Schreiben eines neuen Werts für "alter"
my_dict["alter"] = 26
print(my_dict)  # Ausgabe: {'name': 'Alice', 'alter': 26, 'stadt': 'Berlin'}

# `get(key, default=None)`
print(my_dict.get("stadt"))  # Ausgabe: Berlin
print(my_dict.get("land", "Deutschland"))  # Ausgabe: Deutschland (da "land" nicht existiert)

# `keys()`
print(my_dict.keys())  # Ausgabe: dict_keys(['name', 'alter', 'stadt'])

# `values()`
print(my_dict.values())  # Ausgabe: dict_values(['Alice', 26, 'Berlin'])

# `items()`
print(my_dict.items())  # Ausgabe: dict_items([('name', 'Alice'), ('alter', 26), ('stadt', 'Berlin')])

# `update(dict2)`
my_dict.update({"land": "Deutschland", "beruf": "Ingenieur"})
print(my_dict)  # Ausgabe: {'name': 'Alice', 'alter': 26, 'stadt': 'Berlin', 'land': 'Deutschland', 'beruf': 'Ingenieur'}

# `pop(key)`
alter = my_dict.pop("alter")
print(alter)  # Ausgabe: 26
print(my_dict)  # Ausgabe: {'name': 'Alice', 'stadt': 'Berlin', 'land': 'Deutschland', 'beruf': 'Ingenieur'}

# `clear()`
my_dict.clear()
print(my_dict)  # Ausgabe: {}

# `copy()`
original = {"tier": "Hund", "farbe": "Braun"}
kopie = original.copy()
print(kopie)  # Ausgabe: {'tier': 'Hund', 'farbe': 'Braun'}

