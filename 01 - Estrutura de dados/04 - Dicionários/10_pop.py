# remove uma chave do dicionário (remove e retorna o valor que removeu)

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.pop("guilherme@gmail.com")  # {'nome': 'Guilherme', 'telefone': '3333-2221'}
print(resultado)

# caso ele não encontre, ele retorna o valor do segundo argumento
resultado = contatos.pop("guilherme@gmail.com", {})  # {}
print(resultado)
