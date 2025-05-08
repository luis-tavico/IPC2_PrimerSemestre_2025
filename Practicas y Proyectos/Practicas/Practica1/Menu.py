import random
from Ahorro import CuentaAhorro
from Monetaria import CuentaMonetaria

if __name__ == '__main__':

    cuentaAhorro = None
    cuentaMonetaria = None

    while True:
        print("================Menu Bancario================")
        print("|1. Abrir Cuenta                            |")
        print("|2. Gestionar Cuenta                        |")
        print("|3. salir                                   |")
        print("=============================================")
        opcion = int(input("Seleccione una opcion: "))

        if opcion == 1:
            print("================Menu Bancario================")
            print("|1. Cuenta de ahorro                        |")
            print("|2. Cuenta monetaria                        |")
            print("|3. regresar                                |")
            print("=============================================")
            opcion = int(input("Seleccione una opcion: "))

            if opcion == 1:
                titular = input("Ingrese el nombre del titular: ")
                numeroCuenta = ""
                for _ in range(16):
                    numeroCuenta += str(random.randint(0, 9))
                saldo = float(input("Ingrese el saldo inicial: "))
                tasaInteres = float(input("Ingrese la tasa de interes: "))
                cuentaAhorro = CuentaAhorro(titular, numeroCuenta, saldo, tasaInteres)
                print(f"Cuenta de ahorro creada exitosamente. Número de cuenta: {numeroCuenta}")
            elif opcion == 2:
                titular = input("Ingrese el nombre del titular: ")
                numeroCuenta = ""
                for _ in range(16):
                    numeroCuenta += str(random.randint(0, 9))
                saldo = float(input("Ingrese el saldo inicial: "))
                limiteCredito = float(input("Ingrese el límite de crédito: "))
                cuentaMonetaria = CuentaMonetaria(titular, numeroCuenta, saldo, limiteCredito)
                print(f"Cuenta monetaria creada exitosamente. Número de cuenta: {numeroCuenta}")
            elif opcion == 3:
                continue
            else:
                print("Ingrese una opcion valida.")
        elif opcion == 2:
            if cuentaAhorro is None and cuentaMonetaria is None:
                print("No hay cuentas registradas.")
            else:
                print("================Menu Bancario================")
                print("|1. Ver informacion de cuentas              |")
                print("|2. Depositar dinero                        |")
                print("|3. Retirar dinero                          |")
                print("|4. Calcular interes (Solo Cuenta de Ahorro)|")
                print("|5. regresar                                |")
                print("=============================================")
                opcion = int(input("Seleccione una opcion: "))
                if opcion == 1:
                    print("\nInformación de la Cuenta de Ahorro:")
                    cuentaAhorro.mostrar_informacion()
                    print("\nInformación de la Cuenta Monetaria:")
                    cuentaMonetaria.mostrar_informacion()
                
                elif opcion == 2:
                    tipoCuenta = input("¿En qué cuenta desea depositar? (ahorro/monetaria): ").strip().lower()
                    cantidad = float(input("Ingrese la cantidad a depositar: "))
                    if tipoCuenta == "ahorro":
                        cuentaAhorro.depositar(cantidad)
                    elif tipoCuenta == "monetaria":
                        cuentaMonetaria.depositar(cantidad)
                    else:
                        print("Opción no válida.")
                
                elif opcion == 3:
                    tipoCuenta = input("¿De qué cuenta desea retirar? (ahorro/monetaria): ").strip().lower()
                    cantidad = float(input("Ingrese la cantidad a retirar: "))
                    if tipoCuenta == "ahorro":
                        cuentaAhorro.retirar(cantidad)
                    elif tipoCuenta == "monetaria":
                        cuentaMonetaria.retirar(cantidad)
                    else:
                        print("Opción no válida.")
                
                elif opcion == 4:
                    cuentaAhorro.calcular_interes()
                
                elif opcion == 5:
                    continue
                else:
                    print("Ingrese una opcion valida.")
        elif opcion == 3:
            print("Ejecucion finalizada.")
            break
        else:
            print("Ingrese una opcion valida.")