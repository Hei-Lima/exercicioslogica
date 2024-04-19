import math

num = 1111

#Exercício A.3:


base_string = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def conversor(number, base):
    result = ""
    while number:
        result += base_string[number % base]
        number //= base
    return result[::-1] or "0"



def check(n):
    return len(str(n))
       

binario = bin(num)[2:]

quinario = conversor(num, 5)

octal= (conversor(num, 8))

undecimal= (conversor(num, 11))


duodecimal= (conversor(num, 12))

    
hexadecimal= (conversor(num, 16))


vigesimal= (conversor(num, 20))    

print("Exercício A.3:")
print(f"Binario: {check(binario)}")
print(f"Quinario: {check(quinario)}")
print(f"Octal: {check(octal)}")
print(f"Undecimal: {check(undecimal)}")
print(f"Duodecimal: {check(duodecimal)}")
print(f"Hexadecimal: {check(hexadecimal)}")
print(f"Vigesimal: {check(vigesimal)}")


