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


# N.1
t1 = [(a, impl(a, a)) for a in [0,1]]
print('1) Fumaça | Fumaça → Fumaça')

# N.2
t2 = [(a, b, impl(a, b)) for a in [0,1] for b in [0,1]]
print('2) Fumaça | Fogo | Fumaça → Fogo')

# N.3
t3 = [(a, b, neg(a), neg(b), impl(a, b), impl(neg(a), neg(b)), impl(impl(a, b), impl(neg(a), neg(b)))) for a in [0, 1] for b in [0, 1]]
print('3) Fumaça | Fogo | ¬Fumaça | ¬Fogo | Fumaça → Fogo | ¬Fumaça → ¬Fogo | (Fumaça → Fogo) → (¬Fumaça → ¬Fogo)')

# N.4
t4 = [(a, b, neg(b), disj(a, b), disj(disj(a, b), neg(b))) for a in [0,1] for b in [0,1]]
print('4) Fumaça | Fogo | ¬Fogo | Fumaça ∨ Fogo | Fumaça ∨ Fogo ∨ ¬Fogo')

# N.5
t5 = [(a, b, c, conj(a, b), impl(a, c), impl(b, c), impl(conj(a, b), c), disj(impl(a, c), impl(b, c)), iff(impl(conj(a, b), c), disj(impl(a, c), impl(b, c)))) for a in [0,1] for b in [0,1] for c in [0,1]]
print('5) Fumaça | Calor | Fogo | Fumaça ∧ Calor | Fumaça → Fogo | Calor → Fogo | (Fumaça ∧ Calor) → Fogo | (Fumaça → Fogo) ∨ (Calor → Fogo) | ((Fumaça ∧ Calor) → Fogo) ⇐⇒ ((Fumaça → Fogo) ∨ (Calor → Fire))')

# N.6
t6 = [(a, b, c, impl(a, b), conj(a, c), impl(conj(a, c), b), impl(impl(a, b), impl(conj(a, c), b))) for a in [0,1] for b in [0,1] for c in [0,1]]
print('6) Fumaça | Fogo | Calor | Fumaça → Fogo | Fumaça ∧ Calor | (Fumaça ∧ Calor) → Fogo | (Fumaça → Fogo) → ((Fumaça ∧ Calor) → Fogo)')

# N.7
t7 = [(a, b, impl(a, b), disj(a, b), disj(disj(a, b), impl(a, b))) for a in [0,1] for b in [0,1]]
print('7) Grande | Bobo | Grande → Bobo | Grande ∨ Bobo | Grande ∨ Bobo ∨ (Grande → Bobo)')

# N.8
t8 = [(a, b, neg(b), conj(a, b), disj(conj(a, b), neg(b))) for a in [0,1] for b in [0,1]]
print('8) Grande | Bobo | ¬Bobo | Grande ∧ Bobo | (Grande ∧ Bobo) ∨ ¬Bobo')

atividades = [t1, t2, t3, t4, t5, t6, t7, t8]

print('')
for atividade in atividades:
    print(f'{atividades.index(atividade) + 1})')
    validador = 0
    for row in atividade:
        print(row)
        if row[-1] == 1:
            validador += 1

    if validador == len(atividade):
        print('Tautologia')

    elif validador == 0:
        print('Contradição')

    else:
        print('Contingência')
    
    print('')

#FIM :D