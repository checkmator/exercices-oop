#Crie uma classe Cachorro com os atributos nome, idade e raca. 
#Adicione métodos para exibir as informações do cachorro e calcular a idade do cachorro em anos humanos 
#(multiplique a idade do cachorro por 7).

class Cachorro:
    def __init__(self, nome, idade, raca):
        self.nome = nome
        self.idade = idade
        self.raca = raca

    def calcular_idade(self):
        idade_humano = self.idade*7
        return idade_humano

    def exibir_infos(self):
        return f"Nome: {self.nome}, Idade: {self.idade},Idade em anos humanos: {}, raca: {self.raca}"

dog1 = Cachorro("Perola", 2, "vira lata")

print(dog1.calcular_idade())
print(dog1.exibir_infos())

