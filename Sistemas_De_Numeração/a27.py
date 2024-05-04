def trocar_caracteres(num):
    return ''.join(['1' if bit == '0' else '0' for bit in num])

def complemento_de_dois(num):
    num = num.zfill(12)
    inversao = trocar_caracteres(num)
    binario = bin(int(inversao, 2) + 1)[2:]
    return binario.zfill(12)

numeros = ["1011101","11010111","1011101111","10101001100","1011110111","11011011"]

complementos = [complemento_de_dois(num) for num in numeros]

for indice, resultado in enumerate(complementos, start=1):
    print(f"{indice}. {resultado}")