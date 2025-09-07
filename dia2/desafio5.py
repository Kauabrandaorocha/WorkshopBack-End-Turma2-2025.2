class Animal:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        pass

    def falar(self):
        return "Vozes dos animais"

    def apresentar(self):
        return f"Nome: {self.nome}\nIdade: {self.idade}"


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
    
recebeClasse = Gato(str(input("Digite o nome do gato: ")), int(input("Digite a idade dele: ")))
recebeMetodo = recebeClasse.apresentar()
recebeMetodo2 = recebeClasse.falar()

print(recebeMetodo)
print(recebeMetodo2)

recebeClasse = Cachorro(str(input("Digite o nome do cachorro: ")), int(input("Digite a idade dele: ")))
recebeMetodo = recebeClasse.apresentar()
recebeMetodo2 = recebeClasse.falar()

print(recebeMetodo)
print(recebeMetodo2)