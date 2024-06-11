#Crie uma classe Funcionario com os atributos nome, salario e cargo. 
#Inclua métodos para obter um aumento de salário e exibir as informações do funcionário.

class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
    
    def aumento_salario(self, salario, aumento):
        salario_final = (self.salario + aumento)
        print(salario_final)


dados = Funcionario("joao", 1000, "adm")

dados.aumento_salario(1000, 500)
