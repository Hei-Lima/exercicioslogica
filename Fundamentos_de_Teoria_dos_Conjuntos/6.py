import math

#Exercício 6:
A = set(range(5, 1500))  
B = {10, 12, 16, 20}
C = set()
for y in range(0, 1500): #Apesar do conjunto ser infinito, implementações de infinito em programas de computador são chatas, então 2000 vai ter que dar conta.
    x = 2 * y
    C.add(x)
thatSet = set(range(21))
O = set()     

print("Exercício 6:")


print(f"1. {B <= C}")
print(f"2. {A <= C}")
print(f"3. {set({11, 12, 13}) <= A}")
print(f"4. {set({12}) in B}")
print(f"5. {not thatSet.issubset(B)}")
print(f"6. {set(O) in B}")
print(f"7. {B < A}")
print(f"8. {26 in C}")
print(f"9. {set({12}).issubset(B)}")
print(f"10. ERRO: Operação inválida (Inteiro e Set)" )
print(f"11. {O not in A}")
print(f"12. {not O < A}")



#Os naturais são todos os inteiros positivos mais o 0.
#5 in a