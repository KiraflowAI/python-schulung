# #Diese Aufgabe ist optional.

# a) Welche Bedingung muss im folgenden Code für die ... eingesetzt werden, damit die gesuchte Konsolenausgabe erscheint?

result = [[i, j] for i in [1, 2, 3] for j in [1, 2, 3] if i >= j]
print(result) # [[1, 1], [2, 1], [2, 2], [3, 1], [3, 2], [3, 3]]

#b.) b) Erstelle durch List Comprehension drei Listen, die jeweils eine der folgenden Listen ausgibt.

# a = [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [1, 2], [1, 3]]

# b = [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6], [0, 3, 6, 9]]

# c = [['aA', 'bA', 'cA'], ['aB', 'bB', 'cB'], ['aC', 'bC', 'cC']]

a = [[i, j] for i in [0, 1] for j in [0, 1, 2, 3]]
print(a)

b = [[i*j for i in [0, 1, 2, 3]] for j in [0, 1, 2, 3]]
print(b)

c = [[i+j for i in "abc"] for j in "ABC"]
print(c)

# auch möglich mit range: 

# a = [[i,j] for i in range(2) for j in range(4)]

# b = [[i*j for i in range(4)] for j in range(4)]

# c = [[i+j for i in "abc"] for j in "ABC"]