def main():

    amount_due = 50
    while amount_due > 0:
        print(f'Amount Due: {amount_due}')
        coin = int(input('Insert Coin: '))
        if coin != 25 and coin != 10 and coin != 5:
            continue
        else:
            amount_due = amount_due - coin
    if amount_due < 0:
        print(f"Change Owed: {abs(amount_due)}")


main()
