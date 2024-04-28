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


###endorrelações:

#Reflexiva
def reflexive(l):
    d = set()
    i = set()
    for (x, y) in l:
        i.add(y)
        if x == y:
            d.add(x)
    if d == i:
        return "Reflexiva"
    else:
        return "Não Reflexiva"


#Simetrica            
def symmetric(l):
    for x in l:
        conj = (x[1], x[0])
        if conj in l:
            continue
        else:
            return "Não é simétrica"
    return "Simétrica"

#antissimetrica  
def antisymmetric(l):
    for x in l:
        conj = (x[1], x[0])
        if conj not in l:
            continue
        else:
            return "Não é Antissimétrica"
    return "Antissimétrica"


#transitiva
###Esse codigo aqui foi pego deste site, nele existem implementações melhores que as minhas para os problemas: https://w3.cs.jmu.edu/mayfiecs/cs228/python/relations.py
def transitive(l):
    conj = set()
    for x, y in l:
        conj.add(x)

    for x in conj:
        for y in conj:
            if (x, y) in conj:
                for z in conj:
                    if (y, z) in conj and (x, z) not in conj:
                        return "Não Transitiva"
    return "Transitiva"