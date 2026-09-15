n1 = 10
n2 = 5
n3= 4
n4 = 20

resto = n1 % n2
print(resto)

vendo_diferenca = n4 / n3
print(vendo_diferenca)

# com um / só ele pega a outra casa decimal também, se eu não quiser isso tenho que usar //

diferenca = n4//n3
print(diferenca)

# a exponenciação vem da direita pra esquerda, então se eu quiser que comece ela esquerda tenho que colocar ()
expo = (n2 ** n3) ** n2
print(expo)


age = 18
faculdade = True

# Operações lógicas  and && , or || ou not !

if age < 17 and faculdade == True:
    print("Tu ta sabendo")
else:(
    print("deixa de ser besta")
)

euzinha = True
euzinha = not euzinha
print(euzinha)
