#Crie uma classe Retangulo que tenha atributos largura e altura e métodos para calcular a área e o perímetro do retângulo.

class Retangulo:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def area(self):
        return self.altura*self.largura
    
    def perimetro(self):
        return (self.altura*self.largura)*2
        
retangulo1 = Retangulo(30,60)
perimetro1 = Retangulo(55, 89)

print(retangulo1.area())
print(perimetro1.perimetro())
