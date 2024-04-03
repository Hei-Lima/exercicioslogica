#Exercício 1:
a = {1}
b = {1,2}
c = {frozenset([1]), 1}
O = frozenset([])

print("Exercício 1:")

print(f"1-{a <= b}")
print(f"2-{a < b}")
print(f"3-{a in b}")
print(f"4-{a == b}")
print(f"5-{a <= c}")
print(f"6-{a < c}")
print(f"7-{a in c}")
print(f"8-{a == c}")
print(f"9-{1 in a}")
print(f"10-{1 in c}")
print(f"11-{frozenset([1]) in a}")
print(f"12-{frozenset([1]) in c}")
print(f"13-{O not in c}")
print(f"14-{O <= b}")

