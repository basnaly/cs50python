#include <cs50.h>
#include <stdio.h>

int get_cents(void);
int calculate_quarters(int cents);
int calculate_dimes(int cents);
int calculate_nickels(int cents);
int calculate_pennies(int cents);

int main(void)
{
    // Ask how many cents the customer is owed
    int cents = get_cents();

    do
    {
        cents = get_int("Number of cents: ");
    }
    while (cents < 0);

    printf("Number of cents: %i\n", cents);

    // Calculate the number of quarters to give the customer
    int quarters = calculate_quarters(cents);

    quarters = cents / 25;

    cents = cents - quarters * 25;

    // Calculate the number of dimes to give the customer
    int dimes = calculate_dimes(cents);

    dimes = cents / 10;

    cents = cents - dimes * 10;

    // Calculate the number of nickels to give the customer
    int nickels = calculate_nickels(cents);

    nickels = cents / 5;

    cents = cents - nickels * 5;

    // Calculate the number of pennies to give the customer
    int pennies = calculate_pennies(cents);

    pennies = cents / 1;

    cents = cents - pennies * 1;

    // Sum coins
    int coins = quarters + dimes + nickels + pennies;

    // Print total number of coins to give the customer
    printf("%i\n", coins);
}

int get_cents(cents)
{
    // TODO
    return cents;
}

int calculate_quarters(int cents)
{
    // TODO
    return quarters;
}

int calculate_dimes(int cents)
{
    // TODO
    return dimes;
}

int calculate_nickels(int cents)
{
    // TODO
    return nickels;
}

int calculate_pennies(int cents)
{
    // TODO
    return pennies;
}
