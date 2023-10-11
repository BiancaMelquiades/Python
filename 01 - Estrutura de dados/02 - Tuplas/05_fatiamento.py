# forma de repassar o valor em partes ou acessar um conjunto de elementos
tupla = ("p", "y", "t", "h", "o", "n",)

#  da posição 2 até o final
print(tupla[2:])  # ("t", "h", "o", "n")

# do inicio ao elemento anterior à ultima posicao (posição -1)
print(tupla[:2])  # ("p", "y")

# considera o inicial e o final
print(tupla[1:3])  # ("y", "t")

# inicial, final e step
print(tupla[0:3:2])  # ("p", "t")

# cópia da string
print(tupla[::])  # ("p", "y", "t", "h", "o", "n")

#  cópia ao contrário
print(tupla[::-1])  # ("n", "o", "h", "t", "y", "p")
