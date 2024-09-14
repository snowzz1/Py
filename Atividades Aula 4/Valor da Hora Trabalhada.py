# Solicita o turno de trabalho e a quantidade de horas trabalhadas
turno = input("Digite o turno de trabalho (N para Noturno ou qualquer outro caractere para Diurno): ").upper()
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))

# Verifica o valor da hora de acordo com o turno
if turno == 'N':
    valor_hora = 45.00
else:
    valor_hora = 37.50

# Calcula o salário
salario = valor_hora * horas_trabalhadas

# Mostra o resultado
print(f"O valor do salário é: R$ {salario:.2f}")
