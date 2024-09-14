def calcular_volume_tronco_piramide(h, Bmaior, Bmenor):
    volume = (h / 3) * (Bmaior**2 + Bmenor**2 + (Bmaior * Bmenor)**0.5)
    return volume

h = float(input("Digite a altura do tronco da pirâmide (h): "))
Bmaior = float(input("Digite o valor da base maior (Bmaior): "))
Bmenor = float(input("Digite o valor da base menor (Bmenor): "))

volume = calcular_volume_tronco_piramide(h, Bmaior, Bmenor)

print(f"O volume do tronco da pirâmide é: {volume:.2f}")
