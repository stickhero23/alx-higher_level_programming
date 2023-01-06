#include "lists.h"

/*
 * insert_node - malloc and insert node into sorted list
 * @head: pointer to head of linked list
 * @number: data for new node
 * Return: address of new node or NULL on fail
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = NULL;
	listint_t *new = NULL;

	if (!head)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
		(*head)->next = NULL;
		return (new);
	}
	tmp = *head;
	while (tmp->next != NULL)
	{
		if (new->n < tmp->n)
		{
			new->next = tmp;
			*head = new;
			return (new);
		}
		if (((new->n > tmp->n) && (new->n < (tmp->next)->n)) ||
			(new->n == tmp->n))
		{
			new->next = tmp->next;
			tmp->next = new;
			return (new);
		}
		tmp = tmp->next;
	}
	tmp->next = new;
	return (new);
}
