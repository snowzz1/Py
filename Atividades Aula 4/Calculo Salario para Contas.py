# Solicita os valores das contas e do salário
conta_agua = float(input("Digite o valor da conta de água: R$ "))
conta_luz = float(input("Digite o valor da conta de luz: R$ "))
conta_telefone = float(input("Digite o valor da conta de telefone: R$ "))
salario = float(input("Digite o valor do salário: R$ "))

# Calcula o total das contas
total_contas = conta_agua + conta_luz + conta_telefone

# Verifica se o salário é suficiente para pagar as contas
if salario >= total_contas:
    salario_restante = salario - total_contas
    print(f"Salário suficiente. O valor restante após pagar as contas é: R$ {salario_restante:.2f}")
else:
    print("Salário insuficiente!")
