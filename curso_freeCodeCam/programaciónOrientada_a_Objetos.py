'''PROGRAMACIÓN ORIENTADA A OBJETOS: 

ejemplo: 
"se creará un pequeño programa"
-Número de Cuenta
-Nombre del Titular
-Balanc Inicial
-Balance Actual
-Fecha de Apertura
-...
'''
class CuentaBancaria:
    def __init__(self, num_cuenta, nombre_titular, balance):
        self.numero_cuenta = num_cuenta
        self.nombre_titular = nombre_titular
        self.balance = balance

    def generar_balance(self):
        print(self.balance)
    def depositar(self, monto):
        if monto > 0:
            self.balance += monto

mi_cuenta = CuentaBancaria("105-356-643", "Nora Smith", 5600)
mi_cuenta.generar_balance()

mi_cuenta.depositar(400)

mi_cuenta.generar_balance()