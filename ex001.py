class Dog:
    def __init__(self, name, age):
        self.name = name  
        self.age = age    

    def bark(self):
        print("Woof!")   

name = input("Digite o nome do cachorro: ")
age = int(input("Digite a idade do cachorro: "))

dog = Dog(name, age)

print(f"Nome: {dog.name}")  
print(f"Idade: {dog.age}")  
dog.bark()  