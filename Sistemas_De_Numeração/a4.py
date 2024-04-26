def menor_base(numero):
    numero = numero.upper()
    maior_numero = 0
    letras = {'A': 10, "B":11, "C":12, "D":13, "E":14, "F":15}

    for caracter in numero:
        if caracter.isdigit():
            valor = int(caracter)
        elif caracter in letras:
            valor = letras[caracter]

        if valor > maior_numero:
            maior_numero = valor    
        
    base_minima = maior_numero + 1
    return base_minima    


print(f'''a. {menor_base("0")}
b. {menor_base("1101")}
c. {menor_base("777")}
d. {menor_base("1024")}
e. {menor_base("666")}
f. {menor_base("1EE7")}
g. {menor_base("A5A")}      
h. {menor_base("B1A")}''')