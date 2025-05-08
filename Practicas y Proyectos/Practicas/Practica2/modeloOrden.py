class Orden:
    def __init__(self, numero, nombreCliente, cantidadPizzas, pizzas, tiempoTotal, tiempoEnCola):
        self.numero = numero
        self.nombreCliente = nombreCliente
        self.cantidadPizzas = cantidadPizzas
        self.pizzas = pizzas
        self.tiempoTotal = tiempoTotal
        self.tiempoEnCola = tiempoEnCola

    def getNumero(self):
        return self.numero

    def getNombreCliente(self):
        return self.nombreCliente

    def getCantidadPizzas(self):
        return self.cantidadPizzas

    def getPizzas(self):
        return self.pizzas

    def getTiempoTotal(self):
        return self.tiempoTotal

    def getTiempoEnCola(self):
        return self.tiempoEnCola

    def setNumero(self, numero):
        self.numero = numero

    def setNombreCliente(self, nombreCliente):
        self.nombreCliente = nombreCliente

    def setCantidadPizzas(self, cantidadPizzas):
        self.cantidadPizzas = cantidadPizzas

    def setPizzas(self, pizzas):
        self.pizzas = pizzas

    def setTiempoTotal(self, tiempoTotal):
        self.tiempoTotal = tiempoTotal

    def setTiempoEnCola(self, tiempoEnCola):
        self.tiempoEnCola = tiempoEnCola