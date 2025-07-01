alter = 67
mitglied = True
preis = 10

if alter < 18 or alter >= 65:
    preis = 5
if mitglied:
    preis = preis / 2
print(f'Der Preis beträgt {preis} €.')