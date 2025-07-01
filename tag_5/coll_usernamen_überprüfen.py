#In einem Onlineportal dürfen Nutzer ihren Benutzernamen frei wählen, 
# jedoch gibt es bestimmte Begriffe, die nicht als Teil des
#  Namens auftauchen dürfen. Diese sind in der folgenden 
# Liste verbotener Wörter notiert:

verboten = ['admin', 'super', 'user']

#In einem Onlineportal dürfen Nutzer ihren Benutzernamen frei wählen, jedoch gibt es bestimmte Begriffe, die nicht als Teil des Namens auftauchen dürfen. Diese sind in der folgenden Liste verbotener Wörter notiert:
# superman
# administrator
# Radminister
# Häuser
# superadmin
# admin

#Schreibe ein Programm, das den Nutzer um einen Namen bittet und eine Warnmeldung gibt, wenn der Name verboten ist.


# username = input('Nutzername eingeben: ')
# verboten = ['admin', 'super', 'user']

# for ...:
#     if ...:
        # print("Nutzername nicht erlaubt!")



username = input('Nutzername eingeben:')
verboten = ['admin', 'super', 'user']

for v in verboten:
    if v in username:
        print('Nutzername nicht erlaubt')
