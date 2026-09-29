while True:
    try:
        numero_dia = int(input("Escribe un número del 1 al 7: "))

        match numero_dia:
            case 1:
                print("El día seleccionado es: Lunes")
                break

        # Completa los casos del 2 al 7.
            case 2:     
                print("El día seleccionado es: Martes")
                break

        # Completa los casos del 2 al 7.
            case 3:
                print("El día seleccionado es: Miercoles")
                break

        # Completa los casos del 2 al 7.

            case 4:
                print("El día seleccionado es: Jueves")
                break

        # Completa los casos del 2 al 7.
            case 5:
                print("El día seleccionado es: Viernes")
                break

        # Completa los casos del 2 al 7.

            case 6:
                print("El día seleccionado es: Sabado")
                break
        
            case 7:
                print("El día seleccionado es: Domingo")
                break      
            
            case _:
                print("Error: el número debe estar entre 1 y 7.")
                break
    except ValueError:

        print("dato invalido")