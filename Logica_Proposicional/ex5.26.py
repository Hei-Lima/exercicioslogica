# Para cada fórmula bem formada abaixo, determine se ela é uma tautologia, uma 
# contradição, ou uma contingência. Justifique utilizando tabelas-verdade 
# ou dedução natural.

def neg(x):
    return 1 - x

def conj(x,y):
    return 1 if x+y == 2 else 0

def disj(x,y):
    return 0 if x+y == 0 else 1

def impl(x,y):
    return 1 if x == 0 or y == 1 else 0

def xor(x,y):
    return 0 if x == y else 1

def iff(x,y):
    return 1 if x == y else 0


formula1 = [(p, q, r, neg(p), disj(q, r), neg(disj(q, r)), impl(neg(disj(q, r)), neg(p)), conj( (impl (p, disj(q, r))), impl( neg(disj(q, r)), neg(p) )  )) for p in [0,1] for q in [0,1] for r in [0,1]]
print('1) P | Q | R | ¬P | Q ∨ R | ¬(Q ∨ R) | ¬(Q ∨ R) → ¬P | (P → (Q ∨ R)) ∧ (¬(Q ∨ R) → ¬P)\n')

formula2 = [( p, q, r, neg(r), disj(p, q), disj(q, p), impl(disj(p, q), neg(r)), disj(neg(r), disj(q, p)), conj(impl(disj(p, q), neg(r)), disj(neg(r), disj(q, p))) ) for p in [0,1] for q in [0,1] for r in [0,1]]
print('2) P | Q | R | ¬R | P ∨ Q | Q ∨ P | (P ∨ Q) → ¬R | ¬R ∨ (Q ∨ P) | ((P ∨ Q) → ¬R) ∧ (¬R ∨ (Q ∨ P))\n')

formulas = [formula1, formula2]

for formula in formulas:
    print(f'{formulas.index(formula) + 1})')
    validador = 0
    for row in formula:
        print(row)
        if row[-1] == 1:
            validador += 1

    if validador == len(formula):
        print('Tautologia')

    elif validador == 0:
        print('Contradição')

    else:
        print('Contingência')    
    
    print('')

#FIM :D