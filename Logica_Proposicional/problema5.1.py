'''This code tries to verify if a sentence is a proposition or not. 
However, situations such as code ambiguity cannot be checked with simple code,
therefore, this code does not cover these situations.I will leave a note when 
the quoted sentence is ambiguous.'''

def verifica_proposicao(frase):

    palavras_anulatorias = ["eu", "ele", "ela", "lá", "agora", "sempre", "nunca", "nenhum"]

    if not frase.strip():
        return False

    if frase.strip().endswith("?") or frase.strip().endswith("!"):
        return False
    
    for palavra in palavras_anulatorias:
        if palavra in frase.lower().split():
            return False
    
    return True

frases = ["Fernando cozinho demais a couve-flor", "Não existe força que possa parar você"
          ,"Estava muito escuro lá", "Meus amigos foram a mata colher cogumelos",
          "Renata se esgueirou para dentro da cozinha", "Paula se grudou na parede recem pintada(Esse é um exemplo de ambiguidade)"
          ,"Se Fred Astaire não fosse um dançarino, Greta Garbo não seria uma atriz", "Se ao menos as crianças soubessem mais do que seus pais!"
          , "Será que o Henrique algum dia vai gostar de garotas?","Floriano Peixoto é uma mulher"]

for frase in frases:
    print(f"'{frase}' e uma proposicao" if verificaProposicao(frase) else f"'{frase}' nao e proposicao")