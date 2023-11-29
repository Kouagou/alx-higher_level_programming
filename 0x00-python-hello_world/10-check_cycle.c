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
	listint_t *current;

	if (list == NULL)
		return (0);

	current = list->next;
	while (current != NULL && current != list)
		current = current->next;

	return (current == list);
}
