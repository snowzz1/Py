# Solicitar os valores ao usuário
h = float(input("Digite a altura do tronco da pirâmide (h): "))
Bmenor = float(input("Digite o valor da base menor (Bmenor): "))
Bmaior = float(input("Digite o valor da base maior (Bmaior): "))

# Calcular o volume do tronco da pirâmide
volume = (h/3) * (Bmaior**2 + Bmenor**2 + (Bmaior**2 * Bmenor**2)**0.5)

# Mostrar o resultado
print(f"O volume do tronco da pirâmide é: {volume:.2f}")
