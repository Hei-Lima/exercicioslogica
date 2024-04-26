import itertools


#Exercício 3:
A = {x for x in range(0, 400)}
B = {x for x in range(0, 400)}

z= list(itertools.product(A, B))

def lessThanNine():
    U = set()
    for (x, y) in z:
        if (x + y) < 9:
            U.add((x, y))
    return U

print(f'Exercício 3')
print(f'1. Pares: {lessThanNine()}')






