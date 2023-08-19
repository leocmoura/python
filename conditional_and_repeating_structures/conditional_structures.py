MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input('Informe sua idade: '))

if idade >= MAIOR_IDADE:
    print('Pode tirar CNH.')

# if idade < MAIOR_IDADE:
#     print('Não pode tirar CNH.')
else:
    print('Não pode tirar CNH.')

if idade >= MAIOR_IDADE:
    print('Pode tirar CNH. ')
elif idade == IDADE_ESPECIAL:
    print('Pode assistir aulas teoricas, mas, não pode tirar CNH')
else:
    print('Ainda não pode tirar nem assistir aulas.')