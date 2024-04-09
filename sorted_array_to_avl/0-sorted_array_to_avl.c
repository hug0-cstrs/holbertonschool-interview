#include "binary_trees.h"

/**
 * binary_tree_node - Creates a binary tree node.
 * @parent: Pointer to the parent node of the node to create.
 * @value: Value to put in the new node.
 *
 * Return: Pointer to the new node, or NULL if fail.
 */
binary_tree_t *binary_tree_node(binary_tree_t *parent, int value)
{
	binary_tree_t *new_node = NULL;

	new_node = malloc(sizeof(binary_tree_t)); /* Allocate memory */

	if (!new_node) /* Check if memory allocation failed */
		return (NULL);

  /* Initialize new node */
	new_node->parent = parent;
	new_node->left = NULL;
	new_node->right = NULL;
	new_node->n = value;

	return (new_node);
}

/**
 * sort_insert - Inserts nodes recursively to construct a binary search tree.
 * @array: Pointer to the first element of the array.
 * @min: Lower limit index for array segment.
 * @max: Upper limit index for array segment.
 *
 * Return: Pointer to the root node of the created AVL tree, or NULL on failure
 */
avl_t *sort_insert(int *array, int min, int max)
{
	int half; /* Middle index */
	avl_t *tree;

	if (min > max)
		return (NULL);

	half = (max + min) / 2; /* Calculate middle index */

	tree = binary_tree_node(NULL, array[half]); /* Create node */
	if (!tree) /* Check if node creation failed */
		return (NULL);

	/* Recursively build left subtree */
	tree->left = sort_insert(array, min, half - 1);

	/* Recursively build right subtree */
	tree->right = sort_insert(array, half + 1, max);

	/* Update parent pointers of the left and right child nodes */
	if (tree->left)
		tree->left->parent = tree;

	if (tree->right)
		tree->right->parent = tree;

	return (tree);
}

/**
 * sorted_array_to_avl - Builds an AVL tree from a sorted array.
 * @array: Pointer to the first element of the array.
 * @size: Number of elements in the array.
 *
 * Return: Pointer to the root node of the created AVL tree, or NULL on failure
 */
avl_t *sorted_array_to_avl(int *array, size_t size)
{
	avl_t *root = NULL; /* Root node */

	if (!array || size < 1) /* Check if array is empty */
		return (NULL);

	root = sort_insert(array, 0, size - 1); /* Construct AVL tree */

	return (root);
}
