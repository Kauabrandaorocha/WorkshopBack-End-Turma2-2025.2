class Zoologico:
    
    def __init__(self):
        self.animais = []
        pass

    def adicionarAnimal(self, animal):
        self.animais.append(animal)

    def  listarAnimais(self):
        for animal in self.animais:
            print(animal.apresentar)

    def filtrarPorTipo(self):
        for animal in self.animais:
            if isinstance(animal, Animal):
                print(animal.apresentar())

    
class Animal:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        pass

    def falar(self):    
        return "Sons dos animais"

    def apresentar(self):
        return f" O nome do animal é {self.nome} e sua idade é {self.idade}, ele diz: {self.falar()}"


class Gato(Animal):

    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        pass

    def falar(self):    
        return "Miau"
    

class Cachorro(Animal):

    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        pass

    def falar(self):
        return "Au Au"
    

class Vaca(Animal):

    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        pass

    def falar(self):
        return "Muuu"

zoo = Zoologico()
zoo.adicionarAnimal(Gato("Maggie", 4))
zoo.adicionarAnimal(Cachorro("Rex", 4))
zoo.adicionarAnimal(Vaca("Mimosa", 5))

print("Todos os animais:")
zoo.listarAnimais()

print("\nAnimais do tipo Animal:")
zoo.filtrarPorTipo()