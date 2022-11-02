class CuentaBancaria:

    def __init__(self, balance, tasa_interes):
        self.balance = balance
        self.tasa_interes = tasa_interes

    def deposito(self, monto):
        self.balance += monto
        return self

    def retiro(self, monto):
        if monto > self.balance:
            self.balance -= 5
            return print("Fondos insuficientes: cobrando una tarifa de $5")
        self.balance -= monto
        return self
    
    def mostrar_info_cuenta(self):
        print(f"Balance: ${self.balance}")
        return self

    def generar_interés(self): 
        if self.balance > 0:
            self.balance += (self.balance * self.tasa_interes)
        return self

    # @classmethod
    # def instancias_cuenta_bancaria(cls):
    #     print(
    #         f"Bienvenido, esta es la información de tu cuenta bancaria:\n"
    #         f"Balance: {cls.balance}\n"
    #         f"Tasa de interés: {cls.tasa_interes}")

cuenta1 = CuentaBancaria(1000, 0.01)
cuenta2 = CuentaBancaria(500, 0.01)

cuenta1.deposito(100).deposito(100).deposito(100).retiro(100).generar_interés().mostrar_info_cuenta()

cuenta2.deposito(250).deposito(250).retiro(100).retiro(100).retiro(100).retiro(100).generar_interés().mostrar_info_cuenta()


# cuenta1.instancias_cuenta_bancaria()


