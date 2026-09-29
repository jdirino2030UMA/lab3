tem = [18, 25, 31, 12, 28, 35, 20]
tem.sort()
cantdiafrio = 0
cantdiatibio = 0
cantdiacal = 0
for variable in tem:

    if variable <= 15:

        print(variable, "grados es frio")
        cantdiafrio += 1

    elif 25 >= variable > 15:

        print(variable, "grados es tibio")
        cantdiatibio += 1

    elif variable > 25:

        print(variable, "grados es caliente")
        cantdiacal += 1

print("fueron ", cantdiafrio, "dias frios, ", cantdiatibio, "dias tibios y ", cantdiacal, "dias calientes")