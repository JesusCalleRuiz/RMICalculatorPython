import Pyro4

@Pyro4.expose
class Interfaz:
    def sumar(self, numero1, numero2):
        return numero1 + numero2

    def restar(self, numero1, numero2):
        return numero1 - numero2

    def multiplicar(self, numero1, numero2):
        return numero1 * numero2

    def dividir(self, numero1, numero2):
        if numero2 != 0:
            return numero1 / numero2
        else:
            return "Error: División por cero"

    def modulo(self, numero1, numero2):
        return numero1 % numero2

    def factorial(self, numero1):
        if numero1 < 0:
            return "Error: Factorial de número negativo"
        elif numero1 == 0 or numero1 == 1:
            return 1
        else:
            return numero1 * self.factorial(numero1 - 1)

#Registra la interfaz remota
daemon = Pyro4.Daemon()
uri = daemon.register(Interfaz)

#Imprime la URI para que el cliente se conectee
print("URI:", uri)

#Inicia el servidor
daemon.requestLoop()
