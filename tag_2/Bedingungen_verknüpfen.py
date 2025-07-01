# Operator	Beschreibung	Beispiel
# and	Gib True zurück, wenn alle Parameter True sind.	x < 5 and y > 10
# or	Gibt True zurück, wenn eines der Parameter True ist.	x < 5 or y > 10
# not	Invertiert die Eingabe. Aus True wird False und umgekehrt.	not x >= 6

alter = 65
vereinsmitglied = False
preis = 6

if alter > 55 or alter <5:
    preis = preis / 2
if vereinsmitglied:
    preis = 0
print(f'Ihr Preis ist {preis}')

#Wenn die Person älter als 55 Jahre oder jünger als 5 Jahre ist, wird der Preis halbiert.
# Wenn die Person Vereinsmitglied ist (also wenn die Variable vereinsmitglied auf True gesetzt ist), wird der Preis auf 0 gesetzt, unabhängig vom Alter.
# Wenn vereinsmitglied auf False gesetzt wird, hat dies zur Folge, dass die zweite Bedingung if vereinsmitglied: nicht erfüllt wird. Das bedeutet, dass die Person keinen kostenlosen Eintritt erhält.

