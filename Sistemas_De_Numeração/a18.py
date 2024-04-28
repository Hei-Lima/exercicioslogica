#Solution for exercise a18

def main():
    
    list = [1110100001010, 1010110010001001, 11100111111,  10100101111, 10101111, 1111100110100, 1111010111, 1011111010,  110010110]
    #Note: for some values the first row of 0's must be disregarded when calculated
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
        octList.append(hex(decList[i]))
        print(f'{i+1}. {octList[i]}')
        i += 1

if __name__ == "__main__":
    main()