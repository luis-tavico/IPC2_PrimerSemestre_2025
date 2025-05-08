class Cuenta:
    def __init__(self, titular, numeroCuenta, saldo):
        # Encapsulación: Atributos privado
        self.__titular = titular  
        self.__numeroCuenta = numeroCuenta
        self.__saldo = saldo

    # Métodos getter para acceder a los atributos privados
    def getTitular(self):
        return self.__titular

    def getNumeroCuenta(self):
        return self.__numeroCuenta

    def getSaldo(self):
        return self.__saldo
    
    # Métodos setter para modificar los atributos privados
    def setTitular(self, titular):
        self.__titular = titular

    def setNumeroCuenta(self, numeroCuenta):
        self.__numeroCuenta = numeroCuenta

    def setSaldo(self, saldo):
        self.__saldo = saldo

    # Métodos de la clase
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depósito exitoso de {cantidad}. Nuevo saldo: {self.__saldo}")
        else:
            print("La cantidad a depositar debe ser mayor a 0.")

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Retiro exitoso de {cantidad}. Nuevo saldo: {self.__saldo}")
        else:
            print("Fondos insuficientes o cantidad inválida.")

    def mostrar_saldo(self):
        print(f"Saldo actual de la cuenta {self.__numeroCuenta}: {self.__saldo}")

    def mostrar_informacion(self):
        print(f"Titular: {self.__titular}")
        print(f"Número de cuenta: {self.__numeroCuenta}")
        print(f"Saldo: {self.__saldo}")

    # Método protegido (puede ser usado en clases hijas)
    def _actualizar_saldo(self, cantidad):
        self.__saldo += cantidad