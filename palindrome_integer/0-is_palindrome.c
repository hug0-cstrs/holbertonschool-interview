#include "palindrome.h"

/**
 * is_palindrome - checks if a number is a palindrome
 * @num: number to check
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int is_palindrome(unsigned long num)
{
    unsigned long reversed = 0, last_digit, original;

    original = num;

    while (num != 0)
    {
        last_digit = num % 10; // get the last digit
        reversed = reversed * 10 + last_digit; // add the last digit to the reversed number
        num /= 10; // remove the last digit from the original number
    }

    if (original == reversed)
        return (1);
    else
        return (0);
}
