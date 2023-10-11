# acessa valores do dicionário, localiza uma chave existente
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# contatos["chave"]  # KeyError

# se não encontrar a chave, retorna "none"
resultado = contatos.get("chave")  # None
print(resultado)

# se não encontrar, retorna o dicionário vazio
resultado = contatos.get("chave", {})  # {}
print(resultado)

# se encontrar, não retorna o diiconário vazio, respeita a chave existente
resultado = contatos.get(
    "guilherme@gmail.com", {}
)  # {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
print(resultado)
