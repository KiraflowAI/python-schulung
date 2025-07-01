students = ["Anton", "Bernd", "Carlo", "Dennis", "Eva"]
n = len(students) # Mit der Variable n wird die variable(liste) students bestimmt. 
#mit len(students) wird die anzahl der in der liste gespeicherten werte angezeigt

print(f"Länge der Liste: {n}") # hier wird die geschweifte klammer benutzt,
# um in der konsole auszugeben

print(students[-1]) # "Eva". Bei Minus wird von hinten der Liste abgezählt

print(students[-2]) # "Dennis"

print(students[-5]) # "Anton"

print(students[n-3]) # "Carlo"

print(students[-6])

print(students[5])

print(students[n]) # n = 5
