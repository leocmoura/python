# Criação
frutas = ['laranja', 'maça', 'banana'] # com valores
frutas = [] # vazia
letras = list('python') # com as letras da string passada
numeros = list(range(10)) # com numeros do range
carro = ['Montana', 'LS', 43000, 2015, 150000, 'Brasília', True] # de tipos diferentes
# print(type(carro[2])) >> int
# print(carro[-1]) # ultimo indice

# Listas Aninhadas - "Lista dentro de lista" 

matriz = [
    [1, 'a', 2],
    ['b', 3, 4],
    [6, 5, 'c']
]
matriz[0] # [1, 'a', 2]
matriz [0][2]
(matriz[1][-1]) # 4

# Fatiamento de lista

lista = list('leonardo')
print(lista[2:])
print(lista[0:3:2])
lista[::-1]

# Iterar

for letra in lista:
    print(letra)

# Indice

vehicles = ['xtz 125', 'gol g4', 'montana ls']

for indice, vehicle in enumerate(vehicles):
    print(f"{indice}: {vehicle}")

# List Comprehension

pares = [numero for numero in numeros if numero % 2 == 0 ]
print(pares)
quadrado = [numero ** 2 for numero in numeros]
print(quadrado)

# Metodos da classe list
# [].append() #adiciona ao fim
# [].clear() # limpa a lista
vehicles2 = vehicles.copy() # faz uma cópia
print(id(vehicles2))
print(id(vehicles))
vehicle.count('xtz 125') #>> 1 # conta quantas vezes tem aquele item na lista
[].extend(1, 2,) # extende a lista, aumenta, adiciona ao fim
vehicle.index('xtz 125') # pega o indice do item
[].pop() # remove o ultimo item ou o indice pedido
[].remove() # remove o item pedido
[].reverse() # reverse na lista
[].sort() # reorganiza, ordem alfabetica, tamanho pedido
linguagens = ['python', 'js', 'c', 'java']
linguagens.sort()
linguagens.sort(reverse=True)
linguagens.sort(key=lambda x: len(x))
linguagens.sort(key=lambda x: len(x), reverse=True)
len(linguagens) # conta quantos itens tem na lista
sorted(linguagens)

# [n**2 if n > 6 else n for n in range(10) if n % 2 == 0] 