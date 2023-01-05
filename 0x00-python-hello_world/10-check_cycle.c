#include "lists.h"

/**
 * check_cycle - checks if list is cycle
 * @list: input
 * Return: 0 for no cycle, 1 for cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	if (list == NULL)
		return (0);

	while (fast && slow && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}

