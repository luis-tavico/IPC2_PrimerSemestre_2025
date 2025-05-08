from Cuenta import Cuenta

class CuentaAhorro(Cuenta):
    def __init__(self, titular, numeroCuenta, saldo, tasaInteres=0.05):
        super().__init__(titular, numeroCuenta, saldo)
        self.__tasaInteres = tasaInteres

    def calcular_interes(self):
        interes = self.getSaldo() * self.__tasaInteres
        self.depositar(interes)
        print(f"Interés de {interes} añadido a la cuenta de ahorro.")

    # Polimorfismo: Se redefine el método en la subclase
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Tasa de interés: {self.__tasaInteres * 100}%")