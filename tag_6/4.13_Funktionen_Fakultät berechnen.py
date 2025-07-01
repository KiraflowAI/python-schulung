# def fak(n):
#     if n == 0:
#         return 1  # Sonderfall Wenn jemand fak(0) eingibt, dann gib sofort 1 zurück.

#     ergebnis = 1  #Das ist unser Startwert. Wir beginnen mit 1, weil 1 die neutrale Zahl beim Multiplizieren ist.
    
#     for i in range(1, n + 1):
# #range(1, n + 1) bedeutet: Zähle von 1 bis einschließlich n.
# # Bei jedem Durchlauf: ergebnis = ergebnis * i (Kurzform: *=)
#      ergebnis *= i
#     return ergebnis
# print(fak(5))





# def fak(n, tiefe=0):
#     einrueckung = "  " * tiefe  # Für schönere Darstellung der Stufen

#     print(f"{einrueckung}fak({n}) wird aufgerufen")

#     if n == 0:
#         print(f"{einrueckung}fak(0) = 1 (Abbruchbedingung)")
#         return 1
#     else:
#         print(f"{einrueckung}→ berechne: {n} * fak({n - 1})")
#         ergebnis = n * fak(n - 1, tiefe + 1)
#         print(f"{einrueckung}← fak({n}) = {ergebnis}")
#         return ergebnis


#print("Ergebnis:", fak(4))

# Lösung mit while schleife

def fak(n):
    result = 1
    counter = 1
    while counter <= n:
        result = result * counter
        counter = counter + 1
    return result
print(fak(6))

#Lösung mit for-Schleife und range:

def fak(n):
    result = 1
    for counter in range (1, n+1):
        result = result * counter
    return result 
print(fak(5))


