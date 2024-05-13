#Exercício 3:
a = frozenset({'a', 'b', 'c'})
b = frozenset({'a', ('b','c')})
c = frozenset({'a', ('b', 'c'), ('d')})

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

print(f'Exercício 3')
print(f'1- {powerset(a)}\n')
print(f'2- {powerset(b)}\n')
print(f'3- {powerset(c)}\n')
