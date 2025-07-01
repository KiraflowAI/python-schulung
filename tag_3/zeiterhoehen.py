stunden = int(input('Stunden:'))
minuten = int(input('Minuten:'))
sekunden = int(input('Sekunden'))

sekunden += 1

if sekunden == 60:
    sekunden = 0
    minuten += 1
    if minuten == 60:
        minuten = 0
        stunden += 1
        if stunden == 24:
            stunden = 0 

stunden = str(stunden).zfill (2)
minuten = str(minuten).zfill (2) 
sekunden = str(sekunden).zfill (2)

print(f'Neue Zeit: {stunden}:{minuten}:{sekunden}')
