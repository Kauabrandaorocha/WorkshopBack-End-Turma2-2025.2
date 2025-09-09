#O código abaixo tenta acessar uma chave que não existe no dicionário e ainda pede uma entrada do usuário.

# dados = {
#   "nome": "Isaac ",
#   "idade": 25,
#   "cidade": "São Paulo"
#}

#chave = input("Digite a chave que deseja acessar: ")

#print(f"O valor da chave '{chave}' é: {dados[chave]}")

#Código corrigido

try:
    dados = {
    "nome": "Isaac",
    "idade": 25,
    "cidade": "São Paulo"
    }

    chave = input("Digite a chave que deseja acessar: ")

    print(f"O valor da chave '{chave}' é: {dados[chave]}")

except KeyError:
    dados.get(chave)
    print("Erro: Endereço de chave inválido!")
    