#Häufig wollen wir bestimmte Operationen auf allen Elementen einer Liste durchführen. D
# ies kann zwar über eine while-Schleife implementiert werden, 
# ist aber etwas umständlich und sogar fehleranfällig. 
# Lieber wird mit der for-Schleife gearbeitet, die es erlaubt, alle Elemente einer Liste nacheinander durchzugehen, ohne dass dabei der Index zum Zugriff auf die Elemente genutzt werden muss.
# 


# Lege eine Liste mit Elementen an, die durchlaufen werden sollen.
# Es wird eine Variable i angelegt, die für den Zugriff auf die Liste über den Index benötigt wird.
# Solange i nicht größer ist als der größtmögliche Index, soll die Schleife durchlaufen werden. len(produkte) gibt die Anzahl der Elemente in der Liste zurück und ist hier 3.
# Um nun auf die Elemente zuzugreifen, wird die Index-Notation produkte[i] verwendet.
# Abschließend muss der Wert für i vergrößert werden, um sicher zu stellen, dass im nächsten Schleifendurchlauf auch auf das nächste Element zugegriffen wird.


produkte = ["Butter", "Milch", "Wurst"] # (1)!
i = 0 # (2)!

while i < len(produkte): # (3)!
    print(f"Heute gibt es {produkte[i]}.") # (4)!
    i = i + 1 # (5)!

    # wofür steht i???

# code mit for-loop
# Lege eine Liste mit Elementen an, die durchlaufen werden sollen.
# Hier wird eine Variable produkt angelegt und diese wird nun nacheinander mit allen Elementen der Liste produkte befüllt. Zuerst gilt also produkt = "Butter", mit dem die nächsten eingerückten Zeilen durgeführt wird. Danach ist produkt = "Milch" und die eingerückten Zeilen werden erneut durchgeführt. Dies geht so lange weiter, bis alle Elemente in der Liste durchlaufen wurden.
# Der eingerückte Code ist der Schleifenrumpf. Dieser wird so oft durchlaufen, wie es Elemente in der Liste gibt.

produkte = ['Butter', 'Milch', 'Wurst']

for produkt in produkte:
    print(f'Heute gibt es {produkt}')

    
    
list_of_lists = [1,2,3], [40,50,60], [700,800,900]
summe = 0

for sub_list in list_of_lists: # Hier wird mit sub_list alle Listen gemeint?
    for element in sub_list: # mit element sidn die inhalte der listen gemeint?
        summe += element # neue variable summe=das addierte element in der liste
    print(f'Zwischenergebnis: {summe}') # hier wird erst zwischenergebnis der listen ausgegeben (1+2+3=6)
print(f'Endergebnis: {summe}') # Hier wird das endergebnis der adierten listen ausgegeben

# wo wird hier im endergebnis gesagt das alle listen miteinander addiert werden sollen?


# vorzeitiges abbrechen einer schleife
#In vielen Fällen sucht man einfach einen Wert in einem Bereich oder ein bestimmtes Element in einer List. Sobald man dieses gefunden hat, kann man die Schleife eigentlich abbrechen. Dafür nutzt man das Keyword break:

for i in range(0, 10): # zahlen 0 bis 10 werden gelistet/gespeichert
    print (i)
    if i == 5:
        break
print('Ende')

#Sobald die Bedingung i == 5 wahr wird, sorgt break dafür, dass wir die Schleifen verlassen. Damit sparen wir uns 5 weitere Durchläufe. Bei komplexen Problemstellungen kann man damit sehr viel Zeit sparen.
#Auf der anderen Seite gibt es aber auch Fälle, in denen man nicht die ganze Schleife beenden will, sondern nur den aktuellen Durchlauf. Dafür nutzt man das Keyword continue.

for i in range(0, 10):
    if 3 <= i <= 5: #3 und 5 werden nicht ausgegeben 
        continue
    print(i)    

        
# Wieso? Für jeder Zahl zwischen 0 und 10 wird überprüft, ob diese Zahl zwischen 3 und 5 liegt. Ist das der Fall, springt der Code direkt an den Schleifenanfang (wegen des continue), statt die Zeile 4 auszuführen. direkt zum nächsten Durchlauf. In allen anderen Fällen wird die Zahl auf der Konsole ausgegeben.
# Sehr häufig wird break in Kombination mit while-Schleifen verwendet. Wieso? Weil es so einfach möglich ist, Endlosschleifen zu erzeugen, die unter bestimmten Bedingungen abbrechen, die nicht im Schleifenkopf überprüft werden.
# Zum Beispiel:

while True:
    eingabe = input()
    if eingabe == 'C':
        break
    print(f'Deine Eingabe in groß: {eingabe.upper()}')
print('ByeBye')

#??????

