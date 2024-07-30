#Crie uma classe Produto com os atributos nome e preco. 
#Em seguida, crie uma classe Estoque que gerencie uma lista de produtos, permitindo adicionar e remover produtos, além de calcular o valor total do estoque.

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
class Estoque:
    def __init__(self):
        self.produtos = []
    
    def adicionar_produto(self, produto):
        self.produtos.append(produto)
    
    def remover_produto(self, produto):
        self.produtos.remove(produto)
    
    def calcular_valor_total(self):
        return sum(produto.preco for produto in self.produtos)

# Teste das classes
produto1 = Produto("Arroz", 20)
produto2 = Produto("Feijão", 10)
estoque = Estoque()
estoque.adicionar_produto(produto1)
estoque.adicionar_produto(produto2)
print(estoque.calcular_valor_total())  # Saída: 30
    
