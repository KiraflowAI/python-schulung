#Wie oft wird auf der Konsole der Buchstabe a ausgegeben, 
# wenn der folgende 
# Code ausgeführt wird?

for i in [1, 2, 3, 4]:
    for j in [5, 6, 7]:
        print("a")

#Erstelle eine Variable counter, die mitzählt, wie oft 
# a ausgegeben wird.

# Hier handelt es sich  um eine verschachtelte Schleife. 
# Die erste Schleife wird 4 mal durchlaufen. innerhalb dieser ist
# eine schleife die 3 mal durchläuft. also 4*3 
# ausgegeben wird deshalb 12 mal (durchlaufene Schleifen 4*4)


#Erstelle eine Variable counter, die mitzählt, wie oft a ausgegeben wird.

counter = 0
for i in [1, 2, 3, 4]:
    for j in [5,6,7]:
        print('a')
        counter += 1
print(counter)

# mit counter werden die durchlaufenen mal addiert und das ergebnis wird ausgegeben






