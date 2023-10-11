# FORMATAÇÃO, REMOVER ESPAÇOS E CENTRALIZAR TÍTULOS
nome = "gUIlerMe"

# Formatação de palavras
# Todas as letras Maíúsculas
print(nome.upper())
# Todas as letras Minúsculas
print(nome.lower())
# Primeira maiúcula e demais minúscula
print(nome.title())

texto = "  Olá mundo!  "

# remove espaços em br
print(texto + ".")

# remove espaços das laterais
print(texto.strip() + ".")

# remove espaços da direita
print(texto.rstrip() + ".")

# remove espaços da esquerda
print(texto.lstrip() + ".")

menu = "Python"

print("####" + menu + "####")

# Centraliza a string de acordo com o número definido
print(menu.center(14))

# Concatena palavras para atingir um determinado número de caracteres
print(menu.center(14, "#"))

# insere o caracter desejado intercalando a cada caracter da string
print("-".join(menu))    