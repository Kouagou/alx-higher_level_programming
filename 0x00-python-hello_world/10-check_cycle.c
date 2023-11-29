#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - A function that checks
 * if a singly linked list has a cycle in it.
 * @list: the list to be checked
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL && list->next == NULL)
		return (0);

	slow = list;
	fast = slow->next;
	while (fast != NULL && fast->next != NULL)
	{
		if (slow == fast)
			return (1);

		slow = slow->next;
		fast = fast->next->next;
	}

	return (0);
}
