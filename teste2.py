# Aqui estou criando a função principal para gerar a sequência de Fibonacci
def fibonacci(n):
    fib_sequence = [0, 1]
    while fib_sequence[-1] < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Aqui estou criando a função para verificar se o número pertence à sequência de Fibonacci
def pertence_a_fibonacci(n): 
    fib_sequence = fibonacci(n)
    if n in fib_sequence:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} não pertence à sequência de Fibonacci."

#  E por ultimo, estou pedindo para o usuário digitar um número e o comando print para exibir o resultado se é ou não um numero da sequência de Fibonacci
numero = int(input("Informe um número: "))
resultado = pertence_a_fibonacci(numero)
print(resultado)
