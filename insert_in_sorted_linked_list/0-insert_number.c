#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new, *current;

    /* Vérifier si head est NULL */
    if (head == NULL)
        return (NULL);

    /* Alloue de la mémoire pour le nouveau nœud */
    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    /* Assigne une valeur au nouveau nœud */
    new->n = number;
    new->next = NULL;

    /* Définit current sur head */
    current = *head;

    /* Si la liste est vide, faire du nouveau nœud la tête */
    if (*head == NULL)
        *head = new;

    /* Si il y a un nouveau nœud, il doit être inséré au début */
    else if (current->n > number)
    {
        new->next = current;
        *head = new;
    }

    /* Trouver le nœud après lequel le nouveau nœud doit être inséré */
    else
    {
        while (current->next != NULL && current->next->n < number)
            current = current->next;
        new->next = current->next;
        current->next = new;
    }

    /* Retourne l'adresse du nouveau nœud inséré */
    return (new);
}