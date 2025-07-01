#Schreibe mithilfe der for-Schleife ein Programm, das alle Elemente einer 
# Liste miteinander multipliziert und dieses Produkt am Ende ausgibt.

product = 1 # Lösung wird in der Variable product gespeichert 

factors = [2, 3, 4] # Diese Werte sollen alle miteinander multipliziert werden
product = 1 
for f in factors:
    product = product * f
print(f'Das Produkt von {factors} ist {product}')

