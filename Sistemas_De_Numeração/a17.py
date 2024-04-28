#Solution for exercise a17

def main():
    
    list = [110101010, 100100010, 10100000, 101001, 10100101000, 111101001111, 1100100110, 10110100100, 111001111110]
    decList = []
    octList = []
    
    def binToDec(binary):
 
        decimal, i = 0, 0
        while(binary != 0):
            dec = binary % 10
            decimal = decimal + dec * pow(2, i)
            binary = binary//10
            i += 1
        return decimal

    i = 0
    for i in range(len(list)):
        decList.append(binToDec(list[i]))
        octList.append(oct(decList[i]))
        print(f'{i+1}. {octList[i][2:]}')
        i += 1

if __name__ == "__main__":
    main() 