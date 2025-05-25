from math import sqrt, floor

valor = int ( input ('\nInforme o número até o qual você deseja encontrar todos os primos menores que ele:\n') ) 

raiz = floor(sqrt(valor)) 

lista = [False,False]

primos = []

for i in range (2 ,valor+1):
    lista.append (True)

print ('\nOs primos de 2 a {} são:\n'.format(valor))

for i in range (2, raiz):

    if lista[i]:

        for j in range (i*2, valor+1, i):
            
            lista[j] = False

for numero, i in enumerate(lista):

    if i:
        primos.append(str(numero))

print (', '.join(primos) + '\n')