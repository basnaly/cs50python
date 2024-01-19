def main():

    amount_due = 50
    while amount_due > 0:
        print(f'Amount Due: {amount_due}')
        coin = input('Insert Coin: ')
        if coin != 25 and coin != 10 and coin != 5:
            continue
        amount_due = amount_due - coin
    print(f"Change Owed: {amount_due}")


main()
