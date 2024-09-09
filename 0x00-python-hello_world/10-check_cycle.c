#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks for cycles in a singly-linked list
 * @list: input
 *
 * Return: int
 */

int check_cycle(listint_t *list)
{
	listint_t *t, *h;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}
	t = list->next;
	h = list->next->next;
	while (t && h && h->next)
	{
		if (t == h)
		{
			return (1);
		}
		t = t->next;
		h = h->next->next;
	}
	return (0);
}
