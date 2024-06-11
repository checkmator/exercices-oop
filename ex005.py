#Crie uma classe ContaBancaria com os atributos numero, titular e saldo. 
#Inclua métodos para depositar e sacar dinheiro, além de consultar o saldo.

class ContaBancaria:
    def __init__(self, numero, titular, saldo = 0): #acertei
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")

    def consultar(self): #acertei
        return self.saldo 
    
    #fim

# Teste da classe
conta1 = ContaBancaria("12345-6", "Maria", 1000)
conta1.depositar(500)
conta1.sacar(200)
print(conta1.consultar())  # Saída: 1300








