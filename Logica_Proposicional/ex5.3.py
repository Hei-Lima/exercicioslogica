#Resolution for exercise 5.3 (p. 116 on pdf; p. 98 on book page)

def main():

    def checkEven(x):
        if (x % 2 == 0):
            return True
        else:
            return False
    
    def checkOdd(x):
        if (x % 2 == 1):
            return True
        else:
            return False
    
    def condicional(y, z):
        if (y == False or (y == True and z == True)):
            return True
        else:
            return False
            
    def checkLesser(a, b):
        if (a < b):
            return True
        else:
            return False

    print(f"""1. {checkEven(8) or checkOdd(6)}
2. {checkEven(8) and checkOdd(6)}
3. {checkOdd(8) or checkOdd(6)}
4. {checkOdd(8) and checkOdd(6)}
5. {condicional(checkOdd(8), checkOdd(6))}
6. {condicional(checkEven(8), checkOdd(6))}
7. {condicional(checkOdd(8), checkEven(6))}
8. {condicional(checkOdd(8) and checkEven(6), checkLesser(8, 6))}""")

    return 0
if __name__ == '__main__':
    main()
