#Solution for exercise a14

def main():

  list = [10, 31, 100, 120, 127, 254, 1025, 4094, 65535]
  print(f"{'BIN':<16} {'OCT':<6} {'HEX':<5}") #Head
  print("----------------------------------") 

  for num in list:
    #This code formats the num by stripping unwanted char
    bin = format(num, 'b')
    oct = format(num, 'o')
    hex = format(num, 'x').upper()

    #The function "<5" aligns the text to the left within a five-character space.
    print(f"{bin:<16} {oct:<6} {hex:<5}")

if __name__ == "__main__":  
  main()