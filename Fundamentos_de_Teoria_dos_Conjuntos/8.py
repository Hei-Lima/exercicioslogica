### A implementação de um set com infinitos elementos em python é complicada, por vários motivos. Por isso, escolhi definir infinito como o maior inteiro de 16bits.
import math
import requests
req = requests.get('https://gist.githubusercontent.com/Hei-Lima/d609c5f1ff052aa80948ae43dc6c7a0f/raw/f571df63d238e63703d36b09e2760485fe11b14a/countries.json').json()
#from sympy import *

#Exercício 8:

inf = 2**16
infp = inf * 10

def isEven(x):
    if x % 2:
        return "even"
    else:
        return "odd"

A = set(range(10, infp))
C = set((i['name'] for i in req))
E = set(range(0, 2010))
F = set()

for i in range(infp):
    if isEven(i) == "even":
        F.add(i)

#for i in range(infp):
#    if isprime(i) == True:
#        B.add(i)

def isInf(x):
    if len(x) >= inf:
        return "I (infinito)"
    else: 
        return "F (Finito)"



print("Exercício 8:")


print(f"1. {isInf(A)}")
print(f"2. I (infinito)") #Não tem como checar computacionalmente de forma simples que os primos são infinitos(https://pt.wikipedia.org/wiki/N%C3%BAmero_primo). Então não vou fazer isso. Quem quiser atirar, tem ali a função.
print(f"3. {isInf(C)}")
print(f"4. I (infinito)") #Não tem como criar um set deste tipo, mas tenho bastante certeza que não está errado.
print(f"5. {isInf(E)}")
print(f"6. {isInf(F)}")
print(f"7. I (infinito)") #Existem infinitos conjuntos-solução para a função: https://www.desmos.com/calculator/rq7aew7swl
print(f"8. I (infinito)") #Existem infinitos conjuntos-solução para a função: https://www.desmos.com/calculator/bdn128t8e3



#TODO: Dá pra fazer a 7 e a 8 por programa

