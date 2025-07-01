#Untersuche, was der folgende Code tut:

my_list = [i for i in range(50)]
print(my_list)

#basierend auf deinen Beobachtungen, Wandle den Code so um, dass stattdessen die folgenden Ausgaben erscheinen:

#[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# 50 Nullen

my_list = [0 for i in range(50)]
print(my_list)

#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625]  
# Quadratzahlen von 1 bis 25

my_list = [i * i for i in range(26)]
print(my_list)
