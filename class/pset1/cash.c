#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{
    float dollars;
    do 
    {
    dollars = get_float("Change owed : ");
    }
    while (dollars < 0);
    
    int cents = round(dollars * 100);
    
    int q = (float)cents / 25.0;
    int quarter = cents - 25*q;
    int d = (float)quarter / 10.0;
    int dime = quarter - 10*d;
    int n = (float)dime / 5.0;
    int nickel = dime - 5*n;
    int p = (float)nickel / 1.0;
    int penny = nickel - 1*p;
    
    int coins = q + d + n + p;
    printf("%d\n", coins);
}