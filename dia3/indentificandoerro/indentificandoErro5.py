#O código abaixo pode gerar vários tipos de erro dependendo da entrada do usuário.

def dividir(a, b):
    return a / b
try:
    num1 = input("Digite o primeiro número: ")
    num2 = input("Digite o segundo número: ")

    resultado = dividir(int(num1), int(num2))
    print(f"Resultado: {resultado}")

except ValueError:
    print("Erro: Número inválido!")

except ZeroDivisionError:
    print("Erro: 0 não pode ser dividido!")