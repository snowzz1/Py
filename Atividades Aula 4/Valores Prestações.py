# Solicita ao usuário os valores necessários
valorPrestacao = float(input("Digite o valor da prestação: "))
multa = float(input("Digite a porcentagem de multa por dia de atraso: "))
qtdeDias = int(input("Digite a quantidade de dias de atraso: "))

# Calcula o valor da prestação com a multa
prestacao = valorPrestacao + (valorPrestacao * (multa / 100) * qtdeDias)

# Mostra o valor da prestação atualizado
print(f"O valor da prestação atualizada é: R$ {prestacao:.2f}")
