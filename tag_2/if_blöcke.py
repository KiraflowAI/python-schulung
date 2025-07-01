#name = 'Kiran'
#if 'c' and 'u' in name:
#    print('Wow, das ist ein seltener Name!')
#print(f'Auf jeden Fall ist dein Name: {name}')

#Mit dem if Keyword und Einrückungen kann man festlegen, dass Code nur unter bestimmten Bedingungen ausgeführt wird.
# Wenn die Bedingung, die neben dem if steht, wahr ist, dann werden die nächsten Zeilen Code, die eingerückt sind, ausgeführt. Wenn die Bedingung aber falsch ist, werden die eingerückten Zeilen einfach übersprungen.

#preis = 3.50
#alter = 6

#if alter >= 65:
#    preis = preis-2

#if alter < 7:
#    preis = 0.0

#print(f'Mit {alter} Jahren zahlst du: {preis} €.')

alter = int(input('Wie alt bist du'))
if alter < 0:
    alter = 0
print(f'Du bist {alter} Jahre alt.')


