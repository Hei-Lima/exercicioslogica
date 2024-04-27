import itertools
#Enfim, os que são infinitos são maiores que estes aqui.

#Exercício 12:
A = {x for x in range(0, 400)}
B = {x for x in range(0, 400)}

z= list(itertools.product(A, B))

def lessThanNine():
    U = list()
    for (x, y) in z:
        if (x + y) < 9:
            U.append((x, y))
    return U

def yPlusThree():
    U = list()
    for (x, y) in z:
        if x == y + 3:
            U.append((x, y))
        if len(U) > 200:
            return U[:5]
    return U

def equalsTwelve():
    U = list()
    for (x, y) in z:
        if x*3 + y*3 == 12:
            U.append((x, y))
    return U

def isACube():
    U = list()
    for (x, y) in z:
        if (y**(1/3)).is_integer():
            U.append((x, y))
        if len(U) > 200:
            return U[:5]
    return U

print(f'Exercício 12')
print(f'1. {lessThanNine()}')
print(f'2. {yPlusThree()}...(Xn, Yn+3), (Xn, Yn+6)...')
print(f'3. {equalsTwelve()}')
print(f'4. {isACube()}...(Xn, Y), (Xn, Y(n+1)³)')






