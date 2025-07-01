# a) Erstelle ein Dictionary hobbies mit den Namen von drei Menschen als Schlüssel und ihren Hobbies als Werte.

# b) Füge dem Dictionary dann "Günther" mit dem Hobby "Musik" hinzu.

# c) Gebe auf der Konsole alle Namen und dazugehörigen Hobbies auf. Nutze dazu eine for-Schleife.

# d) Der folgende Code war dazu gedacht, alle Einträge in Dictionary zu löschen, bei denen der Key mit "G" beginnt.




#a.)

hobbies = {'Kira': 'Musik', 'Otto': 'Reisen', 'Hans': 'Schwimmen'}
print(hobbies)


#b.) 

hobbies ['Günther'] = 'Musik'


#c.)

print('Alle Einträge:')
for name, hobby in hobbies.items():
    print (f'{name}:{hobby}')



# d) Lösche alle Einträge, deren Key mit "G" beginnt.
# Da man ein Dictionary nicht direkt während der Iteration verändern sollte,
# erstellen wir eine Liste der Schlüssel, die gelöscht werden sollen.
keys_to_delete = [key for key in hobbies if key[0] == "G"]
for key in keys_to_delete:
    del hobbies[key]

# Ausgabe nach dem Löschen
print("\nNach dem Löschen der Einträge, die mit 'G' beginnen:")
for name, hobby in hobbies.items():
    print(f"{name}: {hobby}")
