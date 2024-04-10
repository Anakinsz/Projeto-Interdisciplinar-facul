n1 = int(input("coloque o primeiro número: "))
n2 = int(input("coloque o segundo número: "))
n3 = int(input("coloque o terceiro número: "))

if   n1 > n2 and n3:
    print("o primeiro número é o maior.")
elif n2 > n3 and n1:
    print("o segundo número é o maior. ")
elif n3 > n1 or n2:
    print ("o terceiro número é o maior. ")
else:
    print("nenhum número")