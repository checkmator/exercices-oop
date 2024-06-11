#Crie uma classe ContaBancaria com os atributos numero, titular e saldo. 
#Inclua métodos para depositar e sacar dinheiro, além de consultar o saldo.

class ContaBancaria:
    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        return self.saldo + valor

    def sacar(self, valor):
        return self.saldo - valor

    def consultar(self):
        return self.saldo









