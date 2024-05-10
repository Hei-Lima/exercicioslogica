#Resolution for the exercise 5.2 (p. 115 on pdf; p. 97 on book page)

def main():

    a = True
    b = False
    c = True

    print(f"""1. {a and (b or c)}
2. {((a and b) or c)}
3. {not(a and b) or c}
4. {not a or not(not b and c)}""")

    return 0
if __name__ == '__main__':
    main()