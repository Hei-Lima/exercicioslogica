#Exercício 2:
a = {1,2,3,4}
b = {"a","b","c","d","e","f"}
c = {1,2}
d = {1,3,4,"a","b"}
e = {frozenset({1}),2,frozenset({"a",1})}
f = {1,"c","d"}
g = {"d","e",2,3}
U = a | b | c | d | e | f | g
O = frozenset([])

print("Exercício 2:")

print(f"1-{c - d}")
print(f"2-{a & f}")
print(f"3-{a & b}")
print(f"4-{(U-c) & (U - f)}")
print(f"5-{e & c}")
print(f"6-{(c | d) - (c & d)}")
print(f"7-{f | c}")
print(f"8-{(U - g) & c}")
print(f"9-{a & e}")
print(f"10-{(e | b) | d}")

