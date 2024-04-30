#Solution for exercise a23
def main():
    from conversor_bases import conversor

    def mult_bases(numeral1, numeral2, base):

        numeral1 = int(numeral1, base)
        numeral2 = int(numeral2, base)
        soma_numerais = numeral1 * numeral2

        conversao = conversor(soma_numerais, base)
        
        return conversao

    print(f'''1. {mult_bases("1100", "11101", 2)} 
2. {mult_bases("1011010", "10100", 2)}
3. {mult_bases("10010", "110100", 2)}
4. {mult_bases("101001", "10100", 2)}
5. {mult_bases("32210", "12033", 4)}
6. {mult_bases("30101", "20121", 4)}
7. {mult_bases("3212", "13013", 4)}
8. {mult_bases("1033", "21132", 4)}
9. {mult_bases("562", "6606", 8)}
10. {mult_bases("73042", "10764", 8)}
11. {mult_bases("7140", "3071", 8)}
12. {mult_bases("7422", "145", 8)}
13. {mult_bases("4564", "2B4", 12)}
14. {mult_bases("942", "B10", 12)}
15. {mult_bases("7B5", "278", 16)}
16. {mult_bases("17A2", "A35", 16)}
17. {mult_bases("9A", "20", 16)}
18. {mult_bases("89", "109", 16)}
19. {mult_bases("0787", "36", 16)}
20. {mult_bases("5B0", "B9", 16)}''')

if __name__ == '__main__':
    main()