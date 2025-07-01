#Erstelle einen Code, der die folgende Fehlermeldung erzeugt.
#Diese soll, bis auf die Adresse des Files identisch sein.

#   a.)
# Traceback (most recent call last):
#   File "c:\Users\Vikto\PycharmProjects\einfuehrung-python\something.py", line 2, in <module>
#     print(x[9])
#           ~^^^
# IndexError: string index out of range

x = 'Hallo'
print(x[x[9]])



   #b.)

#    Traceback (most recent call last):
#   File "c:\Users\Vikto\PycharmProjects\einfuehrung-python\something.py", line 2, in <module>
#     print(x[9])
#           ~^^^
# IndexError: string index out of range

"Hallo"[:::-1]
