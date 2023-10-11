# conjuntos em python não suportam indexiação e nem fatiamento
# é necessário converter o SET em LISTA
numeros = {1, 2, 3, 2}

numeros = list(numeros)

print(numeros[0])
