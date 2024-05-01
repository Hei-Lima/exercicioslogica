#Solution for exercise a25

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


print(f'''1. {complemento_de_dois(12, 5)} 
2. {complemento_de_dois(10,5)}
3. {complemento_de_dois(-7,5)}
4. {complemento_de_dois(-10,5)}
5. {complemento_de_dois(3,5)}
6. {complemento_de_dois(-9,5)}
7. {complemento_de_dois(15,5)}
8. {complemento_de_dois(-4,5)}
9. {complemento_de_dois(-15,5)}
10. {complemento_de_dois(-3,5)}
11. {complemento_de_dois(11,5)}
12. {complemento_de_dois(-1,5)}''')