# a) Schreibe ein Programm, mit dem man die Mathenote von Sophie ausließt.

# b) Schreibe weiter ein Programm, das berechnet, wie viele Fächer Sophie belegt hat.

# c) Schreibe ein Programm, dass die Summe aller Noten von Sophie aurrechnet.

# d) Schreibe ein Programm, dass die Durchschnitsnote von Sophie ausrechnet.

# e) Schreibe ein Programm, das für jeden Studenten den Durchschnitt seiner Noten berechnet und diesen ausgibt.

# f) Schreibe ein Programm, das für ein Fach den Durchschnitt aller Noten berechnet. Das jeweilige Fach wird über eine Nutzereingabe ermittelt.

# Nutze Schleifen, um durch das Dictionary zu iterieren.

# Hinweis:

# Mit len(my_dict) können die Anzahl der Einträge in einem Dictionary bestimmt werden.

# Mit sum(my_list) werden die Elemente einer Liste aufsummiert.


# Hinweis ausblenden

# Mit len(my_dict) können die Anzahl der Einträge in einem Dictionary bestimmt werden.

# Mit sum(my_list) werden die Elemente einer Liste aufsummiert.


studenten = {
      "Anna": {
          "Mathe": 1,
          "Englisch": 2,
          "Biologie": 2,
          "Geschichte": 3,
          "Kunst": 1
      },
      "Max": {
          "Mathe": 3,
          "Englisch": 2,
          "Physik": 4,
          "Chemie": 3,
          "Sport": 2
      },
      "Lisa": {
          "Mathe": 2,
          "Englisch": 1,
          "Biologie": 2,
          "Geschichte": 3,
          "Kunst": 1,
          "Musik": 2
      },
      "Tom": {
          "Mathe": 4,
          "Englisch": 3,
          "Physik": 2,
          "Chemie": 2,
          "Geographie": 3,
          "Sport": 4
      },
      "Julia": {
          "Mathe": 1,
          "Englisch": 1,
          "Geschichte": 2,
          "Biologie": 2,
          "Musik": 1,
          "Kunst": 2
      },
      "Paul": {
          "Mathe": 2,
          "Englisch": 3,
          "Physik": 3,
          "Chemie": 2,
          "Sport": 1,
          "Geschichte": 3
      },
      "Sophie": {
          "Mathe": 3,
          "Englisch": 2,
          "Geschichte": 3,
          "Kunst": 2,
          "Sport": 2,
          "Biologie": 3
      }
  }


#a.) Welche note
print(studenten['Sophie']['Mathe'])

#b.) Wie viel fächer sophie
durch = print(len(studenten['Sophie']))


#c.) Summe noten sophie
summe = 0
for note in studenten['Sophie'].values():
    summe += note
print(summe)

#oder

summe = sum(studenten['Sophie'].values())
print(summe)


#d.) Durchschnitt
# durchschnitt = summe / n #### falsch
# print(durchschnitt)

#e.) 

# for naem, noten in studenten.items():
#     summe = sum(noten.values())
#     durchschnitt = summe / durch 
#     print(f'{name} hat die Durchschnittsnote {durchschnitt}')

#f.) Fach durchschnitt

fach = input('Welches Fach?')

counter = 0
summe = 0

for name, noten in studenten.items():
    if fach in noten.keys():
        summe += noten[fach]
        counter += 1
if counter == 0:
    print(f'Fach {fach} wurde nie belegt')
else:
    print(f'Durchschnittsnotte im Fach {fach} ist {summe / counter}')


