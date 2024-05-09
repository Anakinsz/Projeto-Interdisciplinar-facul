#Projeto Interdisciplinar, apresentar estrutura com menu é possibilidade de escolha da função desejada, utilizar conceitos de sistemas de numeração, conversão entre base aritmética binária com inteiros.

while True:
    n = int(input('''Escolha uma função para base de conversão: 
    [1] Conversão para Binário
    [2] Conversão para Octal
    [3] Conversão para Hexadecimal
    [4] Sair
    '''))

    if n == 1:
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
        print("O número decimal", numero_decimal, "em binário é:", resultado_binario)

    elif n == 2:
        def decimal_para_octal(decimal):
            if decimal == 0:
                return "0"

            octal = ""
            while decimal > 0:
                resto = decimal % 8
                octal = str(resto) + octal
                decimal //= 8

            return octal

        numero_decimal = int(input("Digite o número decimal a ser convertido: "))
        resultado_octal = decimal_para_octal(numero_decimal)
        print("O número decimal", numero_decimal, "em octal é:", resultado_octal)

    elif n == 3:
        def decimal_para_hexadecimal(decimal):
            if decimal == 0:
                return "0"

            caracteres_hexadecimais = "0123456789ABCDEF"
            hexadecimal = ""
            while decimal > 0:
                resto = decimal % 16
                hexadecimal = caracteres_hexadecimais[resto] + hexadecimal
                decimal //= 16

            return hexadecimal

        numero_decimal = int(input("Digite o número decimal a ser convertido: "))
        resultado_hexadecimal = decimal_para_hexadecimal(numero_decimal)
        print("O número decimal", numero_decimal, "em hexadecimal é:", resultado_hexadecimal)

    elif n == 4:
        print("Encerrando o programa")
        break

    else:
        print("Escolha inválida.")
