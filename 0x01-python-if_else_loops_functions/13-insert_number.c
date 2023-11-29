#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
#include <unistd.h>
/**
 * insert_node - inserts a node
 * @head: a linked list
 * @number: num to insert
 * Return: pointer to new head
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr = *head;
	listint_t *nw = NULL;
	listint_t *tp = NULL;

	if (!head)
		return (NULL);
	nw = malloc(sizeof(listint_t));
	if (!nw)
		return (NULL);

	nw->n = number;
	nw->next = NULL;

	if (!*head || (*head)->n > number)
	{
		nw->next = *head;
		return (*head = nw);
	}
	else
	{
		while (curr && curr->n < number)
		{
			tp = curr;
			curr = curr->next;
		}
		tp->next = nw;
		nw->next = curr;
	}
	return (nw);
}
