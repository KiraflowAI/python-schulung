#Nun ist noch wichtig zu erwähnen, dass Funktionen nicht nur verarbeiten, sondern auch ein Ergebnis am Ende ihrer Durchführung zurückgeben können. Der Wert, der zurückgegeben werden soll, steht in einer Zeile mit einem vorangehenden return.

def quadrat(zahl): # (1)
    return zahl * zahl # (2)

x = 4 # (3)
q = quadrat(x) # (4)

print(f"{x}² = {q}") # (5)

#ausgabe: 4² = 16


# # Markdown
# Beim Funktionskopf sagen wir, dass es einen Paramter gibt. Dass es eine Rückgabe geben wird, lässt sich hier nicht erkennen.
# Der Parameter zahl wird mit sich selbst multipliziert und das Ergebnis dann zurückgegeben, da ein return am Anfang der eingerückten Zeile steht. Wichtig: Sobald in einer Funktion die Zeile mit return ausgeführt wurde, endet automatisch die Funktion, egal ob der Funktionskörper danach noch weiter geht oder nicht.
# Wir speichern in der Variablen x das Argument.
# Wir übergeben x an die Funktion und speichern die Rückgabe in der Variablen q.
# Wir geben die Ergebnisse fein säuberlich auf der Konsole aus.