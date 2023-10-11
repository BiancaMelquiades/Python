# forma de repassar o valor em partes ou acessar um conjunto de elementos
lista = ["p", "y", "t", "h", "o", "n"]

#  da posição 2 até o final
print(lista[2:])  # ["t", "h", "o", "n"]

# do inicio ao elemento anterior à ultima posicao (posição -1)
print(lista[:2])  # ["p", "y"]

# considera o inicial e o final
print(lista[1:3])  # ["y", "t"]

# inicial, final e step
print(lista[0:3:2])  # ["p", "t"]

# cópia da string
print(lista[::])  # ["p", "y", "t", "h", "o", "n"]

#  cópia ao contrário
print(lista[::-1])  # ["n", "o", "h", "t", "y", "p"]
