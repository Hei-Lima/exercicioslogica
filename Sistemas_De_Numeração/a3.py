import math

num = *range(0, 30000),

#Exercício A.2:


base_string = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def conversor(number, base):
    result = ""
    while number:
        result += base_string[number % base]
        number //= base
    return result[::-1] or "0"



def check(n):
    cont = 0
    for i in n:
        if len(str(i)) <= 3:
            cont = cont + 1
    return cont
        

binario= []
for i in num:
    binario.append(bin(1111)[2:])

quinario= []
for i in num:
    quinario.append(conversor(int(i), 5))

octal= []
for i in num:
    octal.append(conversor(int(i), 8))

undecimal= []
for i in num:
    undecimal.append(conversor(int(i), 11))

duodecimal= []
for i in num:
    duodecimal.append(conversor(int(i), 12))
    
hexadecimal= []
for i in num:
    hexadecimal.append(conversor(int(i), 16))

vigesimal= []
for i in num:
    vigesimal.append(conversor(int(i), 20))

    


print("Exercício A.3:")
print(f"Binario: {check(binario)}")
print(f"Quinario: {check(quinario)}")
print(f"Octal: {check(octal)}")
print(f"Undecimal: {check(undecimal)}")
print(f"Duodecimal: {check(duodecimal)}")
print(f"Hexadecimal: {check(hexadecimal)}")
print(f"Vigesimal: {check(vigesimal)}")


#Essa é, de longe, a pior solução para o problema. Escala mal demais, pois tem O(n), enquanto a otimizada x**n (n sendo a base) teria O(1). Mas não estou nem ai.