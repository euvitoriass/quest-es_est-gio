# Solicita ao usuário que insira uma string
texto = str(input("Digite uma string para verificar a presença da letra a: "))

# Converte a string para minúsculas para facilitar a contagem
texto = texto.lower()

# Conta o número de vezes que a letra a aparece
quantidade_a = texto.count('a')

# Verifica se a letra a está presente na string
existe_a = quantidade_a > 0

# Exibe o resultado
if existe_a:
    print("A letra 'a' aparece {} vez(es) na string.".format(quantidade_a))
else:
    print("A letra 'a' não está presente na string.")
