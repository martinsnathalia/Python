# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n=int(input('Digite um número: '))
print('O dobro do número {} é {}'.format(n,(n*2)))
print('O triplo do número {} é {}'.format(n,(n*3)))
print('A raiz quadrada do número {} é {}'.format(n,(n**(1/2))))

print('A raiz quadrada do número {} é {}'.format(n,pow(n,(1/2)))) # outra forma de fazer
