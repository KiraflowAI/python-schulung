#Methode	Beschreibung
# append	hinzufügen von einem Eintrag am Ende der Liste
# clear	entfernt alle Elemente aus der Liste
# copy	erstellt eine flache Kopie der Liste
# count	zählt, wie oft ein bestimmter Wert in der Liste vorkommt
# extend	erweitert die Liste durch das Anhängen aller Elemente eines Iterables
# index	gibt den Index des ersten Vorkommens eines bestimmten Wertes zurück
# insert	fügt einen Eintrag an einer spezifizierten Position in der Liste ein
# pop	entfernt und gibt das Element an einem bestimmten Index zurück (standardmäßig das letzte)
# remove	entfernt das erste Vorkommen eines bestimmten Wertes aus der Liste
# sort	sortiert die Elemente der Liste in aufsteigender Reihenfolge

# Beispiel:

liste = [3, 1, 4, 1, 5, 9, 2, 6]

#append: fügt einen Eintrag am Ende hinzu
liste.append(7)
print('append:',liste)

#clear: entfernt alle Elemente
kopie =liste.copy()
kopie.clear()
print('clear:', kopie)

# copy: erstellt eine flache copy
kopie = liste.copy()
print('copy:', kopie)

# count: zählt, wie oft der Wert 1 vorkommt
anzahl = liste.count(1)
print('count:', anzahl)

# extend: erweitert die Liste um mehrere Elemente
liste.extend ([8,9])
print('extend:', liste)

# index: findet den index des ersten vorkommens von 5
index_von_5 = liste.index(5)
print('index:', index_von_5)

# insert: fügt 0 an Position 0 ein
liste.insert(0, 0)
print('insert:', liste)

# pop: entfernt das letzte Element 
letzte = liste.pop()
print('remove:', letzte, liste)

# remove: entfernt das erste Vorkommen von 1
liste.remove(1)
print('remove:', liste)

# sort: sortiert die Liste
liste.sort()
print('sort:', liste)
