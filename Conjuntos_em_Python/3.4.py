#O Livro assume que usaremos um ambiente de REPL como o CMD,
#mas os códigos são os mesmos. Assumo. também, que preciso imprimir o set.
#Exercício 3.4:
print("Exercício 1:")

A = {2, 3, 4, 5}
B = {3, 4, 5, 6, 10} 


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

def cartesian(s1, s2):
    conj = set()
    for x in s1:
        for y in s2:
            conj.add((x, y))
    return conj

R = cartesian(A, B)
R1 = set((x, y) for x, y in R if x % y == 0)
R2 = set((x, y) for x, y in R if x * y == 12)
R3 = set((x, y) for x, y in R if x == y + 1)
R4 = set((x, y) for x, y in R if x <= y)

print("Exercício 2:")

print(f"1-\n Elementos:{R1}\n Domínio:{domain(R1)}\n Image:{image(R1)}")
print(f"1-\n Elementos:{R2}\n Domínio:{domain(R2)}\n Image:{image(R2)}")
print(f"1-\n Elementos:{R3}\n Domínio:{domain(R3)}\n Image:{image(R3)}")
print(f"1-\n Elementos:{R4}\n Domínio:{domain(R4)}\n Image:{image(R4)}")

