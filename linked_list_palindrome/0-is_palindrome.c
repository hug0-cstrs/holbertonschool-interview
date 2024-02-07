#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of first node of listint_t list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *current;
	int i, j, len;
	int *arr;

	if (*head == NULL)
		return (1);

	current = *head;
	len = 0;
	while (current != NULL)
	{
		current = current->next;
		len++;
	}

	arr = malloc(len * sizeof(int));
	if (arr == NULL)
		return (0);

	current = *head;
	for (i = 0; i < len; i++)
	{
		arr[i] = current->n;
		current = current->next;
	}

	for (i = 0, j = len - 1; i < len / 2; i++, j--)
	{
		if (arr[i] != arr[j])
		{
			free(arr);
			return (0);
		}
	}

	free(arr);
	return (1);
}
