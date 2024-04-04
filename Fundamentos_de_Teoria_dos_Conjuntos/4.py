#Exercício 4:
import operator


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
    
a = frozenset({0, 1, 2, 3, 4, 5})
b = frozenset({3, 4, 5, 6, 7, 8})
c = frozenset({1, 3, 7, 8})
d = frozenset({3, 4})
e = frozenset({1, 3})
f = frozenset({1})

x = 1

def acharx(operador1, conjuntofixo1, operador2, conjuntofixo2):
    listaconjuntos = [a, b, c, d, e, f]
    global x 
    print(f'{x}- ', end='')
    for conjunto in listaconjuntos:
        if operador1(conjunto, conjuntofixo1) and operador2(conjunto, conjuntofixo2):
            if conjunto == a:
                print('A', end=' ')
            elif conjunto == b:
                print('B', end=' ')
            elif conjunto == c:
                print('C', end=' ')
            elif conjunto == d:
                print('D', end=' ')
            elif conjunto == e:
                print('E', end=' ')
            elif conjunto == f:
                print('F', end=' ')
            else:
                print('Error')
    x += 1
    
    print('')

acharx(issubset, a, issubset, b)
acharx(isnotsubset, b, issubset, c)
acharx(isnotsubset, a, isnotsubset, c)
acharx(issubset, b, isnotsubset, c)
