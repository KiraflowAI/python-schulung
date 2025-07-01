#Ziel ist es den Code so zu erweitern, dass immer abwechselnd 
# die Namen der beiden Spieler ausgegeben werden.
# Erwartete Ausgabe

# jetziger_spieler = 'Hans'
# nächster_spieler = 'Clara'

# while True:
#     zwischenspeicher = jetziger_spieler
#     jetziger_spieler = nächster_spieler
#     nächster_spieler = zwischenspeicher 
#     print(jetziger_spieler)


jetziger_spieler = "Hans"
nächster_spieler = "Clara"
 
while True:

    zwischenspeicher = jetziger_spieler
    jetziger_spieler = nächster_spieler
    nächster_spieler = zwischenspeicher
    
    print(jetziger_spieler)


