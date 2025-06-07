#This code checks if the entered number isis prime or not

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numero = int(input('Insira um número para saber se ele é primo: '))

if is_prime(numero):
    print('O número escolhido é primo!')
else:
    print('O número escolhido não é primo!')