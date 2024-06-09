#Crie uma classe Retangulo que tenha atributos largura e altura e métodos para calcular a área e o perímetro do retângulo.

class Retangulo:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def area(self):
        return self.altura*self.largura
        
retangulo1 = Retangulo(30,60)

print(retangulo1.area())
