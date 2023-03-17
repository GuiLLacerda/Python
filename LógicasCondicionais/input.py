"""
Funcao input() - Para receber e imprimir dados do usuário
"""
# 1 Forma

nome = input("Qual é seu nome? ")
print("Olá, "+nome)

idade = input("Qual a sua idade? ")
print("Sua idade é "+idade)

# 2 Forma

nome = input("Qual é o seu nome? ")
idade = input("Qual a sua idade? ")

print("Seu nome é {0} e sua idade é {1}".format(nome, idade))

# 3 Forma

nome = input("Qual eh seu nome? ")
idade = input("Qual eh a sua idade? ")

print(f'Seu nome é {nome} e sua idade é {idade}')
