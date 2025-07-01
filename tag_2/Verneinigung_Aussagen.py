name = 'Thure'
mitglied = True
preis = 0

if not mitglied:
    preis = 3

if not 'h' in name and not 'H' in name:
    preis = preis*2

print(f'{name} zahlt {preis} €.')


name = 'Emmi'
mitglied = False
preis = 0

if not mitglied:
    preis = 3

if not 'h' in name and not 'H' in name:
    preis = preis*2

print(f'{name} zahlt {preis} €.')

name = 'Henrik'
mitglied = False
preis = 0

if not mitglied:
    preis = 3

if not 'h' in name and not 'H' in name:
    preis = preis*2

print(f'{name} zahlt {preis} €.')