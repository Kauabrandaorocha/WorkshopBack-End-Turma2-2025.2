import math

def numeroReal(numero):
    valorArredondadoBaixo = math.floor(numero)
    valorArredondadoCima= math.ceil(numero)
    valorInteiroProximo = round(numero)

    return valorArredondadoBaixo, valorArredondadoCima, valorInteiroProximo

numero = numeroReal(float(input("Digite um número: ")))
print(numero)

