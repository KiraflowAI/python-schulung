
#In einer Liste notiert Peter für jeden Tag, wie viele Eiskugeln er verkauft hat. 
# Ihn interessiert was die höchste Zahl ist, die er notiert hat. Schreibe ein Programm, 
# das dies mit Hilfe einer for-Schleife berechnet.
#In Python gibt es auch eine Funktion, mit der ich das Maximum einer Liste bestimmen kann. 
# Recherchiere, welche das ist.

# eis = [12, 0, 24, 59, 120, 88, 30, 46, 77, 11, 32, 45, 109, 56, 2, 118, 62, 97, 20, 71]

# maximum = eis [0]
# for e in eis:
#     if e > maximum:
#         maximum = e
# print(f"Größte Anzahl verkaufter Eiskugeln an einem Tag sind: {maximum}")


eis = [12, 0, 24, 59, 120, 88, 30, 46, 77, 11, 32, 45, 109, 56, 2, 118, 62, 97, 20, 71]

maximum = max(eis)

print(f"Größte Anzahl verkaufter Eiskugeln an einem Tag sind: {maximum}")