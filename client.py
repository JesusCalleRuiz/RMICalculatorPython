import Pyro4

#Solicita la URI del servidor al usuario
uri = input("Ingresa la URI del servidor: ")
interfaz = Pyro4.Proxy(uri)

eleccion = None
while eleccion != -1:
    print("\n----------CALCULADORA---------\n")
    print("[-1] => Salir\n[0] => Sumar\n[1] => Restar\n[2] => Multiplicar\n[3] => Dividir\n[4] => Modulo\n[5] => Factorial")
    eleccion = int(input("Elige: "))

    if eleccion != -1:
        numero1 = float(input("Ingresa el número 1: "))
        if eleccion != 5:
            numero2 = float(input("Ingresa el número 2: "))
        
        if eleccion == 0:
            resultado = interfaz.sumar(numero1, numero2)
        elif eleccion == 1:
            resultado = interfaz.restar(numero1, numero2)
        elif eleccion == 2:
            resultado = interfaz.multiplicar(numero1, numero2)
        elif eleccion == 3:
            resultado = interfaz.dividir(numero1, numero2)
        elif eleccion == 4:
            resultado = interfaz.modulo(numero1, numero2)
        elif eleccion == 5:
            resultado = interfaz.factorial(numero1)

        print("Resultado:", resultado)

