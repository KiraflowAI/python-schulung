#alter = 17

#if alter >= 18:
#    preis = 6.5
#else:
#    preis = 3.9
#print(f'Der Preis ist {preis}')

# Diese Schreibweise lässt sich auch kürzen

#alter = 20
#preis = 6.5 if alter>= 18 else 3.9
#print(f'Der Preis ist {preis}')

alter = 1
if alter >= 18:
    preis = 6.5
elif alter >= 5:
    preis = 3.90
else:
    preis = 0.0

print(f'Der Preis ist {preis}')

#kürzere Schreibweise:

alter = 3

preis = 6.50 if alter >= 18 else 3.90 if alter >= 5 else 0

print(f'Der Preis für dich ist {preis}')