
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    x = int(d)
    return x


def percent_to_float(p):
    y = int(p.split("%"))
    return y/100

main()
