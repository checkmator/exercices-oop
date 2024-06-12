#Crie uma classe ContaCorrente e uma classe ContaPoupanca que herdem de ContaBancaria (do exercício 5). 
#Adicione um método para aplicar juros à ContaPoupanca.
class ContaBancaria:
    def __init__(self, numero, titular, saldo = 0): 
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

    def consultar(self): 
        return self.saldo 
class ContaCorrente(ContaBancaria):
        pass

class ContaPoupanca(ContaBancaria):
    def aplicar_juros(self, taxa):
        self.saldo += self.saldo * (taxa / 100)

# Teste das classes
conta_corrente1 = ContaCorrente("12345-6", "João", 1500)
conta_poupanca1 = ContaPoupanca("65432-1", "Ana", 2000)

conta_poupanca1.aplicar_juros(5)
print(conta_poupanca1.consultar_saldo())  # Saída: 2100.0

