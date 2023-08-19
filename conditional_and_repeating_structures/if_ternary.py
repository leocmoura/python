# if ternario permite escrever condição em uma linha.
# 3 partes, retorno caso verdadeiro, expressão logica e retorno caso false.
# usado para coisas simples

saldo = 2000
saque = 2000
status = 'Sucesso!' if saldo >= saque else 'Falha'

print(f"{status} ao realizar o saque! ")