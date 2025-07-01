print('Hallo Welt')
#Variablen
#a=1
#print(a)
#a=3
#print(a)
#print(a)
#a=10
#b=15
#print(a+b)
#print(a)

#a=4
#a=2+a
#print(a)

#gesamtumsatz = 100000
#anzahlmitarbeiter = 0.000001
#print(gesamtumsatz / anzahlmitarbeiter)

alter = 30 # Integer : Ganzzahlen -3, -2, -0
print(type(alter))

größe = 1.6 #float Fließkommazahlen
print(type(größe))

# Rechner
# Arbeitsspeicher
# Jede Zahl hat eine bestimmte Platzmenge z.b. 64 bits
# 5 --> 0101
# 6 --> 0110
# 7 --> 0111
# 8 --> 1000

# Jede Fließkommazahl muss in 64 einsen und nullen darstellbar sein

name = 'Viktor'
print(name)
wohnort = 'Kiel'
alter = 37
print(type(name))
print(type(wohnort))
print(type(alter))

print('Hallo ich bin' + name)
print(f'Hallo, ich bin {name}. Ich bin {alter} Jahre alt. Ich wohne in {wohnort}.') 
      #formated String

name = input('Wie heißt du?')
print(f'Hallo {name}')

zahl = int(input('Welche Zahl soll ich verdoppeln?'))
print(type(zahl))
print(zahl * 2)