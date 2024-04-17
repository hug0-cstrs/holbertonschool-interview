#include "search.h"

/**
 * linear_skip - searches for a value in a sorted sk list of integers.
 * @list: pointer to the head of the sk list to search in
 * @value: value to search for
 *
 * Return: value
**/
skiplist_t *linear_skip(skiplist_t *list, int value)
{
	skiplist_t *sk, *prev;

	if (!list) /* Verifie si la liste est vide */
		return (NULL);

  /* Initialise sk à la piste express et prev au nœud précédent */
	sk = list->express; /* Pointeur sk pour la liste express */
	prev = list; /* Pointeur prev pour le nœud précédent */

  /* Parcourt la liste jusqu'à ce que sk soit NULL */
	while (sk)
	{
    /* Affiche les valeurs des nœuds actuels */
		printf("Value checked at index [%lu] = [%d]\n", sk->index, sk->n);

    /* Vérifie si sk est le dernier nœud ou si sa valeur est supérieure
    ou égale à celle recherchée */
		if (!sk->express || sk->n >= value)
		{
      /* Si sk est le dernier nœud et sa valeur est inférieure à celle recherchée */
			if (sk->n < value && !sk->express)
			{
				prev = sk; /* Met à jour prev */
				while (sk->next) /* Parcourt la liste jusqu'à la fin */
					sk = sk->next; /* Met à jour sk */
			}
      /* Affiche les indices entre lesquels la valeur recherchée pourrait
      se trouver */
			printf("Value found between indexes [%lu] and [%lu]\n", prev->index,
				sk->index);

      /* Parcourt les nœuds entre prev et sk pour rechercher la valeur */
			while (prev)
			{
        /* Affiche les valeurs des nœuds actuels */
				printf("Value checked at index [%lu] = [%d]\n", prev->index, prev->n);

        /* Vérifie si la valeur actuelle est supérieure à la valeur recherchée */
				if (prev->n > value)
					return (NULL);
        /* Vérifie si la valeur actuelle est égale à la valeur recherchée */
				if (prev->n == value)
					return (prev);
				prev = prev->next; /* Met à jour prev */
			}

      /* Sort de la boucle de recherche */
			break;
		}

    /* Met à jour prev et sk pour passer au prochain nœud sur la piste express */
		prev = sk;
		sk = sk->express;
	}
  /* Retourne null si la valeur n'a pas été trouvée */
	return (NULL);
}
