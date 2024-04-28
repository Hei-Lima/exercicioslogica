#Solution for exercise a19

def main():
    
    list = [50533, 44772, 7675, 761, 3530, 43160, 5571, 552, 174]
    decList = []
    hexList = []
    
    def octalToDec(num):
        decimal_value = 0
        base = 1
        while (num):
            last_digit = num % 10
            num = int(num / 10)
            decimal_value += last_digit * base
            base = base * 8
        return decimal_value

    i = 0
    for i in range(len(list)):
        decList.append(octalToDec(list[i]))
        hexList.append(hex(decList[i]))
        print(f'{i+1}. {hexList[i][2:]}')
        i += 1

    return 0

if __name__ == "__main__":
    main()