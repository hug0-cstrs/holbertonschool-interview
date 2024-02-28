#include "palindrome.h"

/**
 * is_palindrome - vérifie si un nombre est un palindrome
 * @n: nombre à vérifier
 * Return: 1 si c'est un palindrome, 0 sinon
 */
int is_palindrome(unsigned long n)
{
	unsigned long reversed = 0, remainder, original;

	original = n;

	while (n != 0)
	{
		remainder = n % 10;
		reversed = reversed * 10 + remainder;
		n /= 10;
	}

	if (original == reversed)
		return (1);
	else
		return (0);
}
