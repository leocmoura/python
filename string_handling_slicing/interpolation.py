name = "Leonardo"
age = 26.5
height = 1.67
occupation = "Programador"
language = "Python"
saldo = 100.10000

dados = {"nome":"dictionary", "idade":26, "altura":1.67}

# OLD STYLE - nao é mais utilizado
print("Nome: %s Idade: %d Altura: %f " %(name, age, height)) #ordem nas variaveis

# .FORMAT
print("Nome: {} Idade: {} Altura: {}".format(name, age, height))
print("Nome: {1} Idade: {2} Altura: {0}".format(height, name, age))
print("Nome: {1} Idade: {2} Altura: {0}, nome: {1} , nome: {1} , nome: {1} ".format(height, name, age))
print("Nome: {nome} Idade: {idade} Altura: {altura}".format(altura=height, nome=name, idade=age)) 
print("Nome: {nome} Idade: {idade} Altura: {altura}".format(**dados)) #dicionario

# f"String"
print(f"Nome: {name} - Idade: {age} - Altura: {height}.")
print(f"Nome: {name} - Idade: {age} - Altura: {height} - Saldo: {saldo:.2f}.")
print(f"Nome: {name} - Idade: {age} - Altura: {height} - Saldo: {saldo:10.2f}.")
print(f"Nome: {name} - Idade: {age} - Altura: {height} - Saldo: {saldo:.1f}.")
