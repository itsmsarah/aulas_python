# FUNÇÕES

def nome_funcao(p1, p2):
    print(p1 + p2)

nome_funcao(3, 5)

# existe diferença entre return e print:
#
# print() é uma função usada para EXIBIR algo na tela.
#
# return é usado dentro de uma função para DEVOLVER um valor.
# Esse valor pode ser armazenado em uma variável e usado depois.
#
# O return é utilizado dentro de funções/métodos.

def soma(a, b):
    print(a + b)


soma(3, 5)

def soma(a, b):
    return a + b


resultado = soma(3, 5)

print(resultado)

# a função devolve 8, e guardamos esse valor na variável resultado.

def soma(a, b):
    print(a + b)


resultado = soma(3, 5)

print("Resultado:", resultado)
# resultado : NONE



def soma(a, b):
    return a + b


resultado = soma(3, 5)

print("Resultado:", resultado)
# resultado : 8

# pq return retornou um valor