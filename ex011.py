#Crie uma classe Produto com os atributos nome e preco. 
#Em seguida, crie uma classe Estoque que gerencie uma lista de produtos, permitindo adicionar e remover produtos, além de calcular o valor total do estoque.

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    