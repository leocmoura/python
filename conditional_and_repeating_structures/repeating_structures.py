texto = input('informe um texto: ')
texto = ""
VOGAIS = 'AEIOU'

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
else: #pode-se usar else para executar algo no final do laço, não é comum no dia a dia
    print('Else')
    print('Executado no final do laço')

# Função RANGE
# range(start, stop, step)
    tabuada_5 = []
for numero in range(0, 51, 5):
    tabuada_5.append(numero)
    # print(tabuada_5)
    # print(numero, end=" ")
print(tabuada_5)


# Função WHILE

opcao = -1
while opcao != 0:
    opcao = int(input('[1] Sacar \n[2] Extrato \n[0]Sair \n: '))

    if opcao == 1:
        print('Sacando...')
    elif opcao == 2:
        print('Exibindo extrato...')
else: #pode-se usar else para executar algo no final do laço, não é comum no dia a dia
    print('Obrigado por usar nosso sistema')

while True:
    numero = int(input('Informe um número: '))
    if numero == 10:
        break # corta o laço da repetição
    print(numero)

#usando break no for

for number in range(1, 100):

    # if number == 12:
    #     # break
    
    if number % 2 == 0:
        continue

    print(number, end=" ")