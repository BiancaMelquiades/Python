#  método para copiar a lista/ repetir a lista com instância diferente
# uma não reflete na outra

lista = [1, "Python", [40, 30, 20]]

l2 = lista.copy()

print(lista)  # [1, "Python", [40, 30, 20]]

print(id(l2), id(lista))

# exemplo de modificação
l2[0] = 'j'
print("Lista original: ", l2)
print("Depois da alteracao: ", lista)
