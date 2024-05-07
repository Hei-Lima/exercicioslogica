def trocar_caracteres(num):
    return ''.join(['1' if bit == '0' else '0' for bit in num])

def complemento_de_dois(num):
    if num[-1] == "1":
        num = bin(int(num, 2) - 1)[2:]
        num = trocar_caracteres(num)
    num = int(num, 2)     

    return num

numeros = ["0010100101","0010101100","1110110101","0000001011","1000010011","1100111010","1110101010",
"1000110111", "1000110011", "1011111000", "0111101110", "0101010011"]

complementos = [complemento_de_dois(num) for num in numeros]

for indice, resultado in enumerate(complementos, start=1):
    print(f"{indice}. {resultado}")