#O Livro assume que usaremos um ambiente de REPL como o CMD
#mas os códigos são os mesmos. Assumo. também, que preciso imprimir o set.
#Exercício 3.5:

#Funções (não gosto de importar pra facilitar a leitura estruturada do codigo, nesse contexto academico)
def cartesian(n, m):
    conj = set()
    for x in n:
        for y in m:
            conj.add((x, y))
    return conj

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


print("Exercício 1:")

N = set(x for x in range(-1000, 1000))

NSquared = cartesian(N, N)

e1 = set(x for x in N if x%2 == 0)
o1 = set(x for x in N if x%2 != 0)

e2 = set(cartesian(e1, e1))
o2 = set(cartesian(o1, o1))

p1 = set((x, y) for x, y in NSquared if (x + y)%2 == 0)
p1 = set((x, y) for x, y in NSquared if (x + y)%2 == 0)
p1 = set((x, y) for x, y in NSquared if (x + y)%2 == 0)
p1 = set((x, y) for x, y in NSquared if (x + y)%2 == 0)

print(f'ρ1.\n {reflexive(NSquared)}\n {symmetric(NSquared)}\n {transitive(NSquared)}\n {antisymmetric(NSquared)}')
print(f'ρ1.\n {reflexive(NSquared)}\n {symmetric(NSquared)}\n {transitive(NSquared)}\n {antisymmetric(NSquared)}')
print(f'ρ1.\n {reflexive(NSquared)}\n {symmetric(NSquared)}\n {transitive(NSquared)}\n {antisymmetric(NSquared)}')
print(f'ρ1.\n {reflexive(NSquared)}\n {symmetric(NSquared)}\n {transitive(NSquared)}\n {antisymmetric(NSquared)}')

