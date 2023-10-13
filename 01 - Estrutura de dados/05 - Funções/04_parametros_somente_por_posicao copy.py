# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
# def f(positional only /positional or keyword, *, keyword only):

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

# válido: os elementos de antes da barra (/) são posicionais
criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
# inválido: os elementos de antes da barra (/) não são posicionais
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido
