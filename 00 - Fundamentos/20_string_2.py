nome = "Bianca"
idade = 20
profissao = "Programadora"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Bianca", "idade": 20, "saldo": 45.435}

# não muito utilizado
print("Nome: %s Idade: %d" % (nome, idade))

# segue a orgem definida no final
print("Nome: {} Idade: {}".format(nome, idade))

# a ordem é definida dentro das chaves
print("Nome: {1} Idade: {0}".format(idade, nome))
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))

# descrevendo a variável no final, é possível mudar o nome dentro das chaves
print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {name} Idade: {age}".format(name=nome, age=idade))

# utilizando a biblioteca (dados)
print("Nome: {nome} Idade: {idade}".format(**dados))

#  diferença em incluir o "f" no ínicio, forma simples
print(f"Nome: {nome} Idade: {idade}")
# Formatando o número longo
#  O "10" não é obrigatório, ele fala o número de espaços, se deiar vazio é igual a "0"
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.2f}")

