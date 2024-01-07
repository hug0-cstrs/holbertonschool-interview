#!/usr/bin/python3

'''
This module contains a function to determine
if all the lockboxes can be unlocked.

The function `canUnlockAll` takes a list of lists `boxes` as input,
where each inner list represents a lockbox and contains the indices
of the other lockboxes that can be opened with its key.
The function returns True if all the lockboxes can be unlocked,
and False otherwise.

Example usage:
boxes = [[1], [2], [3], []]
print(canUnlockAll(boxes))  # Output: True
'''


def canUnlockAll(boxes):
    # Créer une liste pour suivre les boîtes ouvertes
    unlocked_boxes = [False] * len(boxes)
    unlocked_boxes[0] = True  # Ondéfinit la première boîte comme déjà ouverte

    # On créer une pile (stack) pour effectuer une recherche dans les boîtes
    stack = [0]  # Commencer avec la première boîte

    # Parcourir toutes les boîtes qui sont accessibles
    while stack:
        # On prend la boîte qui est en haut de la pile (stack)
        current_box = stack.pop()

        # On parcours toutes les boîtes accessibles
        # avec les clés de la boîte courante
        for key in boxes[current_box]:
            # On vérifie si la boîte n'est pas déjà ouverte
            if key < len(boxes) and not unlocked_boxes[key]:
                # Si la boîte n'est pas ouverte, on met sa valeur à True
                # (donc ouverte)
                unlocked_boxes[key] = True
                stack.append(key)  # Et on ajoute la boîte à la pile

    # On si toutes les boîtes sont ouvertes
    return all(unlocked_boxes)
