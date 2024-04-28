#Exercício A.1:
num = *range(0, 25),
dec = num

def conversor(number, base):
    base_string = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    while number:
        result += base_string[number % base]
        number //= base
    return result[::-1] or "0"


binario= []
for i in num:
    binario.append(bin(int(i))[2:])

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

    


print("Exercício A.1::")
print(f"Decimal: {dec}")
print(f"Binario: {binario}")
print(f"Quinario: {quinario}")
print(f"Octal: {octal}")
print(f"Undecimal: {undecimal}")
print(f"Duodecimal: {duodecimal}")
print(f"Hexadecimal: {hexadecimal}")
print(f"Vigesimal: {vigesimal}")






#considera-se 0 como o primeiro número.