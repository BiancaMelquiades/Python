# o dicionário é muito parecido com um banco de dados
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

# acessar a chave do dicionário por níveis
telefone = contatos["giovanna@gmail.com"]["telefone"]  # "3443-2121"
print(telefone)
