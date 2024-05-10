from complemento_de_dois import complemento_de_dois
def soma_complemento_de_dois(a, b, bits=8):
    a_int = int(a, 2)
    b_int = int(b, 2)
    soma = (a_int + b_int) % (1 << bits)
    return format(soma, f'0{bits}b')

exercicios = [(-103, -118),(-98, 25), (36, -124),(104, -82),(-26, -63),
(-2, 78), (83, -29),(41, 110),(118, 113),(-42, -12)]

for i, (a, b) in enumerate(exercicios, start=1):
    a_bin = complemento_de_dois(a, 8)
    b_bin = complemento_de_dois(b, 8)
    resultado_bin = soma_complemento_de_dois(a_bin, b_bin)
    print(f"({i}) {a_bin} + {b_bin} = {resultado_bin} -> {int(resultado_bin, 2) if resultado_bin[0] == '0' else int(resultado_bin, 2) - 256}")