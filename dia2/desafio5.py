class Animal:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        pass

    def falar():
        return "Vozes dos animais"

    def apresentar(self):
        return f"Nome: {self.nome} \n Idade: {self.idade}"


class Gato(Animal): 
    
    def __init__ (self, nome, idade):
        super().__init__(nome, idade)
        
    def falar(self):
        return "Miau"

class Cachorro(Animal):

    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def falar(self):
        return "Au Au"