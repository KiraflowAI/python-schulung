#Erstelle eine Funktion quadrat(n), welches ein Quadrat aus Sternen zeichnet. Hier ein paar Beispiele:

#Beispiel 1:
   #   quadrat(5)


        # #*****
        # *****
        # *****
        # *****
        # *****




def quadrat (n, symbol = '*'):
    for i in range(n):   # schleife für jede einzelne zeile // wie oft gehen wir durch die zeile (i)
        for j in range(n): # pro zeile eine schleife für die jeweilige kette // wie hoch ist die anzahl der symbole (j)
            print(symbol,end='')
        print()
quadrat(5)
#quadrat(5, '#')




def quadrat(n, symbol='*'):
    print(n * (n * symbol + "\n")) # hier wird es in absatz angezeigt













































# Hier lohnt sich mit verschachtelten Schleifen zu arbeiten.

# Um einen Absatz in einem String zu machen, kann das Zeichen \n verwendet werden. Dies könnte für deine Lösung relevant sein.

# Die Funktion print() besitzt einen Parameter end='\n'. Dieser sorgt dafür, dass am Ende des print Befehls ein Zeilenumbruch in der Konsole gemacht wird. Diesen können wir überschreiben:

# print("Hallo", end="+")
# print("Du")

# #Ausgabe: Hallo+Du
