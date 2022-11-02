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
    
    def mostrar_info_cuenta(self):
        print(f"Balance: ${self.balance}")

    def generar_interés(self): 
        if self.balance > 0:
            self.balance += (self.balance * self.tasa_interes)



# cuenta1 = CuentaBancaria(1000, 0.01)
# cuenta2 = CuentaBancaria(500, 0.01)




