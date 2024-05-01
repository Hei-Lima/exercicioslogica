###IMPORTANTE: Para o código rodar, instale matplotlib e matplotlb_venn
import matplotlib.pyplot as plt
from matplotlib_venn import venn3

#Exercício 14:
A = {4, 5, 6, 7, 8}
B = {8, 9, 10, 11}
f = {(4, 8), (5, 8), (6, 9), (7, 9), (8, 10)}

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

def isInjetora(s):
    i = list()
    iset = set()
    for (x, y) in s:
        i.append(y)
        iset.add(y)
    if len(iset) != len(i):
        return "Não é Injetora"
    else:
        return "Injetora"
            
def isSobrejetora(r, s):
    img = set()
    for x, y in r:
        img.add(y)
        
    if img != s:
        return "Não é Sobrejetora"
    else:
        return "Sobrejetora"
            

print(f'Exercício 14')
print(f'1. Não pude responder com python, não existe função nativa para um diagrama que seja bom para o caso. O TeX 14 responde.')
print(f'2. Domínio: {domain(f)}, Imagem: {image(f)}')
print(f'3. {[y for (x, y) in f if x == 5]}, {[y for (x, y) in f if x == 7]}')
print(f'4. {[x for (x, y) in f if y == 9]}, {[x for (x, y) in f if y == 10]}')
print(f'5. {isInjetora(f)}, {isSobrejetora(f, B)}')

