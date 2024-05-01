def complemento_de_dois(num, bits):
    binario = bin(abs(num))[2:]
    binario = binario.zfill(bits)

    if num > 0:
        resultado = binario
    else:
        binario_invertido = trocar_caracteres(binario)
        resultado = bin(int(binario_invertido, 2) + 1)[2:]
        resultado = resultado.zfill(bits)
  
    return resultado  

def trocar_caracteres(num):
    return ''.join(['1' if char == '0' else '0' for char in num])