def converte_base(numeral):

    caracteres_valores = {"★":3, "■": 0, "◆": 1, "▲": 2, "∞":4, "🎯": 5}
    soma = 0

    numeral_invertido = numeral[::-1]
    
    for indice, caracter in enumerate(numeral_invertido):
        if caracter in caracteres_valores:
            valor = caracteres_valores[caracter]
            soma += (valor * (6**indice))

    return soma

print(f'''{converte_base("◆■★")}
{converte_base("★■■🎯")}
{converte_base("∞◆★■")}
{converte_base("🎯■▲▲")}''')   