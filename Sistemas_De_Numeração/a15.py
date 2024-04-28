#Solution for exercise a15
from conversor_bases import conversor

def main():

    lista = [15, 45, 153, 211, 272, 549, 1023, 4949, 65535]
    print(f"{'Questoes':<10}{'BASE 5':<6} {'BASE 7':<6}") #Head
    print("----------------------------------") 

    for num in lista:
        pent = conversor(num, 5)
        hept = conversor(num, 7)
        indice = lista.index(num)

    print(f"{indice+1:<10} {pent:<10} {hept:<10}")

if __name__ == "__main__":  
  main()