def trocar_caracteres(num):
    return ''.join(['1' if bit == '0' else '0' for bit in num])

def complemento_de_dois(num):
    if num[-1] == "1":
        num = bin(int(num, 2) - 1)[2:]
        num = trocar_caracteres(num) 

    return num


numeros = ["1101110111","0101000001","0101101001","1101001110","1001101001","0111101000","1101111101",
"1010000000", "0010101101", "0110001110", "1011001010", "0010100000"]

complementos = [complemento_de_dois(num) for num in numeros]

for indice, resultado in enumerate(complementos, start=1):
    print(f"{indice}. {resultado}")
