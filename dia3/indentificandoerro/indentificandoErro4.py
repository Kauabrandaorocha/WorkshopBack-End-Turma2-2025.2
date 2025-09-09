#Código está correto, mas permite o usuário digitar índices inexistentes, dando erro na aplicação

# numeros = [10, 20, 30]
# indice = int(input("Digite um índice para acessar a lista: "))

# print(numeros[indice])

#Código melhorado
while True:
    try:
        numeros = [10, 20, 30]
        indice = int(input("Digite um índice para acessar a lista: "))

        print(numeros[indice])
    
    except IndexError:
        print("Erro: Número de índice digitado fora de escopo")
        
    resp = str(input("Quer continuar? [S/N]"))

    if resp == 'n':
        break
