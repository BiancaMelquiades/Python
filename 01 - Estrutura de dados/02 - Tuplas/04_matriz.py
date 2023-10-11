# a tupla aninhada = lista objeto (matriz)
matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

# recupera o valor da linha
print(matriz[0])  # (1, "a", 2)

# recupera o valor de um elemento (linha + coluna)
print(matriz[0][0])  # 1

# recupera pelo final (negativo)
print(matriz[0][-1])  # 2
print(matriz[-1][-1])  # "c"
