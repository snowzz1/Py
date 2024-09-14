import math

# Solicita o valor do ângulo em graus
graus = float(input("Digite o valor do ângulo em graus: "))

# Converte o ângulo de graus para radianos
radianos = math.radians(graus)

# Calcula o seno, cosseno e tangente
seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)

# Mostra os resultados
print(f"Seno de {graus}°: {seno:.4f}")
print(f"Cosseno de {graus}°: {cosseno:.4f}")
print(f"Tangente de {graus}°: {tangente:.4f}")
