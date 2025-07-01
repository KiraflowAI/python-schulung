jahr = int(input('Jahreszahl:'))

if jahr % 4 == 0: #ist es durch 4 teilbar == 0 : ohne Rest
    if jahr % 100 == 0:
        if jahr % 400 == 0:
            schaltjahr = True
        else:
            schaltjahr = False
    else:
        schaltjahr = True
else:
    schaltjahr = False

if schaltjahr: 
    print(jahr, 'ist kein Schaltjahr')
else:
    print(jahr, 'ist kein Schaltjahr')

# % Modulo der Rest nach der Division wird angezeigt
# // floordivision (Division aber Rest wird ignoriert)
# / division (ganz normale Division, bei der auch eine Kommazahl herauskommen kann)