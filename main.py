numeros = [2]
quadrados = list(map(lambda x: x ** 2, numeros))
print(quadrados)  

#outra forma

dobro = lambda x : x * 2
print(dobro(2))

###############################
from functools import reduce

numeros = [1,2]
soma = reduce(lambda x, y: x + y, numeros)
print(soma)

#outra forma

soma = lambda x1, x2 : x1 + x2

d1 = float(input('Digite'))
d2 = float(input('Digite'))
print(soma(d1,d2))


#############################

numero = [8]
verificar_par = list(map(lambda x: x % 2 == 0, numero))
resultado = verificar_par 
print(resultado)

#outra forma

par = lambda x : x % 2 == 0
print(par(11))

#############################

convert = lambda x: x.upper()
print(convert('hello'))


#################################

produto = lambda a,b,c : a*b*c
print(produto(1,3,6))

#outra forma

from functools import reduce

numeros = [1, 2, 3, 4, 5]
soma = reduce(lambda x, y: x + y, numeros)
print(soma)  # Saída: 15



