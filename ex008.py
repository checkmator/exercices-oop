#Crie uma classe Veiculo com atributos marca e modelo. 
#Em seguida, crie uma classe Carro que herde de Veiculo e adicione o atributo num_portas. 
#Implemente métodos para exibir informações do carro.

class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

class Carro(Veiculo): #duvida1: devo colocar essa a classe filho dentro da classe pai? 
    def __init__(self, marca, modelo, num_portas):
        super().__init__(marca, modelo)
        self.num_portas = num_portas

def mostrar_dados(self): #duvida1: devo colocar esse metodo dentro da classe veiculo
    print(self.marca)

carro1 = Carro(Veiculo("hilux","toyota"))

carro1.mostrar_dados()


    
