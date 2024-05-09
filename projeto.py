#Projeto Interdisciplinar, apresentar estrutura com menu é possibilidade de escolha da função desejada, utilizar conceitos de sistemas de numeração, conversão entre base aritmética binária com inteiros.

n = int(input("Digite um número inteiro: "))
print('''Escolha uma função para base de conversão:  
[1] conversão para Binário
[2] conversão para Octal
[3] conversão para hexadecimal
[4] conversão para Sair''')


def decimal_para_binario(decimal):
    if decimal == 0:
        return "0"

    binario = ""
    while decimal > 0:
        resto = decimal % 2
        binario = str(resto) + binario
        decimal //= 2

    return binario

numero_decimal = int(input("Digite o número decimal a ser convertido: "))
resultado_binario = decimal_para_binario(numero_decimal)
print( "O número decimal", "em binário é:",resultado_binario)