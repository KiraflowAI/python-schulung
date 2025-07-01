#a)Gegeben sei die folgende Liste:

#lst = [1, 2, 3]

#Schreiben Sie einen Code, der eine neue Liste new_lst erzeugt, 
# #ndem alle Einträge der Liste lst verdoppelt werden. 
# Also hier new_lst == [2, 4, 6, 8]

lst = [1, 2, 3]
new_lst = []
for i in lst:
    new_lst.append(i * 2)
print(new_lst)


#b)Gegeben sei die folgende Liste:

#    names = ["Anton", "Ben", "Christian"]

#Schreiben Sie einen Code, der eine neue Liste names_lens erzeugt, indem von allen Einträgen der Liste names die Länge berechnet wird. Also hier names_lens == [5, 3, 9].

# names = ['Anton', 'Ben', 'Christian']
# names_lens = []
# for name in names:
#     names_lens.append(len(name))

# #23-25 --> names_lens = [len(name) for name in names]

# print(names)
# print(names_lens)
#print(names + names_lens)

#c) Bonus: Schreibe den Code mit einer List-Comprehension. (Wenn du das noch nicht kennst, wirst du es später kennenlernen und kannst dann zu dieser Aufgabe zurückkehren.)

names = ['Anton', 'Ben', 'Christian']
names_lens = [len(name) for name in names]
print(names_lens)

