#O Livro assume que usaremos um ambiente de REPL como o CMD
#mas os códigos são os mesmos. Assumo. também, que preciso imprimir o set.
#Exercício 3.5:
print("Exercício 1:")

N = set(x for x in range(-1000, 1000))

def cartesian(n):
    conj = set()
    for x in n:
        for y in n:
            conj.add((x, y))
    return conj

NSquared = cartesian(N)

p1 = list()

for (x, y) in NSquared:
    if y != 0:
        if x % y == 0:
            p1.append((x, y))

p2 = list((x, y) for x, y in NSquared if x == y + 3)

p3 = list((x, y) for x, y in NSquared if (2 * x) + (3 * x) == 12)

#is_integer() checa se um número é um inteiro ou não. Qualquer forma que valide se o número não é quebrado pode ser aceita.
p4 = list((x, y) for x, y in NSquared if y**(1/3).is_integer())


print(f"1-\n ρ1:{p1}")
print(f"2-\n ρ2:{p2}")
print(f"3-\n ρ3:{p3}")
print(f"4-\n ρ3:{p4}")

