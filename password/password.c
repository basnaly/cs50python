// Check that a password has at least one lowercase letter, uppercase letter, number and symbol
// Practice iterating through a string
// Practice using the ctype library

#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

bool valid(string password);

int main(void)
{
    string password = get_string("Enter your password: ");
    if (valid(password))
    {
        printf("Your password is valid!\n");
    }
    else
    {
        printf("Your password needs at least one uppercase letter, lowercase letter, number and symbol\n");
    }
}

// TODO: Complete the Boolean function below
bool valid(string password)
{
    int length = strlen(password);
    bool is_digit;
    bool is_lower;
    bool is_upper;
    bool is_punct;
    for (int i = 0;  i < length; i++)
    {
        if (isdigit(password[i])
        {
            is_digit == true;
        }
        else if (islower(password[i])
        {
            is_lower == true;
        }
        else if (isupper(password[i])
        {
            is_upper == true;
        }
        else if (ispunct(password[i])
        {
            is_punct == true;
        }
    }
    if (is_digit == true && is_lower == true && is_upper == true && is_punct == true)
    {
        return true;
    }
    return false;
}
