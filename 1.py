def pertence_fibonacci(num):
    if num < 0:
        return False
    a, b = 0, 1
    while a < num:
        a, b = b, a + b
    
    return a == num

def main():
    try:
        numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
        if pertence_fibonacci(numero):
            print("O número {} pertence à sequência de Fibonacci.".format(numero))
        else:
            print("O número {} não pertence à sequência de Fibonacci.".format(numero))
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

if __name__ == "__main__":
    main()
