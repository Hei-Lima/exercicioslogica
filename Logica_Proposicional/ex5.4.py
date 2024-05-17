def encontrar_antecedente_consequente(proposicao):
    partes = proposicao.split("->")
    antecedente = partes[0].strip()
    consequente = partes[1].strip()
    return antecedente, consequente


'''
a. O crescimento sadio de plantas é consequência de quantidade suficiente de água.
    A: Crescimento sadio de plantas
    B: Quantidade suficiente de água
    A -> B

b. O aumento da disponibilidade de informação é uma condição necessária para um maior desenvolvimento tecnológico.
    A: Aumento da disponibilidade de informação
    B: Maior desenvolvimento tecnológico
    A -> B

c. Serão introduzidos erros apenas se forem feitas modificações no programa.
    A: Serão introduzidos erros
    B: Modificações no programa
    B -> A  

d. A economia de energia para aquecimento implica boa insulação ou vedação de todas as janelas.
    A: Economia de energia para aquecimento
    B: Boa insulação ou vedação de todas as janelas
    A -> B
'''

proposicoes =["A -> B", "A -> B", "B -> A", "A -> B"]

for indice, proposicao in enumerate(proposicoes):
    antecedente, consequente = encontrar_antecedente_consequente(proposicao)
    print(f"{indice+ 1}) Antecedente: {antecedente}, Consequente: {consequente}")