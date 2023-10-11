# gerar uma lista a partir de uma existente

# Filtrar lista
numeros = [1, 30, 21, 2, 9, 65, 34]
# pares = [retorno for interação in filtro if condição do filtro], só é obrigatório o retorno e a interação
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

# Modificar valores
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero ** 2 for numero in numeros]
print(quadrado)
