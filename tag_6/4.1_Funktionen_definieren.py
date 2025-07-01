# Bisher sind alle unsere Codebeispiele so geschrieben, dass der jeweilige Code einmalig ausgeführt und dann nicht mehr gebraucht wird. Das ist normalerweise nicht der Fall. Normalerweise werden Codeabschnitte immer wieder und in verschiedenen Kontexten aufgerufen. Zum Beispiel wollen wir Code bereitstellen, um den BMI einer Person zu berechnen. Den Code möchte man einerseits für beliebige Personen ausführen und andererseits an verschiedenen Stellen (z.B. bei verschiedenen Anzeigen in einer App).

# Die wichtigste Möglichkeit zur Strukturierung des Codes sind Funktionen bzw. Methoden.

# In Python ist eine Funktion eine selbstständige, wiederverwendbare Codeeinheit, die dazu dient, eine bestimmte Aufgabe zu erledigen. Funktionen können Parameter akzeptieren, Operationen durchführen und Rückgabewerte liefern.

# Beliebte Metaphern, um Funktionen vorzustellen sind:

# Eine Funktion ist eine Maschine, in die wir Rohstoffe stopfen, damit sie diese verarbeitet und uns ein Produkt liefert.
# Eine Funktion ist wie ein Rezept. Es erwartet bestimmte Zutaten und wenn wir der Anleitung folgen, erhalten wir eine raffinierte Mahlzeit.



def hoch(): # (1)!
    print("Er lebe...") # (2)!
    print("HOCH!")

hoch() # (3)!
hoch() # (4)!
hoch() # (5)!



# Die Funktion wird mit dem Schlüsselwort def definiert. Wir geben ihr den Namen hoch. Da sie keine Parameter hat, schreiben wir hier einfach runde Klammern () ohne etwas dazwischen, und danach einen : (so wie beim if).
# Diese Erste Zeile einer Funktion wird Funktionskopf genannt.
# Die nun eingerückten Zeilen sind der Funktionsrumpf oder Funktionskörper. Diese werden nur durchgeführt, wenn die Funktion aufgerufen wird.
# Wir führen in dieser Zeile die Funktion aus. Dazu schreiben wir den Funktionsnamen auf, gefolgt von runden Klammern.
# Wir führen die Funktion erneut aus...
# Und noch ein drittes Mal🥳