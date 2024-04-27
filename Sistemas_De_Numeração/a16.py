#Solution for exercise a16

def main():


    list = [365, 5267, 4612, 170742, 161051, 465, 3420, 6341, 32575]
    i = int(1)
    for num in list:
        #This code formats the num by stripping unwanted char
        hex = format(num, 'x').upper()
        print(f"{i}. {hex:<5}")
        i += 1

    #The function "<5" aligns the text to the left within a five-character space.

    return 0
if __name__ == '__main__':
    main()