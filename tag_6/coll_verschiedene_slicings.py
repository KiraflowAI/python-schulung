#Sage für alle unten vorgegeben Slicings voraus, was das Ergebnis ist.

#Finde heraus, was bedeutet es, wenn man keine Zahl beim Slicing einträgt, z.B. s[:5]?

# --> Wenn man keine zahl einträgt ist es von anfang, wenn es am anfang steht oder am ende bis zum ende


s = 'Echsenmensch'
print(s[2:5]) # 2.er buchstabe bis 5 buchstabe

s="Echsenmenschen"
print(s[0:5])

s="Echsenmenschen"
print(s[:5])


s="Echsenmenschen"
print(s[2:])

s="Echsenmenschen"
print(s[2])

s="Echsenmenschen"
print(s[5])

s="Echsenmenschen"
print(s[:-2])


s="Echsenmenschen"
print(s[-4:])

s="Echsenmenschen"
print(s[6:-2])

s="Echsenmenschen"
print(s[-4:-2])

s="Echsenmenschen"
print(s[-2:-4])

s[0:7:2]

s[1:8:2]

s[::2]

s[:-4:3]

s[::-1]

s[7:-2:-1]

s[1:1]

s[0:4:]

s[:4:]

s[:]

s[::]

s[:1000]

i = 4
s[:i]

s = "Echsenmenschen"

# s[2:5] → Zeichen an den Indizes 2, 3, 4 ("h", "s", "e")
print("s[2:5] =", s[2:5])            # "hse"

# s[0:5] → Zeichen an den Indizes 0 bis 4 ("E", "c", "h", "s", "e")
print("s[0:5] =", s[0:5])            # "Echse"

# s[:5] → entspricht s[0:5] (ohne expliziten Startwert wird 0 angenommen)
print("s[:5] =", s[:5])              # "Echse"

# s[2:] → Zeichen ab Index 2 bis zum Ende
print("s[2:] =", s[2:])              # "hsenmenschen"

# s[2] → einzelnes Zeichen an Index 2
print("s[2] =", s[2])                # "h"

# s[5] → einzelnes Zeichen an Index 5
print("s[5] =", s[5])                # "n"

# s[:-2] → alle Zeichen außer den letzten beiden
print("s[:-2] =", s[:-2])            # "Echsenmensch"

# s[-4:] → die letzten vier Zeichen
print("s[-4:] =", s[-4:])            # "chen"

# s[6:-2] → Zeichen von Index 6 bis zum vorletzten Zeichen (Index -2 wird nicht mit eingeschlossen)
print("s[6:-2] =", s[6:-2])          # "mensch"

# s[-4:-2] → Zeichen von Index -4 bis -3
print("s[-4:-2] =", s[-4:-2])        # "ch"

# s[-2:-4] → leere Zeichenkette, da der Startindex bei positivem Schritt nach dem Endindex liegt
print("s[-2:-4] =", s[-2:-4])        # ""

# s[0:7:2] → von Index 0 bis 6 mit Schrittweite 2 (Indices 0, 2, 4, 6)
print("s[0:7:2] =", s[0:7:2])        # "Ehem"

# s[1:8:2] → von Index 1 bis 7 mit Schrittweite 2 (Indices 1, 3, 5, 7)
print("s[1:8:2] =", s[1:8:2])        # "csne"

# s[::2] → die ganze Zeichenkette mit Schrittweite 2 (jedes zweite Zeichen)
print("s[::2] =", s[::2])            # "Ehemnce"

# s[:-4:3] → von Beginn bis Index -4 (nicht eingeschlossen) mit Schrittweite 3
#    Gewählte Indizes: 0, 3, 6, 9.
print("s[:-4:3] =", s[:-4:3])        # "Esms"

# s[::-1] → die ganze Zeichenkette in umgekehrter Reihenfolge
print("s[::-1] =", s[::-1])          # "nehcsnemneshcE"

# s[7:-2:-1] → mit negativer Schrittweite ergibt dies eine leere Zeichenkette, da der Startindex nicht über den Endindex hinausgeht
print("s[7:-2:-1] =", s[7:-2:-1])    # ""

# s[1:1] → leere Zeichenkette, da Start- und Endindex identisch sind
print("s[1:1] =", s[1:1])            # ""

# s[0:4:] → entspricht s[0:4] (ohne explizite Schrittweite wird 1 angenommen)
print("s[0:4:] =", s[0:4:])          # "Echs"

# s[:4:] → entspricht s[0:4]
print("s[:4:] =", s[:4:])            # "Echs"

# s[:] → die gesamte Zeichenkette (ohne Start- und Endangabe)
print("s[:] =", s[:])                # "Echsenmenschen"

# s[::] → ebenfalls die gesamte Zeichenkette (Standard-Schrittweite 1)
print("s[::] =", s[::])              # "Echsenmenschen"

# s[:1000] → Es gibt keinen Fehler (im Gegensatz zur Indizierung), sondern alle Zeichen werden ausgelesen.
print("s[:1000] =", s[:1000])              # "Echsenmenschen"

# s[:i] → s[:4] → Index ist in einer Variable gespeichert.
i = 4
print("s[:i] =", s[:i])              # "Echs"
