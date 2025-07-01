# #Über Parameter können wir dafür sorgen, dass Funktionen nicht immer exakt das Gleiche tun, sondern, eben abhängig von den übergebenen Parametern, in ihren Ergebnissen variieren, obwohl die Rechenvorschriften gleich sind.

# Im Bild gesprochen: Ein Rezept besteht einerseits aus einer Liste von Zubereitungsschritten (Funktionskörper) aber auch aus einer Auflistung der Zutaten (Parameter). Nun kann man zwei verschiedene Kuchen mit demselben Rezept backen, indem man die Zutaten variiert. So macht es z.B. einen Unterschied, welche konkrete Apfelsorte man in einem Apfelkuchen verwendet.

# Definieren wir Parameter in einer Funktion, so müssen wir diese beim Funktionsaufruf in den Klammern angeben


def print_greeting(name, age): # (1)!
    print(f"Hallo {name}!") # (2)!
    if age > 65: # (3)!
        print(f"Geht es?") # (4)! 

print_greeting("Jörg", 68) # (5)!
print_greeting("Kevin", 20) # (6)!


# Bei der Funktionsdefinition werden alle Parameter, mit , dazwischen getrennt, in die runden Klammern geschrieben.
# Der erste übergebene Parameter wird hier in der Konsolenausgabe verwendet.
# Der zweite übergebene Parameter wird hier in der Bedingung benutzt.
# Auch diese zwei Mal eingerückte Zeile gehört noch zum Funktionsrumpf.
# Die Funktion wird hier aufgerufen. Die Argumente (so werden die Werte, die die Funktion als Parameter annimmt genannt) sind Jörg und 68, welche für die Paramter name und age eingesetzt werden.
# Die Funktion wird hier erneut aufgerufen, allerdings mit anderen Argumenten. Dies führt zu anderen Konsolenausgaben als bei der ersten Durchführung.

