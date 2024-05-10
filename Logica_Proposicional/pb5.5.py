from itertools import product

# Função auxiliar para simular o operador "implica"
def implies(a, b):
    return not a or b

def eval_formula(formula, values):
    # Avalia a fórmula usando a função 'eval' com um ambiente que inclui a função 'implies'
    return eval(formula, {"implies": implies}, values)

def is_tautology(results):
    return all(results)

def is_contradiction(results):
    return not any(results)

def is_contingency(results):
    return not is_tautology(results) and not is_contradiction(results)

# Dicionário de fórmulas com a substituição correta para o operador "implica"
formulas = {
    'a': 'implies(A and B, A)',
    'b': 'not P and (P and Q)',
    'c': 'P or (Q and (not P or not Q))',
    'd': 'implies(A, implies(B, A and B))',
    'e': 'implies(P, implies(False, not P))'
}

variables = {
    'a': ['A', 'B'],
    'b': ['P', 'Q'],
    'c': ['P', 'Q'],
    'd': ['A', 'B'],
    'e': ['P']
}

for key, formula in formulas.items():
    print(f"Formula {key.upper()}: ")
    print(f"{formula}")
    results = []
    for values in product([False, True], repeat=len(variables[key])):
        val_dict = dict(zip(variables[key], values))
        result = eval_formula(formula, val_dict)
        results.append(result)
        print(f"{val_dict} => {result}")
    
    if is_tautology(results):
        print("Result: Tautoloiag\n")
    elif is_contradiction(results):
        print("Result: Contradição\n")
    elif is_contingency(results):
        print("Result: Contingência\n")