import itertools
U = set()
#Powerset
def powerset(conjunto):
    listaconjunto = list(conjunto)
    subconjuntos = []
    for i in range(2 ** len(listaconjunto)):
        subconjunto = []
        for k in range(len(listaconjunto)):
            if i & 1 << k:
                subconjunto.append(listaconjunto[k])
        subconjuntos.append(subconjunto)
    return subconjuntos

#É subset e não é subset
def issubset(x, y):
    if x <= y:
        return True
    else:
        return False
    
def isnotsubset(x, y):
    if x <= y:
        return False
    else:
        return True
    
#Complemento absoluto
def absoluteComplement(x):
   z = U - x #U é o conjunto-Universo, crie ele antes.
   return z

#Produto cartesiano (Importe itertools)
def cartesianProduct(x, y):
    z= list(itertools.product(x,y))
    return z

#Par ou impar
def isEven(x):
    if x % 2:
        return "even"
    else:
        return "odd"
    

#Dominio
def domain(s):
    D = set()
    for (x, y) in s:
        D.add((x))
    return D

#Imagem
def image(s):
    Im = set()
    for (x, y) in s:
        Im.add((y))
    return Im