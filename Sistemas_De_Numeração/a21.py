#Solution for exercise a21
from conversor_bases import conversor

def soma_bases(numeral1, numeral2, base):

    numeral1 = int(numeral1, base)
    numeral2 = int(numeral2, base)
    soma_numerais = numeral1 + numeral2

    conversao = conversor(soma_numerais, base)
    
    return conversao

print(f'''1. {soma_bases("01010110", "1000110", 2)} 
2. {soma_bases("1110000", "100111", 2)}
3. {soma_bases("100110000", "100111101", 2)}
4. {soma_bases("000001001", "111001", 2)}
5. {soma_bases("1211030", "32000", 4)}
6. {soma_bases("1331331", "3301122", 4)}
7. {soma_bases("3120322", "1121000", 4)}
8. {soma_bases("23301", "1231030", 4)}
9. {soma_bases("505052", "4034", 8)}
10. {soma_bases("4306", "77166", 8)}
11. {soma_bases("43254", "132042", 8)}
12. {soma_bases("327104", "373277", 8)}
13. {soma_bases("6A41", "310", 12)}
14. {soma_bases("6A5B50", "BA342", 12)}
15. {soma_bases("75A6B4", "786625", 12)}
16. {soma_bases("798A2", "749220", 12)}
17. {soma_bases("4DE058", "564DF", 16)}
18. {soma_bases("85DE", "F1365E", 16)}
19. {soma_bases("E2C1", "A123", 16)}
20. {soma_bases("64FA4D", "E5AFFE", 16)}''')

