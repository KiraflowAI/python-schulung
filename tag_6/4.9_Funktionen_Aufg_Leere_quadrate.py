# Jürgen möchte gerne seine Quadratfunktion ändern, sodass Sie nur die äußeren Symbole des Quadrates zeichnet.

# Das soll also z.B. so aussehen:

        #   quadrat(5)


# *****
# *   *
# *   *
# *   *
# *****


# Jürgen denkt, er kann dies gut durch das hinzufügen einer Bedingung in der inneren Schleife seines Codes erreichen. Er stellt sich das wie folgt vor:


# def quadrat(n, symbol='*'):
#     for i in range(n):
#         for j in range(n):
#             s = ___ if ___ else ___
#             print(s, end="")
#         print()


# a) Hilf Jürgen dabei, seinen Code zu vervollständigen

def quadrat(n, symbol='*'): 
#n ist die Größe des Quadrats (also Höhe und Breite).symbol='*' ist das Zeichen, das du benutzen willst. Wenn du nichts angibst, wird * verwendet.
    for i in range(n):
#Schleife über die Zeilen. i steht für die aktuelle Zeilennummer (von 0 bis n-1).Beispiel bei n=5: i läuft durch 0, 1, 2, 3, 4.
        for j in range(n):
#Schleife über die Spalten (also die Zeichen in einer Zeile).j steht für die aktuelle Spaltennummer (von 0 bis n-1)
            s = symbol if i in [0, n-1] or j in [0, n-1] else " "

#Ziel: Wir wollen nur an den Rändern ein Symbol (*) drucken, sonst ein Leerzeichen.

# i in [0, n-1] → Erste oder letzte Zeile?

# j in [0, n-1] → Erste oder letzte Spalte?

# Wenn ja, drucke symbol (*)

# Wenn nein, drucke " " (Leerzeichen)


            print(s, end="")
# #Druckt das Zeichen s, aber ohne automatisch eine neue Zeile anzufangen.
# So bleiben die Zeichen in einer Zeile nebeneinander stehen.


        print()
# Nach jeder Zeile wird hier ein Zeilenumbruch erzeugt, damit die nächste Zeile korrekt darunter beginnt.

quadrat(0)


# Beispiel bei n = 5:
# i (Zeile)	j (Spalte)	Ausdruck s
# 0	0–4	symbol → erste Zeile: *****
# 1	0	symbol (Rand)
# 1	1–3	" " (innen)
# 1	4	symbol (Rand)
# …	…	…
# 4	0–4	symbol → letzte Zeile: *****


                #b.)b) Lösung mit Parameter:


# def quadrat(n, symbol='*', filled=True):
#     for i in range(n):
#         for j in range(n):
#             s = symbol if filled or i in [0, n-1] or j in [0, n-1] else " "
#             print(s, end="")
#         print()
# quadrat(5)




# mit benutzereingabe:


def quadrat(n, symbol='*', filled=True):
    for i in range(n):
        for j in range(n):
            s = symbol if filled or i in [0, n-1] or j in [0, n-1] else " "
            print(s, end="")
        print()

# --- Benutzerinteraktion ---
n = int(input("Wie groß soll das Quadrat sein? (z. B. 5): "))
zeichen = input("Welches Zeichen willst du benutzen? (z. B. *, #, @): ")
rahmen = input("Nur Rahmen? (ja/nein): ").strip().lower() == "ja"

quadrat(n, symbol=zeichen, filled=not rahmen)