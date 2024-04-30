#Solution for exercise a21
from conversor_bases import conversor

def soma_bases(numeral1, numeral2, base):

    numeral1 = int(numeral1, base)
    numeral2 = int(numeral2, base)
    soma_numerais = numeral1 - numeral2

    conversao = conversor(soma_numerais, base)
    
    return conversao

print(f'''1. {soma_bases("100101101", "10110010", 2)} 
2. {soma_bases("10011", "101110", 2)}
3. {soma_bases("1100100", "1011", 2)}
4. {soma_bases("110000110", "10111000", 2)}
5. {soma_bases("3121020", "1212131", 4)}
6. {soma_bases("123020", "122302", 4)}
7. {soma_bases("3132320", "2202122", 4)}
8. {soma_bases("232021", "230001", 4)}
9. {soma_bases("5153778", "35502138", 8)}
10. {soma_bases("2204420", "57743", 8)}
11. {soma_bases("5512", "6014118", 8)}
12. {soma_bases("4560407", "2521118", 8)}
13. {soma_bases("6870B", "B2B917", 12)}
14. {soma_bases("86712", "1423", 12)}
15. {soma_bases("41308A", "96599", 12)}
16. {soma_bases("9BA29B", "48A50", 12)}
17. {soma_bases("66BA94", "49FEC", 16)}
18. {soma_bases("A27A42", "A7FD72", 16)}
19. {soma_bases("C7C83", "1855BC", 16)}
20. {soma_bases("9337C", "30BDE4", 16)}''')

