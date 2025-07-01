# Schreibe ein Programm, das den Nutzer nach einer Zahl fragt. 
# Das Programm kann intern in einer Variablen namens summe die Summe 
# aller bisher abgefragten Zahlen bilden und ausgeben.
# Die Konsolenausgabe soll also in etwa so aussehen:

# Bisherige Summe: 0
# Gib eine Zahl ein: 3
# Bisherige Summe: 3
# Gib eine Zahl ein: 10
# Bisherige Summe: 13
# Gib eine Zahl ein: -20
# Bisherige Summe: -7
# Gib eine Zahl ein: 


#Tipps ohne Code:

# Lege dir zunächst eine Variable summe an, in der du die Summanden zusammenzählen wirst. Was ist ein sinnvoller Startwert?
# Um eine Schleife dauerhaft für immer zu durchlaufen kann als Bedingung True genutzt werden.
# Mit int(input("Gib eine Zahl ein: ")) kann man den Nutzer um eine Zahl bitten.
# Addiere die Eingabe zu summe und speichere diese.

summe = 0
while True:
    print(f'Bisherige Summe: {summe}')
    eingabe = int(input('Gib eine Zahl ein:'))
    summe = summe + eingabe 