def main():
    # Remove spaces in user's input
    expression = input("Expression: ").strip()
    # Split user's input by ' '
    x, y, z = expression.split(' ')
    match y:
        case'+':
            print(float(x) + float(z))
        case '-':
            print(float(x) - float(z))
        case '*':
            print(float(x) * float(z))
        case '/':
            print(f'{float(x) / float(z):.1f}')


main()
