#Crie uma classe Livro com os atributos titulo, autor e preco. 
#Adicione um método para aplicar um desconto ao preço do livro.

class Livro:
    def __init__(self, titulo, autor, preco=0):
        self.titulo = titulo
        self.autor = autor
        self.preco = preco

    def aplicar_desconto(self,percentual):
        valor_final = self.preco - (percentual/100)
        return valor_final
    
livro1 = Livro("ex007.py", "jpg", 100)
livro1.aplicar_desconto(10)
