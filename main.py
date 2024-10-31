from sumar import suma
from resta import resta
from multiplicacion import multiplicar
from dividir import dividir
from suma_avanzada import suma_avanzada

def menu():
    print("--------------------------")
    print("-Calduladora Open Source-")
    print("--------------------------") 
    print("Selecciona una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Suma Avanzada (+ de 2 números)")
    print("6. Salir")

opcion = 0

def main():
    while True:
        print()
        menu()
        opcion = input("Ingresa una opción: ")
        print()
        if opcion == "1":
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            print("Resultado:", suma(a, b))
        elif opcion == "2":
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            print("Resultado:", resta(a, b))
        elif opcion == "3":
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            print("Resultado:", multiplicar(a, b))
        elif opcion == "4":
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            print("Resultado:", dividir(a, b))
        elif opcion == "5":
            numeros = input("Ingresa los numeros separados por comas: ").split(",")
            numeros = [float(num) for num in numeros]
            print("Resultado:", suma_avanzada(*numeros))
        elif opcion == "6":
            print("Hasta luego, vuelva pronto")
            break
        else:
            print("Opción inválida. Intentalo de Nuevo.")

main()
