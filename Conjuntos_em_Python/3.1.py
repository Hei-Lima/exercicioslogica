#O Livro assume que usaremos um ambiente de REPL como o CMD
#mas os códigos são os mesmos. Assumo. também, que preciso imprimir o set.
#Exercício 3.2:
print("Exercício 1:")
A = {1}
B = {1, 2} 
C = {frozenset({1}), 1} 
print("A = {1}")
print("B = {1, 2}")
print("C = {frozenset({1}), 1} \n")

print("Exercício 2:")


print(f"a-{A <= B}")
print(f"b-{A < B}")
print(f"c-{A in B}")
print(f"d-{A == B}")
print(f"e-{A <= C}")
print(f"f-{A < C}")
print(f"g-{A in C}")
print(f"h-{A == C}")
print(f"i-{1 in A}")
print(f"j-{1 in C}")
print(f"k-{frozenset({1}) in A}")
print(f"l-{frozenset({1}) in C}")
print(f"m-{set() not in A}")
print(f"n-{set() <= C}")
print(f"o-{B < C}")
