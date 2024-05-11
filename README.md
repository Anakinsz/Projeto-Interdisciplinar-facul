Documentação do Projeto

Descrição do Software
O software desenvolvido é uma aplicação de conversão de números decimais para outras bases numéricas, como binário, octal e hexadecimal. Ele oferece um menu de seleção que permite ao usuário escolher a base para a qual deseja converter o número decimal inserido.

Finalidade
A finalidade deste software é fornecer uma ferramenta simples e intuitiva para a conversão de números decimais em outras bases numéricas.
Funcionalidades
O software oferece as seguintes funcionalidades:
1. Conversão de números decimais para binário.
2. Conversão de números decimais para octal.
3. Conversão de números decimais para hexadecimal.
4. Opção para sair do programa.
5. menu intuitivo

Solução Implementada
O software utiliza um loop principal para apresentar um menu de opções ao usuário. Com base na escolha do usuário, o programa chama a função correspondente para realizar a conversão do número decimal inserido para a base numérica desejada. As funções de conversão implementadas são:

- decimal_para_binario(decimal)`: Converte um número decimal para binário.
- decimal_para_octal(decimal)`: Converte um número decimal para octal.
- decimal_para_hexadecimal(decimal)`: Converte um número decimal para hexadecimal.

Cada uma dessas funções utiliza algoritmos específicos para realizar a conversão de acordo com as regras de cada sistema numérico.

Print de Trechos de Códigos
python
while True:
    n = int(input('''Escolha uma função para base de conversão: 
    [1] Conversão para Binário
    [2] Conversão para Octal
    [3] Conversão para Hexadecimal
    [4] Sair
    '''))

    if n == 1:
        # Função de conversão para binário

    elif n == 2:
        # Função de conversão para octal

    elif n == 3:
        # Função de conversão para hexadecimal

    elif n == 4:
        print("Encerrando o programa")
        break

    else:
        print("Escolha inválida.")

Fundamentação Teórica
O projeto utiliza conceitos de sistemas de numeração, conversão entre bases aritméticas binárias e algoritmos para implementar as funções de conversão. Esses conceitos são fundamentais para entender a representação de números em diferentes sistemas numéricos e para realizar operações de conversão entre eles.

Conclusão
O software desenvolvido oferece uma solução prática e eficiente para a conversão de números decimais em outras bases numéricas. Ele incorpora conceitos teóricos de sistemas de numeração e algoritmos de conversão, proporcionando uma experiência educativa e funcional para os usuários.


FEITO PELO: 
NATHAN SILVA DA COSTA 
RGM: 37291742
