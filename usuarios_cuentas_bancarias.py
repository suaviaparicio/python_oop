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
        return self.balance
    
    def mostrar_info_cuenta(self):
        return f"Balance: ${self.balance}"

    def generar_interes(self): 
        if self.balance > 0:
            self.balance += (self.balance * self.tasa_interes)


class Usuario:

    def __init__(self, nombre):
        self.nombre = nombre
        self.cuenta = CuentaBancaria(balance=0, tasa_interes=0.02)
    
    def hacer_deposito(self, monto):
        self.cuenta.deposito(monto)
        return self
    
    def hacer_retiro(self, monto):
        self.cuenta.retiro(monto)
        return self

    def mostrar_balance(self):
        print(f"la persona {self.nombre} tiene un {self.cuenta.mostrar_info_cuenta()}")

    def transferir_dinero(self, otro_usuario, monto):
        if type(otro_usuario) is not Usuario:
            print("El usuario no es válido")
            return
        if self.cuenta.mostrar_info_cuenta < monto:
            print("Saldo insuficiente")
            return
        self.hacer_retiro(monto) 
        otro_usuario.hacer_deposito(monto)


miguel = Usuario("miguel")
miguel.hacer_deposito(1000).hacer_deposito(200).hacer_retiro(100).mostrar_balance()

matias = Usuario("matias")
matias.hacer_deposito(2000).hacer_deposito(100).hacer_retiro(100).mostrar_balance()

marcela = Usuario("marcela")
marcela.hacer_deposito(500).hacer_deposito(700).hacer_retiro(200).mostrar_balance()

# cuenta1 = CuentaBancaria(1000, 0.01)
# cuenta2 = CuentaBancaria(500, 0.01)




