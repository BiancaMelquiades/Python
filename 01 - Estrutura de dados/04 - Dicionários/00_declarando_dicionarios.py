# o dicionário é um conjunto não ordenado de pares chave:valor, onde as chaves não são únicas
# são delimitados por chaves {} e para ser válido precisa conter uma lista ou uma tupla ou o dict
#  a chave deve ser imutável

# biblioteca = {"chave": xx. "chave": xx}
pessoa = {"nome": "Guilherme", "idade": 28}
print(pessoa)

# biblioteca = contrutor dict(parâmetro="", parâmetro="")
pessoa = dict(nome="Guilherme", idade=28)
print(pessoa)

# quando já tem um dicionário criado e precisa incluir uma nova
pessoa["telefone"] = "3333-1234"  # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}
print(pessoa)
