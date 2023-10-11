# elimina elementos duplicados
numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)  # {1, 2, 3, 4}

#  o SET não garante a ordem dos elementos, não ordena
letras = set("abacaxi")
print(letras)  # {"b", "a", "c", "x", "i"}

carros = set(("palio", "gol", "celta", "palio"))
print(carros)  # {"gol", "celta", "palio"}

#  também é possível declarar com {}
linguagens = {"python", "java", "python",}
print(linguagens)
