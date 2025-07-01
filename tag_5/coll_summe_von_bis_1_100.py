#Erstelle Code, der die Zahlen von 1 bis 100 summiert.

# Tue dies in verschiedenen Varianten:

# a) Verwende while.

# b) Verwende for und range.

# c) Erstelle nun ein Programm mit der man die Zahlen 1, 2, 3, ... usw. so lange addiert, 
# bis die Summe größer als 100 ist.





#a.)  # solange dieser counter kleiner oder gleich 100 wollen wir zu dieser summe den inhalt des counters dazu addieren und danach um eins addieren

counter = 1                              # counter starter bei 1
sum = 0                                  # hier wird der wert gespeichert
while counter <= 100:                    # solange dieser counter kleiner oder gleich ist 
    sum += counter                       # addieren wir zu dieser summe den inhalt des counters
    counter += 1                         # und erhöhen die summe des counters um 1
print(sum)

#b.) b) Verwende for und range.

sum = 0                                  
for i in range(101):                
    sum += i
print(sum)

#c.) c) Erstelle nun ein Programm mit der man die Zahlen 1, 2, 3, ... usw. so lange addiert, bis die Summe größer als 100 ist.

#while
counter = 1                             # 
sum = 0
while sum <= 100:
    sum += counter
    counter += 1
print(sum)

#for
summe = 0
for counter in range(1, 101):
    if summe > 100:
        break
    summe += counter
print(summe)

