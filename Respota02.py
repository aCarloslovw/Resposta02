# Função para calcular a sequência de Fibonacci e verificar se um número pertence a ela
def fibonacci_check(num):
    # Inicializando os primeiros valores da sequência de Fibonacci
    a, b = 0, 1
    fibonacci_sequence = [a, b]  # Armazena a sequência de Fibonacci

    # Gerar a sequência até que o próximo valor seja maior ou igual ao número informado
    while b < num:
        a, b = b, a + b
        fibonacci_sequence.append(b)

    # Exibir a sequência gerada
    print(f"Sequência de Fibonacci gerada: {fibonacci_sequence}")

    # Verificar se o número informado pertence à sequência
    if num in fibonacci_sequence:
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} NÃO pertence à sequência de Fibonacci."

# Definir o número que queremos verificar
numero = 21  # Pode ser alterado ou informado de outra forma

# Chamar a função e exibir o resultado
resultado = fibonacci_check(numero)
resultado
