#!/usr/bin/python3

def canUnlockAll(boxes):
    # Créer une liste pour suivre les boîtes ouvertes
    unlocked_boxes = [False] * len(boxes)
    unlocked_boxes[0] = True # Ondéfinit la première boîte comme déjà ouverte

    # On créer une pile (stack) pour effectuer une recherche dans les boîtes
    stack = [0] # Commencer avec la première boîte

    # Parcourir toutes les boîtes qui sont accessibles
    while stack:
        current_box = stack.pop() # On prend la boîte qui est en haut de la pile (stack)

        # On parcours toutes les boîtes accessibles avec les clés de la boîte courante
        for key in boxes[current_box]:
            if key < len(boxes) and not unlocked_boxes[key]: # On vérifie si la boîte n'est pas déjà ouverte
                unlocked_boxes[key] = True # Si la boîte n'est pas ouverte, on met sa valeur à True (donc ouverte)
                stack.append(key) # Et on ajoute la boîte à la pile

    # On si toutes les boîtes sont ouvertes
    return all(unlocked_boxes)
