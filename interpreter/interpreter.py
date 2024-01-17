def main():
    expression = input("Expression: ").strip()
    x, y, z = expression.split(' ')
    print(x)
    print(y)
    print(z)
    match y:
        case y == '+':
            print(int(x) + int(z))
        case y == '-':
            print(int(x) - int(z))
        case y == '*':
            print(int(x) * int(z))
        case y == '/':
            print(int(x) / int(z))


main()
