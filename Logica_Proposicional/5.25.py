
def neg(x):
    return 1 - x

def conj(x,y):
    return 1 if x+y == 2 else 0

def disj(x,y):
    return 0 if x+y == 0 else 1

def impl(x,y):
    return 1 if x == 0 or y == 1 else 0;

def xor(x,y):
    return 0 if x == y else 1;

def iff(x,y):
    return 1 if x == y else 0;


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

# # N.5
# t1 = [(a, impl(a, a)) for a in [0,1]]
# print('1) Fumaça | Fumaça → Fumaça')

# # N.6
# t1 = [(a, impl(a, a)) for a in [0,1]]
# print('1) Fumaça | Fumaça → Fumaça')

# # N.7
# t1 = [(a, impl(a, a)) for a in [0,1]]
# print('1) Fumaça | Fumaça → Fumaça')

# # N.8
# t1 = [(a, impl(a, a)) for a in [0,1]]
# print('1) Fumaça | Fumaça → Fumaça')

atividades = [t1, t2, t3, t4]

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
