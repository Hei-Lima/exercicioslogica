#Solution for exercise a26
#A solução de como calcular complemento de dois esta no arquivo a25
from complemento_de_dois import complemento_de_dois
def main():
    lista1 = [7, 6, 5, 4, 3, 2, 1]
    print(f"{'DECIMAL':<16}{'Complemento de 2':<16}") #Head
    print("----------------------------------") 

    for num in lista1:
        print(f"{num:<16}{complemento_de_dois(num, 4):<16}")
    

    lista2 = [-1,-2,-3,-4,-5,-6,-7,-8]
    print()
    print(f"{'DECIMAL':<16}{'Complemento de 2':<16}") #Head
    print("----------------------------------") 

    for num in lista2:
        print(f"{num:<16}{complemento_de_dois(num, 4):<16}")

if __name__ == "__main__":
    main()