# Exemplo

pessoa = {"nome": "Leonardo", "idade": 26} # criando
pessoa = dict(nome="Leonardo", idade=26) # criando
pessoa["telefone"] = "99999-9999" # adicionando key telefone valor ...

# Dicts aninhados

contatos = {
    "leonardo@email.com": {"nome": "leonardo", "telefone": "99995-9999"},
    "lia@email.com": {"nome": "lia", "telefone": "99992-9999"},
    "israel@email.com": {"nome": "israel", "telefone": "99995-9999"},
    "extra@email.com": {"nome": "extra", "telefone": "99995-9999", "extra": {"a": 1}},
}

telefone = contatos["israel@email.com"]["telefone"]
print(telefone)

extra = contatos["extra@email.com"]["extra"]["a"]
print(extra)

# ITERANDO

# for chave in contatos:
#     print(chave, contatos[chave])

# melhor
for chave, valor in contatos.items():
    print(chave, valor)

# METODOS

.clear() # limpa dict
.copy() # cria copia
.fromkeys() # cria keys
dict.fromkeys(["nome", "telefone"]) # cria com valores none
dict.fromkeys(["nome", "telefone"], "vazio") # cria com valores padrão "vazio"
.get("key") # se key nao existir retorna None ou valor default
.get("key", {}) # {}
.keys() # retorna valor so das chaves
.pop() # remove uma chave, retorna valor que encontrou
.pop("key", "não encontrou")
.popitem() # remove na sequencia
.setdafault() # adiciona chave se não existir e valor definido, se existir ele nao muda o valor
.update() # atualizar dicionario 
.values() # retorna so os valores sem as chaves

# Metodo in de verificação
# chave é uma key in dict
chave in dict # True or False

del contatos["leonardo@email.com"]["telefone"]
del contatos["israel@email.com"]