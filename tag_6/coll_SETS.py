#SETS (MENGEN): 
#Ein Set ist eine Datenstruktur, die für die Speicherung einer ungeordneten Sammlung von einzigartigen Elementen verwendet wird. Das heißt, dass sich die Elemente in einem Set nicht wiederholen.

# Sets bieten folgende Eigenschaften:

# Ungeordnet: Sets haben keine feste Reihenfolge der Elemente.

# Einzigartige Elemente: Jedes Element in einem Set ist einzigartig. Duplikate werden ignoriert und tauchen im Set nur einmal auf.

# Unveränderliche Elemente: Sets können nur unveränderliche (immutable) Datentypen als Elemente enthalten, wie Zahlen, Strings und Tupel. Das heißt, Listen und Dictionaries können zum Beispiel nicht in Sets gespeichert werden.

# Veränderlich: Sets selbst sind veränderlich, das heißt man kann Elemente hinzufügen und entfernen.

# Kein Indexzugriff: Aufgrund der Ungeordnetheit der Elemente gibt es keinen direkten Indexzugriff. Die Mitgliedschaft eines Elements wird mit Methoden wie in überprüft.

# Sets werden mit geschweiften Klammern {} oder der set()-Funktion erstellt.

einzigartige_zahlen = {1, 2, 3, 2, 1} 
buchstaben = {'a', 'a', 'b', 'b'}

text = "Python ist cool. Mathe ist auch cool."
unique_words = set(text.split())

for word in unique_words:
    print(word)

