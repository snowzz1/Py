a = int(input("Digite o Valor de A: "))
b = int(input("Digite o Valor de B: "))
c = int(input("Digite o Valor de C: "))

if a > b and c > b:
    print("O menor Valor é o B!")

elif a < b and c > a:
    print("O menor Valor é o A")

else:
    print("O menor Valor é o C")