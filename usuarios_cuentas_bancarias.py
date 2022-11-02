import usuarios_cuentas_bancarias_bonus2 as CuentaBancaria

class Usuario:

    def __init__(self, nombre, cuenta):
        self.nombre = nombre
        # self.tipo_cuenta = tipo_cuenta
        self.cuenta = cuenta
    
    def hacer_deposito(self, monto):
        self.cuenta.deposito += monto
    
    def hacer_retiro(self, monto):
        self.cuenta.retiro -= monto

    def mostrar_balance(self):
        print(f"la persona {self.nombre} tiene un {self.cuenta.mostrar_info_cuenta}")

    def transferir_dinero(self, otro_usuario, monto):
        if type(otro_usuario) is not Usuario:
            print("El usuario no es válido")
            return
        if self.cuenta.mostrar_info_cuenta < monto:
            print("Saldo insuficiente")
            return
        self.hacer_retiro(monto) 
        otro_usuario.hacer_deposito(monto)

cuenta = CuentaBancaria(1000, 0.01)
print (cuenta.deposito(100))
# miguel = Usuario("miguel", CuentaBancaria(balance=0, tasa_interes=0.02))
# matias = Usuario("matias")
# marcela = Usuario("marcela")


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




