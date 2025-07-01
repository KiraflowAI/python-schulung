list_0 = []
#print(list_0)

list_0.append(15)
#print(list_0)

list_0.append(3 * 2) # Ausgabe= 15 und 6 
print(list_0)

a = 5
b = 15
list1= [1 + 1, 1 / 2, a, a + b] # Ausgabe: 20, 5, 5, 20
#print(list1)
list1.append(a * b +7) # 5*15+7 = 82 Ausgabe: 20,5,5,20,82
#print(list1)

list1.append(list1[0]) # Die Stelle 0 innerhalb des indexes ist = 1+1, also = 2 
print(list1)

