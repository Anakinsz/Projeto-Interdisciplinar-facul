def conversao_decimal_para_binario(decimal):
    if decimal == 0:
        return "0"

    binario = ""
    while decimal > 0:
        resto = decimal % 2
        binario = str(resto) + binario
        decimal //= 2