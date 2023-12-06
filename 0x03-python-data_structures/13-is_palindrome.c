#include "lists.h"

/**
 * rev_listint - a function that reverses a string
 * @head: a pointer to the list
 * Return: a pointer to head of reversed list
 */
void rev_listint(listint_t **head)
{
	listint_t *prevnode = NULL;
	listint_t *currentnode = *head;
	listint_t *nextnode = NULL;

	while (currentnode)
	{
		nextnode = currentnode->next;
		currentnode->next = prevnode;
		prevnode = currentnode;
		currentnode = nextnode;
	}
	*head = prevnode;
}

/**
 * is_palindrome - a function that checks if a list is a palindrome.
 * @head: a pointer to the linked list
 * Return: 1 if it is palindrome and 0 if otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *t = *head, *h = *head;
	listint_t *ptr = *head, *rlist = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (1)
	{
		h = h->next->next;
		if (h == NULL)
		{
			rlist = t->next;
			break;
		}
		if (h->next == NULL)
		{
			rlist = t->next->next;
			break;
		}

		t = t->next;
	}
	rev_listint(&rlist);
	while (rlist && ptr)
	{
		if (ptr->n == rlist->n)
		{
			rlist = rlist->next;
			ptr = ptr->next;
		}
		else
			return (0);
	}
	if (rlist == NULL)
		return (1);
	return (0);
}
