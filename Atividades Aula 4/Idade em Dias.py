# Solicita a idade em anos ao usuário
idade_anos = int(input("Digite sua idade em anos: "))

# Converte a idade para dias e meses
idade_em_dias = idade_anos * 365
idade_em_meses = idade_anos * 12

# Mostra o resultado
print(f"Sua idade é aproximadamente {idade_em_dias} dias ou {idade_em_meses} meses.")
