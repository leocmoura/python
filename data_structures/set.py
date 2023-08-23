# Coleção que não possui objetos repetidos, é usado para representar conjuntos matemáticos
# eliminar itens duplicados 

set([1,2,3,1,3,4]) # {1,2,3,4}
# ordem dos elementos retornados não é confiavel
# não é possivel acessar indice dos elementos

numeros = {'1,2,3,2'}
# numeros[0] ERRO
# deve-se converter para list para acessar indice
numeros = list(numeros)
numeros[0]

# iteração
carros = {'gol', 'celta', 'palio'}

for carro in carros:
    print(carro)
else:
    print('------')

# no for pode usar função enumerate para saber o indice daquele elemento

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
    
# operações matematica dos conjuntos
conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

# {}.union()
conjunto_a.union(conjunto_b)
# {}.intersection()
conjunto_b.intersection(conjunto_b)
# {}.difference()
conjunto_a.difference(conjunto_b) # {1}
conjunto_b.difference(conjunto_a) # {4}
# {}.symmetric_difference()
conjunto_a.symmetric_difference(conjunto_b) # {1, 4}
# {}.issubset - 
conjunto_c = {1,2,3}
conjunto_d = {4,1,2,5,6,3}
conjunto_c.issubset(conjunto_d) # True
conjunto_d.issubset(conjunto_c) # False
# {}.issuperset - contrario issubset
conjunto_c.issubset(conjunto_d) # False
conjunto_d.issubset(conjunto_c) # True
# {}.isdisjoint
conjunto_e = {1,2,3,4,5}
conjunto_f = {6,7,8,9}
conjunto_g = {1,0}
conjunto_e.isdisjoint(conjunto_f) # True
conjunto_e.isdisjoint(conjunto_g) # False
# {}.add
conjunto_g.add(2)
conjunto_g.add(2)
# {}.clear - limpar
# {}.copy - copiar
# {}.discard(valor) - descartar algum valor, se valor nao estiver no conjunto simplesmeste ignora
# {}.pop - retirando os valores 1 por 1 da esquerda para direita
# {}.remove(valor) - 
# {}.len() - retorna tamanho

# in
1 in conjunto_e # True

print(conjunto_c | conjunto_d)