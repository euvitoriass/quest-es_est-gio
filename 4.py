# Sequência a): 1, 3, 5, 7, ___
# Lógica: Números ímpares consecutivos
ultimo_numero_a = 7
proximo_elemento_a = ultimo_numero_a + 2

# Sequência b): 2, 4, 8, 16, 32, 64, ____
# Lógica: Potências de 2
ultimo_numero_b = 64
proximo_elemento_b = ultimo_numero_b * 2

# Sequência c): 0, 1, 4, 9, 16, 25, 36, ____
# Lógica: Quadrados perfeitos
n = 7  # O próximo número após 36 é o quadrado de 7
proximo_elemento_c = n ** 2

# Sequência d): 4, 16, 36, 64, ____
# Lógica: Quadrados perfeitos de números pares
proximo_elemento_d = 10 ** 2  # Próximo número após 64 é o quadrado de 10

# Sequência e): 1, 1, 2, 3, 5, 8, ____
# Lógica: Sequência de Fibonacci
a, b = 8, 13  # Últimos dois números da sequência
proximo_elemento_e = a + b

# Sequência f): 2, 10, 12, 16, 17, 18, 19, ____
# Lógica: Sequência com padrão irregular
proximo_elemento_f = 19 + 1  # Próximo número após 19 é 20

# Exibindo os resultados
print("Próximo elemento da sequência a): {}".format(proximo_elemento_a))
print("Próximo elemento da sequência b): {}".format(proximo_elemento_b))
print("Próximo elemento da sequência c): {}".format(proximo_elemento_c))
print("Próximo elemento da sequência d): {}".format(proximo_elemento_d))
print("Próximo elemento da sequência e): {}".format(proximo_elemento_e))
print("Próximo elemento da sequência f): {}".format(proximo_elemento_f))
