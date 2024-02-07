#include "lists.h"

/**
 * is_palindrome - vérifie si une liste chaînée est un palindrome
 * @head: pointeur vers le pointeur du premier noeud de la liste listint_t
 * Return: 0 si ce n'est pas un palindrome, 1 si c'est un palindrome
 */

int is_palindrome(listint_t **head)
{
  listint_t *current; /* Pointeur vers le noeud actuel */
  int i, j, len;
  int arr[10]; /* Tableau pour stocker les valeurs de la liste */

  if (*head == NULL) /* Si la liste est vide, c'est un palindrome */
    return (1);

  current = *head; /* Initialisation du pointeur actuel */
  len = 0; /* Initialisation de la longueur */

  while (current != NULL) /* Parcours de la liste pour stocker les valeurs dans le tableau */
  {
    arr[len] = current->n; /* Stocke la valeur du noeud actuel dans le tableau */
    current = current->next; /* Passe au noeud suivant */
    len++; /* Incrémente la longueur */
  }

  for (i = 0, j = len - 1; i < len / 2; i++, j--) /* Parcours le tableau pour vérifier si c'est un palindrome */
  {
    if (arr[i] != arr[j]) /* Si les valeurs ne correspondent pas, ce n'est pas un palindrome */
      return (0);
  }

  return (1); /* Si toutes les valeurs correspondent, c'est un palindrome */
}
