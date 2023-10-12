def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

# formas de chamar a função:

# se atenta a ordem informada, não pode inverter
salvar_carro("Fiat", "Palio", 1999, "ABC-1234")

# declara um a um/nomeado (ne modificar o nome do argumento, dará erro)
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")

# está passando um dicionário para a função
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})
