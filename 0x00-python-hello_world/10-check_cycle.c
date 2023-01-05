#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if list is cycle
 * @list: input
 * Return: 0 for no cycle, 1 for cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp;

	if (!list)
		return (0);
	while (list)
	{
		tmp = list;
		list = list->next;
		if (tmp <= list)
			return (1);
	}
	return (0);
}

