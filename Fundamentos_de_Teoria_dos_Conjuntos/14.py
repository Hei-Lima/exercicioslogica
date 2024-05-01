import itertools


#Exercício 3:
A = {4, 5, 6, 7, 8}
B = {8,9, 10, 11}
f = {(4, 8) (5, 8) (6, 9) (7, 9) (8, 10)}

def absoluteComplement(x):
   z = U - x #U é o conjunto-Universo, crie ele antes.
   return z

def cartesianProduct(x, y):
    z= list(itertools.product(x,y))
    return z

print(f'Exercício 3')
print(f'1. {B & C}')
print(f'2. {A | C }')
print(f'3. {absoluteComplement(C)}')
print(f'4. {A & B & C}')
print(f'5. {B - C}')
print(f'6. {C - B}')
print(f'7. {absoluteComplement(A | B)}')
print(f'8. {cartesianProduct(A, B)}')
print(f'9. {(A | B) & absoluteComplement(C)}')
print(f'10. {absoluteComplement((A - B)) - absoluteComplement(C)}')



