#include "lists.h"

/*
 * insert_node - malloc and insert node into sorted list
 * @head: pointer to head of linked list
 * @number: data for new node
 * Return: address of new node or NULL on fail
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp;
	listint_t *new_node;

	tmp = *head;
	if (!head)
		return (NULL);
	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number;
	if (!tmp || tmp->n >= number)
	{
		new_node->next = tmp;
		*head = new_node;
		return (new_node);
	}
	return (new_node);
}
