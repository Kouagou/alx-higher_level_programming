#include "lists.h"

/**
 * insert_node - A function in C that inserts a number
 * into a sorted singly linked list.
 * @head: pointer to pointer of first node of listint_t list.
 * @number: integer to be included into the sorted singly linked list.
 *
 * Return: Returns the address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;
	listint_t *prev = NULL;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	if (*head == NULL)
		*head = new;
	else
	{
		while (current->next != NULL && current->n < number)
		{
			prev = current;
			current = current->next;
		}

		if (current->next == NULL)
		{
			if (prev == NULL)
			{
				new->next = current;
			}
			else
			{
				new->next = NULL;
				current->next = new;
			}
		} else
		{
			if (prev == NULL)
			{
				new->next = current;
				*head = new;
			} else
			{
				prev->next = new;
				new->next = current;
			}
		}

	}

	return (new);
}
