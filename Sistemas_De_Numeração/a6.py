#Solution for exercise a6
def converte_base(numeral):

    caracteres_valores = "ZABCDEFGHIJKLMNOPQRSTUVWXY"
    soma = 0

    numeral_invertido = numeral[::-1]

    for indice, caracter in enumerate(numeral_invertido):
        if caracter in caracteres_valores:
            valor = caracteres_valores.index(caracter)
            soma += (valor * (26**indice))

    print(soma)
    return soma

converte_base("YOU")
converte_base("SHALL")
converte_base("NOT")
converte_base("PASS")