name = "lEoNardo mOura"

print(name.upper()) # tudo maiusculo
print(name.lower()) # tudo minusculo
print(name.title()) # primeira maiuscula

text = "  hello word!  "

print(text)
print(text.strip() + ".") # removendo espaços
print(text.rstrip() + ".") # removendo espaços da direita. rightstrip
print(text.lstrip().title() + ".") # removendo espaços da esquerda. leftstrip

menu = "Python"

print("$$$$" + menu + "$$$$")
print(menu.center(14, "-"))
print("-".join(menu))

# for letra in menu:
#     print(letra, end="-")
# print()