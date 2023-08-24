def exibir_mensagem():
    print("Olá mundo")


def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")


def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")

# exibir_mensagem()
# exibir_mensagem_2(nome="Leozin")
# exibir_mensagem_3()
# exibir_mensagem_3(nome="Leozi3")


def salvar_carro(marca, modelo, ano, placa):
    print(F"Carro inserido com sucesso! {marca} / {modelo} / {ano} / {placa}")

# salvar_carro("Fiat", "palio", 2000, "ABC-1234")
# salvar_carro(marca="Fiat", modelo="Palio", ano=2000, placa="ABC1234")
# salvar_carro(**{"marca": "Fiat", "modelo":"Palio","ano":2000, "placa":"ABC4567"})


def exibir_poema(data_extensa, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join(
        [f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extensa}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)


exibir_poema("Sexta-feira, 24 de agosto de 2023",
             "Conta e Tempo",
             "\n"
             "Deus pede estrita conta de meu tempo.",
             "E eu vou do meu tempo, dar-lhe conta.",
             "Mas, como dar, sem tempo, tanta conta",
             "Eu, que gastei, sem conta, tanto tempo?",
             "\n"
             "Para dar minha conta feita a tempo,",
             "O tempo me foi dado, e não fiz conta,",
             "Não quis, sobrando tempo, fazer conta,",
             "Hoje, quero acertar conta, e não há tempo.",
             "\n"
             "Oh, vós, que tendes tempo sem ter conta,",
             "Não gasteis vosso tempo em passatempo.",
             "Cuidai, enquanto é tempo, em vossa conta!",
             "\n"
             "Pois, aqueles que, sem conta, gastam tempo,",
             "Quando o tempo chegar, de prestar conta",
             "Chorarão, como eu, o não ter tempo...",
             autor="Frei António das Chagas",
             ano=1631)
print("\n")

# Parâmetros especiais

# Positional only
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
                                # a barra restringe a maneira que os argumentos podem ser passados
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")

# Keyword only

def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
            # asterisco define que argumentos devem ser passados com KEY
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro(modelo="palio", ano=1999, placa="ABC-1111", marca="Fiat", motor="1.0", combustivel="Flex")

# Keyword and positional only

def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

    criar_carro("palio", 1999, "abc-2222", marca="fiat", motor="1.3", combustivel="flex")

# Passando funções em funções - funçoes tbm sao objetos

def somar(a,b):
    return a + b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da opreação {a} + {b} = {resultado}")

exibir_resultado(10,10,somar)

# Escopo local e global - Não é boa pratica e deve ser evitada

salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    # Função alterou a variavel global - 
    # Certo seria copiar valor para outra variavel
    return salario

salario_bonus(500)
# print(salario_bonus)
print(salario)

