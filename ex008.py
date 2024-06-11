#Crie uma classe Veiculo com atributos marca e modelo. 
#Em seguida, crie uma classe Carro que herde de Veiculo e adicione o atributo num_portas. 
#Implemente métodos para exibir informações do carro.

class Veiculo:
    def __init__(self, marca, modelo):#acertei 
        self.marca = marca
        self.modelo = modelo

class Carro(Veiculo): #acertei
    def __init__(self, marca, modelo, num_portas):
        super().__init__(marca, modelo)
        self.num_portas = num_portas #duvida1: devo colocar essa a classe filho dentro da classe pai? R: nao
        
    def mostrar_dados(self): #duvida1: devo colocar esse metodo dentro da classe carrp? R: Sim
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Número de portas: {self.num_portas}"

carro1 = Carro("toyota", "hilux", "4") #Errei, aqui eu deveria ter chamado a classe filha (Carro("hilux, toyota"))

print(carro1.mostrar_dados())


    
