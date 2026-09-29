def sumar(primer_numero, segundo_numero):
    return primer_numero + segundo_numero

def restar(primer_numero, segundo_numero):
    return primer_numero - segundo_numero

def multiplicar(primer_numero, segundo_numero):
    return primer_numero * segundo_numero

def dividir(primer_numero, segundo_numero):
    if segundo_numero == 0:
        return "Error: No se puede dividir entre cero."
    return primer_numero / segundo_numero

def es_par(numero):
    if numero % 2 == 0:
        return f"El número {numero} es PAR."
    return f"El número {numero} es IMPAR."


while True:
    print("\n--- CALCULADORA ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Verificar si un número es par")
    print("6. Salir")

    # Esta línea DEBE llevar sangría (4 espacios) para estar dentro del bucle
    opcion = input("Elige una opción: ")

    # El match también va dentro del bucle
    match opcion:
        case "1":
            num1 = int(input("Primer número: "))
            num2 = int(input("Segundo número: "))
            print(f"Resultado: {sumar(num1, num2)}")

        case "2":
            num1 = int(input("Primer número: "))
            num2 = int(input("Segundo número: "))
            print(f"Resultado: {restar(num1, num2)}")

        case "3":
            num1 = int(input("Primer número: "))
            num2 = int(input("Segundo número: "))
            print(f"Resultado: {multiplicar(num1, num2)}")

        case "4":
            num1 = int(input("Primer número: "))
            num2 = int(input("Segundo número: "))
            print(f"Resultado: {dividir(num1, num2)}")

        case "5":
            num = int(input("Ingresa un número: "))
            print(es_par(num))

        case "6":
            print("¡Hasta luego!")
            break


        case _:
            print("Opción no válida. Por favor, elige un número del 1 al 6.")