#This code defines a function to get a range of values from the user then, prints the prime numbers in that range.
#The code also checks the number of divisions made to determine the prime numbers.

def eh_primo(n):
    global total_divisoes  # Permite acessar a variável fora da função
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        total_divisoes += 1  # Conta cada tentativa de divisão
        if n % i == 0:
            return False
    return True

# Entrada do usuário
limite = int(input("Insira um número inteiro N para encontrar os primos entre 1 e N: "))

primos = []
total_divisoes = 0  # Contador global de divisões

# Verifica todos os números de 2 até N
for numero in range(2, limite + 1):
    if eh_primo(numero):
        primos.append(numero)

# Saída dos resultados
print(f"Números primos entre 1 e {limite}: {primos}")
print(f"Total de divisões executadas: {total_divisoes}")

# This code defines a function to get a range of values from the user,
# then prints the prime numbers in that range.