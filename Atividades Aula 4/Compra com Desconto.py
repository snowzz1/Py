# Solicita o valor da compra
valor_compra = float(input("Digite o valor da compra: R$ "))

# Verifica se a compra é elegível para desconto
if valor_compra > 200:
    desconto = valor_compra * 0.20
    valor_final = valor_compra - desconto
    print(f"Você recebeu um desconto de 20%. O valor final da compra é: R$ {valor_final:.2f}")
else:
    print(f"Não há desconto. O valor da compra é: R$ {valor_compra:.2f}")
