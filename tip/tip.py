
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # Convert d(argument) to float and return it
    return float(d.replace("$", ""))


def percent_to_float(p):
    # Remove char % from p, convert it to float, divide by 100 and return it
    return float(p.replace("%", ""))/100

main()
