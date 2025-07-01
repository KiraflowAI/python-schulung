#Gegeben sei der folgende Code. Sage voraus, was auf der Konsole erscheinen wird, wenn


# summanden = [1,2,3,4]
#summanden = [3, -3, 4, -2]
#summanden = [1]
#summanden = []

summanden = [1,2,3,4]
summe = 0
for s in summanden:
    summe = summe + s
print(f'Die Summe von {summanden} ist {summe}')

summanden = [3, -3, 4, -2]
summe = 0
for s in summanden:
    summe = summe + s
print(f'Die Summe von {summanden} ist {summe}')

summanden = [1]
summe = 0
for s in summanden:
    summe = summe + s
print(f'Die Summe von {summanden} ist {summe}')

summanden = []
summe = 0
for s in summanden:
    summe = summe + s
print(f'Die Summe von {summanden} ist {summe}')