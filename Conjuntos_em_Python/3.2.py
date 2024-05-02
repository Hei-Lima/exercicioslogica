#O Livro assume que usaremos um ambiente de REPL como o CMD
#mas os códigos são os mesmos. Assumo. também, que preciso imprimir o set.
#Exercício 3.2:
print("Exercício 1:")

A = {1, 2, 3, 4}
B = {"a", "b", "c", "d", "e", "f"} 
C = {1, 2} 
D = {1, 3, 4, "a", "b"} 
E = {frozenset({1}), 2, frozenset({"a", 1})} 
F = {1, "c", "d"}
G = {"d", "e", 2, 3} 
U = A | B | C | D | E | F | G

print("Exercício 2:")

print(f"a-{C - B}")
print(f"b-{A & F}")
print(f"c-{A & B}")
print(f"d-{(A-U) & (B-U)}")
print(f"e-{E & C}")
print(f"f-{(C | D) - (C & D)}")
print(f"g-{F | C}")
print(f"h-{(G - U) & C}")
print(f"i-{A | E}")
print(f"j-{(E | B) | D}")
print(f"k-{A ^ D}")
print(f"l-{A ^ B ^ C}")