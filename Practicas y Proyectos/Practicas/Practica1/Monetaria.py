from Cuenta import Cuenta

class CuentaMonetaria(Cuenta):
    def __init__(self, titular, numeroCuenta, saldo, limiteCredito=500):
        super().__init__(titular, numeroCuenta, saldo)
        self.__limiteCredito = limiteCredito

    # Metodos getter y setter para acceder a los atributos privados
    def getLimiteCredito(self):
        return self.__limiteCredito
    
    def setLimiteCredito(self, limiteCredito):
        self.__limiteCredito = limiteCredito

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= (self.getSaldo() + self.__limiteCredito):
            self._actualizar_saldo(-cantidad)
            print(f"Retiro exitoso de {cantidad}. Nuevo saldo: {self.getSaldo()}")
        else:
            print("Fondos insuficientes o cantidad excede el límite de crédito.")

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Límite de crédito: {self.__limiteCredito}")