# #Mit List Comprehension wird eine Schreibweise in Python benannt, mit der geänderte Kopien von Listen schnell und leserlich erstellt werden können. Sie bedarf (vor allem bei Erfahrungen mit andereren Programmiersprachen) etwas Eingewöhnung, ist aber sehr beliebt in Python und liefert sogar Laufzeitvorteile.

# Man sollte es mit dieser Technik aber auch nicht übertreiben, da irgendwann die Leserlichkeit leidet.




#Betrachten wir den folgeden Code, der alle Element einer Liste verdreifacht und das Ergebnis in einer neuen Liste speichert:

numbers = [1, 2, 3, 4]

triple_numbers = []
for number in numbers:
    triple_numbers.append(number * 3)

print(triple_numbers)

# kurzschreibweise mit list comporehension

numbers = [1, 2, 3, 4]

triple_numbers = [number * 3 for number in numbers]

print(triple_numbers)

#Um die Struktur der List Comprehension besser zu erkennen lohnt es sich diese auszusprechen:

# Ich lege eine Liste an (erkennt man an den eckigen Klammern [...]), in der ich jede number mit 3 multipliziere, wobei (for) die number aus numbers kommt.


#Hier noch ein zweites Beispiel, welches die entsprechenden Teile im Code farblich hervorhebt:

# Without List Comprehension
quadrate = []
for i in [1, 2, 3, 4, 5]:
    quadrate.append(i * i)

# List Comprehension
quadrate = [i * i for i in [1, 2, 3, 4, 5]]



#Es ist bei einer List Comprehension einfach möglich bestimmte Elemente aus der Liste unter einer Bedingung zu entfernen.

# Ohne List Comprehension

words = ["Python", "ist", "cool"]

result = []
for word in words:
    if len(word) > 3:
        result.append(word)

print(result)

#list comprehension

words = ['python', 'ist', 'cool']
result = [word for word in words if len(word) > 3]
print(result)

#bedingte einsetzung:
# Im letzten Beispiel haben wir gesehen, wie wir Elemente filtern können. Manchmal möchte man aber auch verschiedene Operationen, basierend auf einer Bedingung, auf einem Element durchführen. Hier lässt sich der ternäre Operater nutzen.
# Hinweis zum folgenden Beispiel: Mit der Operation i % 2 wird ausgerechnet, ob eine Zahl i bei der Division mit 2 den Rest 1 oder 0 hat. Damit kann man dann bestimmen, ob eine Zahl gerade (Rest 0) oder ungerade (Rest 1) ist. Die 1 wird vom if als True interpretiert und die 0 als False. Das %-Zeichen nennt sich der Modulo-Operator. Diesen gibt es in vielen Programmiersprachen und ist für einige Anwendungsfälle sehr nützlich.

# Ohne List Comprehension

result = []
for i in [0, 1, 2, 3, 4, 5]:
    if i % 2:
        result.append(i)
    else:
        result.append(i*i)

print(result)                       #[0, 1, 4, 3, 16, 5]


# Ohne List Comprehension, aber ohne if-else-Block

result = []
for i in [0, 1, 2, 3, 4, 5]:
    result.append(i if i % 2 else i * i)

print(result)                       #[0, 1, 4, 3, 16, 5]


# Mit List Comprehension
result = [i if i % 2 else i * i for i in [0, 1, 2, 3, 4, 5]]
print(result)



# #Es ist auch möglich verschachtelte Schleifen in List Comprehensions zu übersetzen.

# Hinweis zum folgenden Beispiel: Im folgenden Beispiel wird range(4) genutzt. Dies kann man sich als eine Kurzschreibweise für das Anlegen einer Liste mit dem Inhalt [0, 1, 2, 3] vorstellen. Allgemein kann also mit range(n) etwas ähnliches angelegt werden, wie eine Liste mit n Elmenten, nämlich [0, 1, ..., n-1]. Warum nur "etwas ähnliches wie eine Liste"? range baut keine komplette Liste im Speicher auf, sondern liefert auf Nachfrage ein Element nach dem anderen aus der imaginären Liste. Dies spart sehr viel Speicherplatz, Rechenzeit und auch Schreibarbeit. Die Elemente von 0 bis 1000 nacheinander zu erhalten ist mit range(1001) schnell geschafft, aber diese lange Liste komplett aufzuschreiben, ist sehr als mühseelig.

# 💻

# Code ohne List Comprehension

result = []
for i in range(4):
    for j in range(4):
        result.append(i * j)
print(result)                               #[0, 0, 0, 0, 0, 1, 2, 3, 0, 2, 4, 6, 0, 3, 6, 9]


#list comprehension
result = [i * j for i in range (4) for j in range (4)]
print(result) 



