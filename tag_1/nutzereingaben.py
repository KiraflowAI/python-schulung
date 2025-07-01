#print('Sei gegrüßt!')
#vorname = input('Wie heißt du?')
#print('Hallo')
#print(vorname) 

#Mit der print Funktion können wir auf der Konsole eine Ausgabe erzeugen.
# Andererseits kann mit der Funktion 
# input eine Eingabe des Nutzers auf 
# der Konsole erwartet werden. Wenn die 
# Funktion aufgerufen wird, wartet der Code so lange, 
# bis eine Nutzereingabe getätigt und 
# mit ++enter++ bestätigt wurde. 
# Die Eingabe des Nutzers wird dann in einer 
# Variablen gespeichert.


#Immer, wenn man Zahlen vom Nutzer einlesen will und mit diesem im Code rechnen möchte, so muss man Python ganz explizit sagen, dass hier eine Zahl folgt. Verwenden sie daher folgenden Code:
# Bei Ganzzahlen nutze int(input(...)):

#alter = int(input('Wie alt bist du?'))
#print ('In einem Jahr bist du:')
#print (alter+1)

#Bei Fließkommazahlen nutze float(input(...)):

#preis = float(input('Wie viel kostet das Produkt?'))
#print ('Die Mehrwertsteuer des Produktes beträgt:')
#print(preis*0.19)

#Ersetze die ... im folgenden Code so, dass in einer Variable vorname der Name des Nutzers gespeichert wird. 
# Danach soll in der Variable alter das Alter des Nutzers gespeichert werden

#vorname = input('Wie heißt du?')
#alter = input('Wie alt bist du?')

#gewicht = 65
#mars_faktor = 0.38
#mars_gewicht = gewicht * mars_faktor
#print(f'Dein Marsgewicht:{mars_gewicht}')

gewicht = int(input('Was wiegst du?'))
mars_faktor = 0.37
mars_gewicht = gewicht * mars_faktor
print(f'Dein Marsgewicht:{mars_gewicht}')

