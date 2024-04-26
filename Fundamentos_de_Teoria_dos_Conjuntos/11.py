import itertools


#Exercício 11:
A = {2, 3, 4, 5}
B = {3, 4, 5, 6, 10}

z= list(itertools.product(A, B))

def domain(s):
    D = set()
    for (x, y) in s:
        D.add((x))
    return D

def image(s):
    Im = set()
    for (x, y) in s:
        Im.add((y))
    return Im


def isDivisible():
    U = set()
    for (x, y) in z:
        if (x % y) == 0:
            U.add((x, y))
    return U

def isTwelve():
    U = set()
    for (x, y) in z:
        if (x * y) == 12:
            U.add((x, y))
    return U

def isPlusOne():
    U = set()
    for (x, y) in z:
        if x == (y + 1):
            U.add((x, y))
    return U

def isLessEqual():
    U = set()
    for (x, y) in z:
        if x <= y :
            U.add((x, y))
    return U



print(f'Exercício 11')
print(f'1. Pares: {isDivisible()}, Domínio: {domain(isDivisible())}, Imagem: {image(isDivisible())}')
print(f'2. Pares: {isTwelve()}, Domínio: {domain(isTwelve())}, Imagem: {image(isTwelve())}')
print(f'3. Pares: {isPlusOne()}, Domínio: {domain(isPlusOne())}, Imagem: {image(isPlusOne())}')
print(f'4. Pares: {isLessEqual()}, Domínio: {domain(isLessEqual())}, Imagem: {image(isLessEqual())}')





