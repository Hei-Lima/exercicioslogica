#Solution for exercise a20

def main():
    
    list = ['bb7', 'fe4', '2c5', '1b37e', '062fc', '5e68', 'a2', 'da572', '540f']
    octList = []

    def hexToOct(hex_number):
        # Convert hexadecimal 
        decimal_number = int(hex_number, 16)
        
        # Convert decimal to octal
        octal_number = oct(decimal_number)
        
        # Return the octal representation
        return octal_number

    i = 0
    for i in range(len(list)):
        octList.append(hexToOct(list[i]))
        print(f'{i}. {octList[i][2:]}')
        i += 1

if __name__ == "__main__":
    main()