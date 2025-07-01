# Im folgenden ist die Funktion rechteck_umfang gegeben.





# a) Welche der anschließenden Aufrufe führen zu einer Fehlermeldung? Führe sie nacheinander aus!


def rechteck_umfang(a, b):
    return 2 * (a + b)   


print(rechteck_umfang(1,2))

print(rechteck_umfang(7.0,2))


#Die ersten beiden Aufrufe der Funktion führen zu keinen Problemen. Die Funktion rechteck_umfang führt einfache Rechenoperationen aus, wodurch sowohl der Datentyp int als auch float kein Problem darstellt.
#Der dritte Aufruf führt zu folgender Fehlermeldung:
#TypeError: rechteck_umfang() missing 1 required positional argument: 'b'


print(rechteck_umfang(3))

#Dieser sagt uns, dass wir einen Parameter (in diesem Fall b) zu wenig belegt haben.
#Der vierte Aufruf führt zu folgender Fehlermeldung:
#TypeError: rechteck_umfang() takes 2 positional arguments but 3 were given


print(rechteck_umfang(3,4,5))

#Hier haben wir den gegenteiligen Fall: Wir haben einen Parameter zu viel belegt. Die 5, welche wir der Funktion übergeben, hat keinen zugehörigen Parameter




# b) Es wird eine kleine Änderung an der Funktion vorgenommen.

# Welche Aufrufe führen nun zu Fehlermeldungen? Finde eine Erklärung hierfür!

def rechteck_umfang(a, b=2):
    return 2 * (a + b)

print(rechteck_umfang(1, 2))

print(rechteck_umfang(7.0, 2))

print(rechteck_umfang(3))

print(rechteck_umfang(3, 4, 5))

# Hier bleibt fast alles gleich. Interessanter Weise führt nun der dritte Aufruf zu keiner Fehlermeldung, aber woran liegt das?
# Es liegt daran, dass bei der Funktionsdefinition b = 2 angegeben wurde. Das sagt der Funktion, dass wenn für diesen Parameter nichts übergeben wird, dann setze ihn auf 2.