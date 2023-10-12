# def = informa que inicia uma função

def exibir_mensagem():
    print("Olá mundo!")


def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")


def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")

# para executar, é necessário chamar a função e informar seus argumentos
exibir_mensagem()
exibir_mensagem_2(nome="Guilherme") #ou exibir_mensagem_2("Guilherme")
exibir_mensagem_3()
exibir_mensagem_3(nome="Chappie")
