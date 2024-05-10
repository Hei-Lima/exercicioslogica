from complemento_de_dois import complemento_de_dois


#Essa função de soma foi gerada por IA, mas foi devidamente corrigida
def soma_complemento_de_dois(a, b, bits=8):
    a_int = int(a, 2)
    b_int = int(b, 2)

    '''O limite de um numero positivo de 8 bits é 127 == 2**(8-1), logo
    todo numero igual ou maior que 128 é um numero negativo'''
    if a_int >= 2**(bits-1):
        '''Aqui ele ta definindo qual o numero negativo, no caso de a_int ser
    130(maior que 128, logo, negativo), vc subtrai de 2 elevado ao numero de
    bits utilizado. Então 130 - 256(2**8) = -126'''
        a_int -= 2**bits
    if b_int >= 2**(bits-1):
        b_int -= 2**bits

    soma = a_int + b_int

    return complemento_de_dois(soma, bits)


exercicios = [
    ("10111100", "00001000"),
    ("11010010", "11110010"), 
    ("00000010", "10111100"), 
    ("00001100", "00001000"),
    ("00001000", "00000011"),
    ("00100000", "00111010"),
    ("01111110", "01111111"),
    ("00001001", "00100000"),
    ("01101010", "01010000"),
    ("00101101", "00101101"),
]

for i, (a, b) in enumerate(exercicios, start=1):
    resultado = soma_complemento_de_dois(a, b)
    print(f"({i}) {a} + {b} = {resultado}")