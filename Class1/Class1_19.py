#This code's going to check if the entered number is prime or not
#and
#if it's not prime, gonna print it's respective divisors

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

numero = int(input('Insira um número para saber se ele é primo: '))
if is_prime(numero):
    print('O número escolhido é primo!')
else:
    print('O número escolhido não é primo!')
    divisors = get_divisors(numero)
    print(f'Os divisores de {numero} são: {divisors}')

# This code checks if the entered number is prime or not
# and if it's not prime, it prints its respective divisors.