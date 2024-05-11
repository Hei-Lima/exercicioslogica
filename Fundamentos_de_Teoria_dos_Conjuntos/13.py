import itertools
from sympy import *
import time
start_time = time.time()
#Geralmente, as relações não mudam indo para infinito, então só precisamos de uma amotra suficientemente grande para provar.
#Esse, provavlmente, vai ser o código mais lento de todo o projeto, mas me orgulho muito dele. O time ali é para mostrar a demora da execução. - Hei-Lima

#Exercício 13:
A = {x for x in range(0, 400)}
B = {x for x in range(0, 400)}
P = {i for i in range(20) if isprime(i)}
O = {0, 1}
O2 = {(1, 1), (2, 2), (3, 3), (1, 2), (2, 1)}


z= list(itertools.product(A, B))
zp= list(itertools.product(P, P))
zo = list(itertools.product(O, O))
#relações:

def isEven():
    U = list()
    for (x, y) in z:
        if (x + y)%2 == 0:
            U.append((x, y))
    return U

def isDivisible():
    U = list()
    for (x, y) in zp:
        if (x % y) == 0:
            U.append((x, y))
    return U

#isParallel (tendi nada)

def isEqualSquared():
    U = list()
    for (x, y) in z:
        if x == y**2:
            U.append((x, y))
    return U

def isOneSquared():
    U = list()
    for (x, y) in zo:
        if x == y**2:
            U.append((x, y))
    return U

def isOlder():
    U = list()
    for (x, y) in z:
        if x > y:
            U.append((x, y))
    return U

def isSameOrOlder():
    U = list()
    for (x, y) in z:
        if x >= y:
            U.append((x, y))
    return U

def isSameColumn():
    U = list()
    for (x, y) in z:
        #se a coluna tiver 10 pessoas:
        if x//10 == y//10:
            U.append((x, y))
    return U

def isSameLevel():
    U = list()
    for (x, y) in z:
        #Mesmo coompreende apenas se tiverem o mesmo direito exato.
        if x == y:
            U.append((x, y))
    return U


###Relações:
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
            
def symmetric(l):
    for x in l:
        conj = (x[1], x[0])
        if conj in l:
            continue
        else:
            return "Não é simétrica"
    return "Simétrica"

def antisymmetric(l):
    for x in l:
        conj = (x[1], x[0])
        if conj not in l:
            continue
        else:
            return "Não é Antissimétrica"
    return "Antissimétrica"

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

print(f'Exercício 13')
print(f'1.\n {reflexive(isEven())}\n {symmetric(isEven())}\n {transitive(isEven())}\n {antisymmetric(isEven())}')
print(f'2.\n {reflexive(isDivisible())}\n {symmetric(isDivisible())}\n {transitive(isDivisible())}\n {antisymmetric(isDivisible())}')
print(f'3.Não consegui fazer computacionalmente')
print(f'4.\n {reflexive(isEqualSquared())}\n {symmetric(isEqualSquared())}\n {transitive(isEqualSquared())}\n {antisymmetric(isEqualSquared())}')
print(f'5.\n {reflexive(isOneSquared())}\n {symmetric(isOneSquared())}\n {transitive(isOneSquared())}\n {antisymmetric(isOneSquared())}')
print(f'6.\n {reflexive(O2)}\n {symmetric(O2)}\n {transitive(O2)}\n {antisymmetric(O2)}')
print(f'7.\n {reflexive(isOlder())}\n {symmetric(isOlder())}\n {transitive(isOlder())}\n {antisymmetric(isOlder())}')
print(f'8.\n {reflexive(isSameOrOlder())}\n {symmetric(isSameOrOlder())}\n {transitive(isSameOrOlder())}\n {antisymmetric(isSameOrOlder())}')
print(f'9.\n {reflexive(isSameColumn())}\n {symmetric(isSameColumn())}\n {transitive(isSameColumn())}\n {antisymmetric(isSameColumn())}')
print(f'10.\n {reflexive(isSameLevel())}\n {symmetric(isSameLevel())}\n {transitive(isSameLevel())}\n {antisymmetric(isSameLevel())}')
print("--- %s seconds ---" % (time.time() - start_time))







