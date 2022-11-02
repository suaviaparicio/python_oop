class Usuario:

    def __init__(self, nombre, balance):
        self.balance = balance
        self.nombre = nombre
    
    def hacer_deposito(self, monto):
        self.balance += monto
        return self
    
    def hacer_retiro(self, monto):
        self.balance -= monto
        return self

    def mostrar_balance(self):
        print(f"la persona {self.nombre} tiene ${self.balance}")

    def transferir_dinero(self, otro_usuario, monto):
        if type(otro_usuario) is not Usuario:
            print("El usuario no es válido")
            return self
        if self.balance < monto:
            print("Saldo insuficiente")
            return self
        self.hacer_retiro(monto) 
        otro_usuario.hacer_deposito(monto)
        return self

mati = Usuario("Matias Jose", 2000)
mati.hacer_deposito(500).hacer_deposito(500).hacer_deposito(500).hacer_retiro(80).mostrar_balance()

miguel = Usuario("Miguel Baquero", 1000)
miguel.hacer_deposito(500).hacer_deposito(100).hacer_retiro(80).hacer_retiro(200).mostrar_balance()

marcela = Usuario("Marcela Alvarez", 0)
marcela.hacer_deposito(1000).hacer_retiro(80).hacer_retiro(100).hacer_retiro(20).mostrar_balance()

mati.transferir_dinero(marcela, 100).mostrar_balance()
marcela.mostrar_balance()