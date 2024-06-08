class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def get_nome(self):
        return self.nome
    
    def get_idade(self):
        return self.idade
    
    def set_nome(self, nome):
        self.nome = nome
    
    def set_idade(self, idade):
        self.idade = idade

# Teste da classe
pessoa1 = Pessoa("João", 25)
print(pessoa1.get_nome())  # Saída: João
print(pessoa1.get_idade())  # Saída: 25
