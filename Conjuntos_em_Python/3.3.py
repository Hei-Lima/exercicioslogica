#O Livro assume que usaremos um ambiente de REPL como o CMD
#mas os códigos são os mesmos. Assumo. também, que preciso imprimir o set.
#Exercício 3.3:
print("Exercício 1:")

A = {"p", "q", "r", "s"}
B = {"r", "t", "v"} 
C = {"p", "s", "t", "u"} 
U = {"p", "q", "r", "s", "t", "u", "v", "w"}

def cartesian(s1, s2):
    conj = set()
    for x in s1:
        for y in s2:
            conj.add((x, y))
    return conj


print("Exercício 2:")

print(f"a-{B & C}")
print(f"b-{A | C}")
print(f"c-{(C - U)}")
print(f"d-{(A & B & C)}")
print(f"e-{B - C}")
print(f"f-{(C - B)}")
print(f"g-{(A | B) - U}")
print(f"h-{cartesian(A, B)}")
print(f"i-{((A | B) & (C - U)) }")
print(f"j-{((A - B) - U) & (C - U)}")