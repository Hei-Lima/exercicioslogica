import math
### Seguindo o conceito de alfabeto real, é improvavel checar se uma determinada lista de números é um alfabeto. Por isso, importei uma lista com os 3 alfabetos mais famosos.
###JSON da lista: https://gist.githubusercontent.com/Hei-Lima/45c9917535d7d0b3b44d60939e8ba255/raw/412fc0bb59905eab6d9823f6706eb171f35c64bb/alphabets.json
latin =  {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}
cyrilic = {"А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З", "И", "Й", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т", "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ъ", "Ы", "Ь", "Э", "Ю", "Я", "а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"}
greek = {"Α", "Β", "Γ", "Δ", "Ε", "Ζ", "Η", "Θ", "Ι", "Κ", "Λ", "Μ", "Ν", "Ξ", "Ο", "Π", "Ρ", "Σ", "Τ", "Υ", "Φ", "Χ", "Ψ", "Ω", "α", "β", "γ", "δ", "ε", "ζ", "η", "θ", "ι", "κ", "λ", "μ", "ν", "ξ", "ο", "π", "ρ", "σ", "τ", "υ", "φ", "χ", "ψ", "ω"}
#Exercício 8:


def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
        
    return True

primos = set(i for i in range(1000) if isPrime(i) == True)

def check(x):
    if x == latin or x == greek or x == cyrilic:
        return "Alfabeto"
    else:
        return "Não é alfabeto"


print("Exercício 8:")

print(f'1. {check(set(range(1000)))}')
print(f'2. {check(primos)}')
print(f'3. {check(latin)}')
print(f'4. {check({range(0, 9)})}')
print(f'5. {check({"I", "V", "X", "L"})}')
print(f'6. {check({"a, b, c, d, e"})}')
print(f'7. {check({"a", "e", "i", "o", "u"})}')
print(f'8. {check(greek)}')



