# Fibo

def verifica_fibonacci(numero):
    a, b = 0, 1
    while b <= numero_informado:
        if b == numero_informado:
            return True
        a, b = b, a + b
    return False

numero_informado = int(input("Insira um número para descobrir se ele pertence à sequência de Fibonacci: "))

if verifica_fibonacci(numero_informado):
    print(f"O número {numero_informado} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero_informado} não pertence à sequência de Fibonacci.")
