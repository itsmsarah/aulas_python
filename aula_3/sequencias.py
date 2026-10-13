# listas mutavel ou seja dá para mudarid
# da para fazer append em list como "inteiros.append(91) mas não da pra fazer em tupla"
# é uma lista ordenada, ou seja, vc sempre vai ter as posições cpmeçand por 1 elemento, dps 2 elemento e etc
inteiros = [1,2,3]
strings = ["sarah" , "gi" , "sa"]
mista = ['abc', None, 1, False]

# tuplas são imutaveis
# não da pra usar append aqui , ou seja, adicionar mais alguma coisa
inteiros = (1,2,3)
strings = ("sarah" , "gi" , "sa")
mista = ('abc', None, 1, False)

# METODO É ATRIBUTO QUE É CHAMAVEL

# intervalos (range)
range(fim)
#inicio = 0 /passo = 1 
#ele sempre coloca o primeiro na lista, se nn colocarmos vai ser igual a 0 
range(inicio, fim)
#aqui podemos colocar qual nmr ele vai começar, exemplo ele vai de 2 a 10 ou seja (2,11)
#colocar 11 inves de 10 pq ele vai até o penultimo nmr que vc realmente quer
range ( inicio,fim ,passo)
#e a gente pode tbm colocar o passo, se  a gente quiser que pule as casas etc
#ex range (2,11,2) -começa no 2, vai até 10 e pula de 2 em 2 

# tbm pode ir de tras pra frente, caso eu quero que comece no 10 e vai ate o 2 , de 2 em2
#basta colocar list(range(10, 2, -2)), ou seja , o 2 começou a ser o final da lista