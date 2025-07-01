# a.) erstelle eine liste der quadrate der zahlen 1 bis 10 , also 1,4,9,16

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quadrat_numbers = [n * n for n in numbers]
print(quadrat_numbers)

# die zahlen n sollen mit den zahlen n quadriert werden, wobei die zahlen n aus n kommen
# oder n ** 2 
# man kann auch numbers direkt in die variable schreiben:

quadrat_numbers = [n * n for n in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
print(quadrat_numbers)

# oder man kann es mit range machen
quadrat_numbers = [n ** 2 for n in range(1, 11)]
print(quadrat_numbers)


#b.) Erstelle eine liste mit den längen jedes wortes in einer vorgegeben liste von wörtern 
# z.b. [Hallo, johannes, hatte] [5,6,7]

wortlaenge = [len(wort) for wort in ['Hallo', 'Johannes', 'hatte']]
print(wortlaenge)
# [5, 8, 5]

#c.) erstelle eine liste der ersten zeichen jedes wortes in einer liste von wörtern 
#z.b. [hallo, johannes, hatte ] [h, j, h]

['Hallo', 'Johannes', 'hatte']
erste_zeichen = [wort[0] for wort in ['Hallo', 'Johannes', 'hatte']]
print(erste_zeichen)