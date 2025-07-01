# jahr = int(input("Jahreszahl: "))

# schaltjahr = False
# if jahr % 4 == 0:
#     schaltjahr = True
# if jahr % 100 == 0:
#     schaltjahr = False
# if jahr % 400 == 0:
#     schaltjahr = True

# if schaltjahr:
#     print(jahr, "ist ein Schaltjahr.")
# else:
#     print(jahr, "ist kein Schaltjahr.")

# kürzen der codes mit and / or / not 

# 1. version

# jahr = int(input('Jahreszahl:'))

# schaltjahr = (jahr % 4 == 0 and not jahr % 100 == 0) or jahr % 400 == 0

# if schaltjahr:
#     print(jahr, 'Ist kein Schaltjahr')
# else:
#     print(jahr, 'Ist kein Schaltjahr')

# 2. Version

jahr = int(input('Jahreszahl:'))

schaltjahr = (jahr % 4 == 0 and not jahr % 100 == 0) or jahr % 400 == 0

print(f'{jahr} ist {'k' if not schaltjahr else ''}ein Schaltjahr.')

# '' ist ein Platzhalter 
#

