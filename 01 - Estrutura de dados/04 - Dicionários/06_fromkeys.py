# cria chaves em 2 situações
# pode ser um dicionário existente ou não

# apenas criar as chaves, sem valor
resultado = dict.fromkeys(["nome", "telefone"])  # {"nome": None, "telefone": None}
print(resultado)

# cria um conjunto de chaves com valor padrão
resultado = dict.fromkeys(["nome", "telefone"], "vazio")  # {"nome": "vazio", "telefone": "vazio"}
print(resultado)
