# Houve uma confusão/Erro de tipagem na hora de declarar os parâmetros fora da função e o usuário declarou o '5' como uma string, onde não é possível realizar operações no python entre inteiros e strings (TypeError)
# def somar(a, b):
    #return a + b

# resultado = somar(10, "5")
# print(resultado)

# Código corrigido
def somar(a, b):
    return a + b

try:
    resultado = somar(10, "5")
except TypeError:
    print("Erro: Você está digitando um número inválido!")
except ZeroDivisionError:
    print("Erro: Não é possível realizar divisão por 0")