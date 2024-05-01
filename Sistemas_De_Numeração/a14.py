#Solution for exercise a14

def main():

  lista = [10, 31, 100, 120, 127, 254, 1025, 4094, 65535]
  print(f"{'BIN':<16} {'OCT':<6} {'HEX':<5}") #Head
  print("----------------------------------") 

  for num in lista:
    #This code formats the num by stripping unwanted char
    binario = format(num, 'b')
    octal = format(num, 'o')
    hexadecimal = format(num, 'x').upper()

    #The function "<5" aligns the text to the left within a five-character space.
    print(f"{binario:<16} {octal:<6} {hexadecimal:<5}")

if __name__ == "__main__":  
  main()