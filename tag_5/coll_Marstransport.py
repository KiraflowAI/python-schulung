#Die folgende Funktion berechnet das Marsgewicht für eine einzelne Variable.
# gewicht = 65
# mars_faktor = 0.38
# mars_gewicht = gewicht * mars_faktor
# print(f'Dein Marsgewicht:{mars_gewicht}')

#a) Passe das Programm so an, dass für eine Liste gewichte = 
# [100, 65, 23] die Berechnung durchgeführt wird und auf der Konsole erscheint:
#
# #Dein Marsgewicht: 38.0
# Dein Marsgewicht: 24.7
# Dein Marsgewicht: 8.74

# gewichte = [100, 65, 23]
# mars_faktor = 0.38
# for gewicht in gewichte:
#     mars_gewicht = gewicht * mars_faktor
#     print(f'Dein Marskgewicht: {mars_gewicht}')



#b) Erweitere das Programm, sodass zusätzlich alle Marsgewichte in einer Liste gespeichert und am Ende ausgegeben werden.
# Dein Marsgewicht: 38.0
# Dein Marsgewicht: 24.7
# Dein Marsgewicht: 8.74
# Marsgewichte: [38.9, 24.7, 8.74]

# gewichte = [100, 65, 23]
# mars_gewichte = [] # diese klasse ist leer, erst mal 
# mars_faktor = 0.38
# for gewicht in gewichte:
#     mars_gewicht = gewicht * mars_faktor 
#     mars_gewichte.append(mars_gewicht) # die leere klasse wird erweitert mars_gewicht
#     print(f'Dein Marsgewicht:{mars_gewicht}')
# print(f'Marsgewicht: {mars_gewichte}')


#c) Bonus: Schreibe den Code mit einer List-Comprehension. (Wenn du das noch nicht kennst, wirst du es später kennenlernen und kannst dann zu dieser Aufgabe zurückkehren.)


gewichte = [100, 65, 23]
mars_faktor = 0.38
mars_gewichte = [gewicht * mars_faktor for gewicht in gewichte]

for mars_gewicht in mars_gewichte:
    print(f'Dein Marsgewicht:{mars_gewicht}')
print(f'Marsgewichte: {mars_gewichte}')